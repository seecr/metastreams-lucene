#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## begin license ##
#
# "Metastreams Lucene" is a set of components and tools to integrate Lucene into Metastreams
#
# Copyright (C) 2007-2008 SURF Foundation. http://www.surf.nl
# Copyright (C) 2007-2010 Seek You Too (CQ2) http://www.cq2.nl
# Copyright (C) 2007-2009 Stichting Kennisnet Ict op school. http://www.kennisnetictopschool.nl
# Copyright (C) 2009-2010 Delft University of Technology http://www.tudelft.nl
# Copyright (C) 2009 Tilburg University http://www.uvt.nl
# Copyright (C) 2012-2013, 2015, 2019, 2021-2022 Seecr (Seek You Too B.V.) https://seecr.nl
# Copyright (C) 2012-2013 Stichting Bibliotheek.nl (BNL) http://www.bibliotheek.nl
# Copyright (C) 2015 Koninklijke Bibliotheek (KB) http://www.kb.nl
# Copyright (C) 2021 Data Archiving and Network Services https://dans.knaw.nl
# Copyright (C) 2021 SURF https://www.surf.nl
# Copyright (C) 2021 Stichting Kennisnet https://www.kennisnet.nl
# Copyright (C) 2021 The Netherlands Institute for Sound and Vision https://beeldengeluid.nl
#
# This file is part of "Metastreams Lucene"
#
# "Metastreams Lucene" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Metastreams Lucene" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Metastreams Lucene"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

version = '$Version: trunk$'[9:-1].strip()
name = 'metastreams-lucene'

from os import walk
from os.path import join, dirname

from setuptools import setup
from setuptools.command.install import install


class CompileJccExtension(install):
    """Post-installation for installation mode."""
    def run(self):
        root = join(dirname(__file__), self.root)
        import os
        os.system(f"./compile-meresco-jar --target={root} --version=1.7.2.2")
        install.run(self)

for path, dirs, files in walk('doc'):
    files = [f for f in files if f != 'license.conf']
    if files:
        data_files.append((path.replace('doc', '/usr/share/doc/%s' % name, 1), [join(path, f) for f in files]))

setup(
    name=name,
    cmdclass={
        'install': CompileJccExtension,
    },
    version = version,
    url = 'https://seecr.nl',
    author = 'Seecr (Seek You Too B.V.)',
    author_email = 'info@seecr.nl',
    description = 'Python wrappers for components in Meresco Lucene',
    long_description = '"Metastream Lucene" is a set of python wrappers for components in Meresco Lucene',
    license = 'GPLv2',
    platforms = 'all',
)
