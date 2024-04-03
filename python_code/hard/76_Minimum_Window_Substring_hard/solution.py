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
    def minWindow(self, s, t):
        cnt_s, cnt_t, n, left, r = {}, {}, len(s), set(t), -1
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        L = l = 0
        while left:
            r += 1
            if r >= n:
                return ""
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            if s[r] in cnt_t and cnt_s[s[r]] == cnt_t[s[r]]:
                left.discard(s[r])
        R = r
        cnt_s[s[r]] -= 1
        while l < r < n:
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            while s[l] not in cnt_t or cnt_s[s[l]] > cnt_t[s[l]]:
                cnt_s[s[l]] -= 1
                l += 1
            if r - l < R - L:
                L, R = l, r
            r += 1
        return s[L: R + 1]

    
Time: O(m+n)
Space: O(128)=O(1)
Hash table
Sliding Window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = collections.Counter(t)
        required = len(t)
        bestLeft = -1
        minLength = len(s) + 1

        l = 0
        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            while required == 0:
                if r - l + 1 < minLength:
                    bestLeft = l
                    minLength = r - l + 1
                count[s[l]] += 1
                if count[s[l]] > 0:
                    required += 1
                l += 1

        return '' if bestLeft == -1 else s[bestLeft: bestLeft + minLength]