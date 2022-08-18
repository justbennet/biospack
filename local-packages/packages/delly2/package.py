# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class Delly2(MakefilePackage):
    """Delly2 is an integrated structural variant prediction method that can
    discover, genotype and visualize deletions, tandem duplications,
    inversions and translocations at single-nucleotide resolution in
    short-read massively parallel sequencing data.."""

    homepage = "https://github.com/dellytools/delly"
    git = "https://github.com/dellytools/delly.git"

    # Dev branch had version 0.9.1 using tag only. I switched it to commit ID.
    version("0.9.1", commit='ef1cd626a85cfd1c1b7acfca2b5fd5957f2a05f1')
    version("2017-08-03", commit="e32a9cd55c7e3df5a6ae4a91f31a0deb354529fc", deprecated=True)

    variant("openmp", default=False, description="Build with openmp support")

    depends_on("htslib", type=("build", "link"))
    depends_on("boost", type=("build", "link"))
    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    #    depends_on(Boost.with_default_variants)
    # Did not recognize "with_default_variants" for Boost, so I switched
    # it to a normal depends_on. jshelly 17 Aug 2022
    depends_on("boost")
    depends_on("bcftools", type="run")

    def edit(self, spec, prefix):
        if "+openmp" in self.spec:
            env["PARALLEL"] = "1"
        # Only want to build delly source, not submodules. Build fails
        # using provided submodules, succeeds with existing spack recipes.
        if self.spec.satisfies("@2017-08-03"):
            makefile = FileFilter("Makefile")
            makefile.filter("HTSLIBSOURCES =", "#HTSLIBSOURCES")
            makefile.filter("BOOSTSOURCES =", "#BOOSTSOURCES")
            makefile.filter("SEQTK_ROOT ?=", "#SEQTK_ROOT")
            makefile.filter("BOOST_ROOT ?=", "#BOOST_ROOT")
            makefile.filter("cd src", "# cd src")
            makefile.filter(".htslib ", "")
            makefile.filter(".bcftools ", "")
            makefile.filter(".boost ", "")
            makefile.filter(".htslib:", "# .htslib:")
            makefile.filter(".bcftools:", "# .bcftools:")
            makefile.filter(".boost:", "# .boost:")
        else:
            env["EBROOTHTSLIB"] = self.spec["htslib"].prefix
            filter_file("BUILT_PROGRAMS =.*$", "BUILT_PROGRAMS = src/delly src/dpe", "Makefile")
            filter_file("${SUBMODULES}", "", "Makefile", string=True)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with working_dir("src"):
            install("delly", prefix.bin)
            install("dpe", prefix.bin)
            if self.spec.satisfies("@2017-08-03"):
                install("cov", prefix.bin)
