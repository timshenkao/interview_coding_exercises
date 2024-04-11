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

 # 408. Valid Word Abbreviation https://leetcode.com/problems/valid-word-abbreviation/
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
# The lengths should not have leading zeros.
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#       "s10n" ("s ubstitutio n")
#       "sub4u4" ("sub stit u tion")
#       "12" ("substitution")
#       "su3i1u2on" ("su bst i t u ti on")
#       "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#       "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
#        "s010n" (has leading zeros)
#        "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
# A substring is a contiguous non-empty sequence of characters within a string.
# 1 <= word.length <= 20
# word consists of only lowercase English letters.
# 1 <= abbr.length <= 10
# abbr consists of lowercase English letters and digits.
# All the integers in abbr will fit in a 32-bit integer.


class Solution:
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        i = num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                if num:
                    i += num
                    num = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        return i == len(word) if num == 0 else i + num == len(word)

    def valid_word_abbreviation2(self, word: str, abbr: str) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        i = 0  # word's index
        j = 0  # abbr's index
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if not abbr[j].isdigit() or abbr[j] == '0':
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        return i == len(word) and j == len(abbr)
