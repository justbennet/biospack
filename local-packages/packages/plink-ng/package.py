# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PlinkNg(Package):
    """A comprehensive update to the PLINK association analysis toolset."""

    homepage = "https://www.cog-genomics.org/plink/2.0/"
    url      = "https://www.cog-genomics.org/static/bin/plink2_src_220503.zip"

    version('220503', sha256='e08041189670e03839ea12296fa530be3c1ee8a16fc2f64ef0b838c205fae8c1')

    depends_on('zlib')
    depends_on('zstd@1.4.4:')
    depends_on('cblas')
    depends_on('blas')
    depends_on('lapack')

    conflicts('%gcc@:4')

    def url_for_version(self, ver):
        template = 'https://www.cog-genomics.org/static/bin/plink2_src_{0}.zip'
        return template.format(ver)

    def setup_build_environment(self, env):
        zlib = join_path(self.spec['zlib'].prefix.lib, 'libz.a')
        env.set('ZLIB', zlib)

    def install(self, spec, prefix):
        ld_flags = [spec['lapack'].libs.ld_flags, spec['blas'].libs.ld_flags]
        filter_file('-llapack -lcblas -lblas', ' '.join(ld_flags),
                    'build.sh', string=True)
        which('sh')('build.sh')
        install_tree('.', prefix)
