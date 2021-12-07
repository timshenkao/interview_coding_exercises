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

# 482. License Key Formatting  https://leetcode.com/problems/license-key-formatting/
# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group,
# which could be shorter than k but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to
# uppercase.
# Return the reformatted license key.
# 1 <= s.length <= 100 000
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 10 000

DASH = '-'


class Solution:
    def license_key_formatting(self, s: str, k: int) -> str:
        """ Time complexity: O(n).
            Space complexity: O(1). We create additional list to keep generated characters.
        """
        result = list()
        temp_count = k
        for i in range(len(s) - 1, - 1, -1):
            if temp_count == 0 and s[i] != DASH:
                result.append(DASH)
                temp_count = k
            if s[i] != DASH:
                result.append(s[i].upper())
                temp_count -= 1

        result.reverse()
        return ''.join(result)
