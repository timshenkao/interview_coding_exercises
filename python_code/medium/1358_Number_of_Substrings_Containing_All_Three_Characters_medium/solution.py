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

# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


class Solution:
    # Similar to 3. Longest SubWithout Repeating Characters
    def number_of_substrings(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        ans = 0
        count = {c: 0 for c in "abc"}
        l = 0
        for c in s:
            count[c] += 1
            while min(count.values()) > 0:
                count[s[l]] -= 1
                l += 1
            # s[0..r], s[1..r], ..., s[l - 1..r] are satisfied strings.
            ans += l
        return ans

    def number_of_substrings2(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        ans = 0
        # last_seen[c] - the index of the last time c appeared
        last_seen = {c: -1 for c in 'abc'}
        for i, c in enumerate(s):
            last_seen[c] = i
            # s[0..i], s[1..i], s[min(last_seen)..i] are satisfied strings.
            ans += 1 + min(last_seen.values())
        return ans
