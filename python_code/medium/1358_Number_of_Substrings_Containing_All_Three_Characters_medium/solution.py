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

Approach 1: Sliding window
Time: O(n)
Space: O(3)=O(1)


class Solution:
    # Similar to 3. Longest SubWithout Repeating Characters
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        count = {c: 0 for c in 'abc'}

        l = 0
        for c in s:
            count[c] += 1
            while min(count.values()) > 0:
                count[s[l]] -= 1
                l += 1
            # s[0..r], s[1..r], ..., s[l - 1..r] are satified strings.
            ans += l

        return ans



Approach 2: Last seen
Time: O(n)
Space: O(3)=O(1)


class Solution:
    # Similar to 3. Longest SubWithout Repeating Characters
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        # lastSeen[c] := the index of the last time c appeared
        lastSeen = {c: -1 for c in 'abc'}

        for i, c in enumerate(s):
            lastSeen[c] = i
            # s[0..i], s[1..i], s[min(lastSeen)..i] are satisfied strings.
            ans += 1 + min(lastSeen.values())

        return ans