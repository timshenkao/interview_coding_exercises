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

import collections

# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def length_ols(self, s):
        """ Time complexity: O(n).
            Space complexity: O(128) = O(256) = O(1).
        """
        mx, start, chars = 0, 0, {}
        for i in range(len(s)):
            if s[i] in chars and start <= chars[s[i]]:
                start = chars[s[i]] + 1
            else:
                mx = max(mx, i - start + 1)
            chars[s[i]] = i
        return mx

    def length_ols2(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(128) = O(256) = O(1).
        """
        ans = 0
        count = collections.Counter()
        l = 0
        # TC O(n)
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                # be careful here with TC
                l += 1
            ans = max(ans, r - l + 1)
        return ans

    def length_ols3(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(128) = O(256) = O(1).
        """
        ans = 0
        # The substring s[j + 1..i] has no repeating characters.
        j = -1
        # last_seen[c] := the index of the last time c appeared
        last_seen = {}

        for i, c in enumerate(s):
            # Update j to last_seen[c], so the window must start from j + 1.
            j = max(j, last_seen.get(c, -1))
            ans = max(ans, i - j)
            last_seen[c] = i
        return ans
