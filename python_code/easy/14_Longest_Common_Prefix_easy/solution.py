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

from typing import List

# 14. Longest Common Prefix  https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
MAX_LENGTH = 200


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        """ Time complexity: O(N). We iterate through array once and then check characters (min_length * N) times.
                             min_length is fixed and <= 200.
            Space complexity: O(1).
        """
        if not strs:
            return ''

        min_length = MAX_LENGTH
        # find length of the shortest string within array
        for elem in strs:
            if len(elem) < min_length:
                min_length = len(elem)

        # we keep prefix length
        prefix_length = 0
        # min_length is fixed and <= 200
        for i in range(min_length):
            # check characters in each string within array
            for j in range(len(strs)):
                # we found discrepancy, return accumulated prefix
                if strs[j][i] != strs[0][i]:
                    return strs[0][:prefix_length]
            prefix_length += 1
        return strs[0][:min_length]
