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

# 58. Length of Last Word  https://leetcode.com/problems/length-of-last-word/
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in
# the string.
# A word is a maximal substring consisting of non-space characters only.
# 1 <= s.length <= 10000
# s consists of only English letters and spaces ' '
# There will be at least one word in s
SPACE = ' '


class Solution:
    def length_of_last_word(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through string.
            Space complexity: O(1).
        """
        s_length = len(s) - 1
        last_non_space_flag = 0
        word_length = 0
        # iterate backwards
        while s_length >= 0:
            if s[s_length] == SPACE:
                # we have already seen non-space character, i.e. it's space before last word
                if last_non_space_flag:
                    return word_length
            # non-space character: set the flag, increase counter
            else:
                last_non_space_flag = 1
                word_length += 1
            s_length -= 1
        return word_length
