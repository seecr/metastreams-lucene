## begin license ##
#
# "Metastreams Lucene" is a set of components and tools to integrate Lucene into Metastreams
#
# Copyright (C) 2013-2016, 2019, 2021-2023 Seecr (Seek You Too B.V.) https://seecr.nl
# Copyright (C) 2013-2014 Stichting Bibliotheek.nl (BNL) http://www.bibliotheek.nl
# Copyright (C) 2015-2016 Koninklijke Bibliotheek (KB) http://www.kb.nl
# Copyright (C) 2016, 2021 Stichting Kennisnet https://www.kennisnet.nl
# Copyright (C) 2021 Data Archiving and Network Services https://dans.knaw.nl
# Copyright (C) 2021 SURF https://www.surf.nl
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

from os.path import join, dirname, islink                               #DO_NOT_DISTRIBUTE
import os, sys                                                          #DO_NOT_DISTRIBUTE
parentDir = dirname(dirname(__file__))                                  #DO_NOT_DISTRIBUTE
srcDir = join(parentDir, "src")                                         #DO_NOT_DISTRIBUTE
targetDir = join(srcDir, "root")                                        #DO_NOT_DISTRIBUTE
retcode = os.system(f"cd {srcDir}; ./build.sh {targetDir}")             #DO_NOT_DISTRIBUTE
if retcode != 0:                                                        #DO_NOT_DISTRIBUTE
    print("Build command failed.")                                      #DO_NOT_DISTRIBUTE
    sys.exit(1)                                                         #DO_NOT_DISTRIBUTE
for dist in ['dist-packages', 'site-packages']:                         #DO_NOT_DISTRIBUTE
    for p, d, f in os.walk(targetDir):                                  #DO_NOT_DISTRIBUTE
        if dist in d:                                                   #DO_NOT_DISTRIBUTE
            fullDistDir = join(targetDir, p, dist)                      #DO_NOT_DISTRIBUTE
            linkSource = join(fullDistDir, "metastreams_lucene")        #DO_NOT_DISTRIBUTE
            linkTarget = join(parentDir, 'metastreams_lucene')          #DO_NOT_DISTRIBUTE
            if not islink(linkTarget):                                  #DO_NOT_DISTRIBUTE
                os.symlink(linkSource, linkTarget)                      #DO_NOT_DISTRIBUTE
            break                                                       #DO_NOT_DISTRIBUTE

from seecrdeps import includeParentAndDeps       #DO_NOT_DISTRIBUTE
includeParentAndDeps(__file__)                   #DO_NOT_DISTRIBUTE


import lucene
import metastreams_lucene
lucene.initVM(classpath=":".join([lucene.CLASSPATH, metastreams_lucene.CLASSPATH]))

import unittest
from warnings import simplefilter, filterwarnings
simplefilter('default')
filterwarnings('ignore', message=r".*has no __module__ attribute.*", category=DeprecationWarning)

from delegatinganalyzertest import DelegatingAnalyzerTest
from documentutiltest import DocumentUtilTest

if __name__ == '__main__':
    unittest.main()
