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

class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for w in strings:
            pattern = ""
            for i in range(1, len(w)):
                if ord(w[i]) - ord(w[i - 1]) >= 0:
                    pattern += str(ord(w[i]) - ord(w[i - 1]))
                else:
                    pattern += str(ord(w[i]) - ord(w[i - 1]) + 26)
            table[pattern].append(w)
        return [table[pattern] for pattern in table]


Time: O(Σ∣strings[i]∣)
Space: O(Σ∣strings[i]∣)



class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        keyToStrings = collections.defaultdict(list)

        def getKey(s: str) -> str:
            """
            Returns the key of 's' by pairwise calculation of differences.
            e.g. getKey("abc") -> "1,1" because diff(a, b) = 1 and diff(b, c) = 1.
            """
            diffs = []

            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                diffs.append(str(diff))

            return ','.join(diffs)

        for s in strings:
            keyToStrings[getKey(s)].append(s)

        return keyToStrings.values()