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

# 500. Keyboard Row   https://leetcode.com/problems/keyboard-row/
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of
# American keyboard.
# In the American keyboard:
#     the first row consists of the characters "qwertyuiop",
#     the second row consists of the characters "asdfghjkl", and
#     the third row consists of the characters "zxcvbnm".


class Solution:
    def find_words(self, words: List[str]) -> List[str]:
        """ Time complexity: O(N). We iterate through array of words, each word has 1 <= words[i].length <= 100.
                             If each word's length weren't strictly limited, than O(N * M)
            Space complexity: O(N). We create result array which may contain N words in worst case.
                              We also create 3 fixed-size sets of letters O(1) and current word's set of letters O(1).
        """
        first_row_set = set("qwertyuiop")
        second_row_set = set("asdfghjkl")
        third_row_set = set("zxcvbnm")
        result = list()

        for elem in words:
            curr_set = set(elem.lower())
            if curr_set.issubset(first_row_set) \
                    or curr_set.issubset(second_row_set) or curr_set.issubset(third_row_set):
                result.append(elem)
        return result
