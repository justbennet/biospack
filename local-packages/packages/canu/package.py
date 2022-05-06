# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Canu(MakefilePackage):
    """A single molecule sequence assembler for genomes large and
       small."""

    homepage = "https://canu.readthedocs.io/"
#    url      = "https://github.com/marbl/canu/archive/v1.5.tar.gz"

    version('2.2',   sha256='e4d0c7b82149114f442ccd39e18f7fe2061c63b28d53700ad896e022b73b7404')
    version('2.1.1', sha256='18c030ada93286be90c364387879025c17001c8e445e64719c866bc6c7609b98')
    version('2.1',   sha256='73c70d2d6326bdaf471549f2d1eb7a1bf1e0fbf45cdc4a830bd6ce9fe3f3c231')
    version('2.0',   sha256='e2e6e8b5ec4dd4cfba5e372f4a64b2c01fbd544d4b5867746021f10771a6f4ef')
    version('1.9',   sha256='6b086ab6086c050752166500378bc4b3b3543d4c617863e894d296171cee3385')
    version('1.8',   sha256='30ecfe574166f54f79606038830f68927cf0efab33bdc3c6e43fd1448fa0b2e4')
    version('1.7.1', sha256='c314659c929ee05fd413274f391463a93f19b8337eabb7ee5de1ecfc061caafa')
    version('1.7',   sha256='c5be54b0ad20729093413e7e722a19637d32e966dc8ecd2b579ba3e4958d378a')
    version('1.5',   sha256='06e2c6d7b9f6d325b3b468e9c1a5de65e4689aed41154f2cee5ccd2cef0d5cf6')

    depends_on('gnuplot', type='run')
    depends_on('java', type='run')
    depends_on('perl', type='run')
    # build fail when using boost@1.71.0:1.73.0 by canu@1.8:2.0
    depends_on('boost@:1.70.0')

    build_directory = 'src'
    build_targets = ['clean']

    def patch(self):
        # Use our perl, not whatever is in the environment
        filter_file(r'^#!/usr/bin/env perl',
                    '#!{0}'.format(self.spec['perl'].command.path),
                    'src/pipelines/canu.pl')

    def url_for_version(self, version):
        if version > Version('2.1'):
            url = "https://github.com/marbl/canu/releases/download/v{0}/canu-{0}.tar.xz"
            return url.format(version)
        elif version > Version('2.0'):
            url = "https://github.com/marbl/canu/releases/download/v{0}/canu-{0}.tar.gz"
            return url.format(version)
        else:
            url = "https://github.com/marbl/canu/archive/v{0}.tar.gz"
            return url.format(version)

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make('all', 'TARGET_DIR={0}'.format(prefix))
