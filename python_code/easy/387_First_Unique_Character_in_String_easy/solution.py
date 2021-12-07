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

# 387. First Unique Character in a String   https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 1 <= s.length <= 105
# s consists of only lowercase English letters.



class Solution:
    def first_uniq_char(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through list once and through auxiliary dictionary as well.
            Space complexity: O(n). We create auxiliary dictionary to keep characters' frequencies.
        """
        result = dict()
        for i in range(len(s)):
            # we have seen the symbol already
            if s[i] in result:
                result[s[i]].append(i)
            # the first occurrence of a symbol
            else:
                result[s[i]] = [i]

        first_index = len(s)
        # iterate through auxiliary dictionary and find earliest character with single occurrence
        for k, v in result.items():
            # single occurrence
            if len(v) == 1:
                if v[0] < first_index:
                    first_index = v[0]

        if first_index < len(s):
            return first_index
        # if fisrt_index was not updated
        else:
            return -1
