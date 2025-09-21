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

# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Given a string s and an integer k, return the length of the longest substring of s that contains at most k
# distinct characters.
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50


class Solution:
    def length_olskd(self, s: str, k: int) -> int:
        if not k:
            return 0
        cnt = collections.Counter()
        i = res = 0
        for j, c in enumerate(s):
            while len(cnt) == k and c not in cnt:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            cnt[c] += 1
            res = max(res, j - i + 1)
        return res

    def length_olskd2(self, s: str, k: int) -> int:
        """ Time complexity: O(N).
            Space complexity: O(256) = O(1). As there can be 128 or 256 characters
        """
        if not k:
            return 0
        ans = 0
        distinct = 0
        count = collections.Counter()

        # window sliding
        l = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            # new unseen character
            if count[ch] == 1:
                distinct += 1
            # move left pointer to the right if number of distinct characters > k
            while distinct == k + 1:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    distinct -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
