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


# 290. Word Pattern  https://leetcode.com/problems/word-pattern/
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        """ Time complexity: O(N). We iterate through pattern and string.
            Space complexity: O(M). We create 2 dictionaries, the second dictionary may contain M words.
        """
        words = s.split()
        # pattern must have as many letters as words in the string
        if len(words) != len(pattern):
            return False

        # keep pattern-to-word correspondence
        table = dict()
        # keep word-to-pattern correspondence
        reverse_table = dict()
        for i in range(len(pattern)):
            if (not pattern[i] in table) and (not words[i] in reverse_table):
                table[pattern[i]] = words[i]
                reverse_table[words[i]] = pattern[i]
            elif (pattern[i] in table and table[pattern[i]] != words[i]) or \
                    (words[i] in reverse_table and reverse_table[words[i]] != pattern[i]):
                return False
        return True
