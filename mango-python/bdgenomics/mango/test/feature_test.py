#
# Licensed to Big Data Genomics (BDG) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The BDG licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from bdgenomics.mango.test import SparkTestCase
from bdgenomics.mango.features import *

from bdgenomics.adam.adamContext import ADAMContext


class FeatureTest(SparkTestCase):

    def test_visualize_features(self):
        # load file
        ac = ADAMContext(self.ss)
        testFile = self.resourceFile("smalltest.bed")

        # read features
        features = ac.loadFeatures(testFile)

        featureViz = FeatureSummary(ac, features)

        contig = "chrM"
        start = 1
        end = 2000

        x = featureViz.viewPileup(contig, start, end)
        assert(x != None)
