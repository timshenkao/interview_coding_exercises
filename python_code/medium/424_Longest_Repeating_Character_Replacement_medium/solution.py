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

# 424. Longest Repeating Character Replacement https://leetcode.com/problems/longest-repeating-character-replacement/
# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times.
# Return the LENGTH of the longest substring containing the same letter you can get after performing the above
# operations.
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution:
    def replace_character(self, s, k):
        """ Time complexity: O(n).
            Space complexity: O(26) = 1.
        """
        dic, start, end = {}, 0, 0
        for end in range(1, len(s)+1):
            if not s[end-1] in dic:
                dic[s[end-1]] = 1
            else:
                dic[s[end-1]] += 1

            if end - start - max(dic.values()) > k:
                dic[s[start]] -= 1
                start += 1
        return end - start

    def replace_character2(self, s: str, k: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(26) = 1.
        """
        ans = 0
        max_count = 0
        count = collections.Counter()
        l = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])
            while max_count + k < r - l + 1:
                count[s[l]] -= 1
                # be careful here with TC
                l += 1
            ans = max(ans, r - l + 1)
        return ans

    def replace_character3(self, s: str, k: int) -> int:
        """ Time complexity: O(n) = O(2*n) because of sliding window
            Space complexity: O(26) = 1.
        """
        max_count = 0
        count = collections.Counter()
        # maximum window instead of the valid window
        left = 0
        right = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            # calculate for current character
            max_count = max(max_count, count[ch])
            # shrink window
            while max_count + k < right - left + 1:
                count[s[left]] -= 1
                left += 1
        return right - left + 1
