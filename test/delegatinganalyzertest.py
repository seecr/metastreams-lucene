## begin license ##
#
# "Metastreams Lucene" is a set of components and tools to integrate Lucene into Metastreams
#
# Copyright (C) 2021-2022 Seecr (Seek You Too B.V.) https://seecr.nl
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

import unittest

from org.apache.lucene.analysis import Analyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer

from nl.metastreams.lucene.py_analysis import DelegatingAnalyzer
from nl.metastreams.lucene.py_analysis import DocumentUtil

class DelegatingAnalyzerTest(unittest.TestCase):

    def test_analyzer(self):
        d = StandardAnalyzer()
        a = DelegatingAnalyzer(d, 10)

        assert 10 == a.getPositionIncrementGap("field1")

    def testDocumentUtil(self):
        d = DocumentUtil()
