#!/bin/bash
## begin license ##
#
# "Metastreams Lucene" is a set of components and tools to integrate Lucene into Metastreams
#
# Copyright (C) 2021 Data Archiving and Network Services https://dans.knaw.nl
# Copyright (C) 2021 SURF https://www.surf.nl
# Copyright (C) 2021-2022 Seecr (Seek You Too B.V.) https://seecr.nl
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


MYDIR=$(cd $(dirname $0); pwd)

TARGET=$1
if [ -z "${TARGET}" ]; then
    TARGET="${MYDIR}/root"
fi

# only compile if:
#  - the target directory does not exist
#  - the .so file does not exist
#  - there are files in the source directory newer than the .so file
if [ -d "${TARGET}" ]; then
    SO_FILE=$(find ${TARGET} -name "_metastreams_lucene*.so" -type f -print | head -n 1)
    if [ ! -z "${SO_FILE}" ]; then
        NEWER_SRC_FILES=$(find ${MYDIR}/nl -newer ${SO_FILE})
        if [ -z "${NEWER_SRC_FILES}" ]; then
            exit 0
        fi
    fi
fi

./seecr-build-jcc \
    --path=${MYDIR} \
    --name=metastreams-lucene \
    --package=nl/metastreams/lucene/py_analysis \
    --jcc=3.10 \
    --lucene=8.9.0 \
    --target=${TARGET} \
    --java_home=/usr/lib/jvm/java-17-openjdk-amd64
