# Copyright (c) 2021 - present, Timur Shenkao
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

Time: O(∣encoded1∣+∣encoded2∣)
Space: O(∣encoded1∣+∣encoded2∣)

class Solution:
    def findRLEArray(self, encoded1: List[List[int]],
                     encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0  # encoded1's index
        j = 0  # encoded2's index

        while i < len(encoded1) and j < len(encoded2):
            mult = encoded1[i][0] * encoded2[j][0]
            minFreq = min(encoded1[i][1], encoded2[j][1])
            if ans and mult == ans[-1][0]:
                ans[-1][1] += minFreq
            else:
                ans.append([mult, minFreq])
            encoded1[i][1] -= minFreq
            encoded2[j][1] -= minFreq
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return ans