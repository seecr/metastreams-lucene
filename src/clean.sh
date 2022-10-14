#!/bin/bash

test -d build && rm -rf build
test -d root && rm -rf root
test -d metastreams_lucene.egg-info && rm -rf metastreams_lucene.egg-info
test -L ../metastreams_lucene && rm ../metastreams_lucene
