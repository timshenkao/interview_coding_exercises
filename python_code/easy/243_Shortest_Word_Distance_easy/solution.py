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

# 243. Shortest Word Distance https://leetcode.com/problems/shortest-word-distance/
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.


class Solution:
    def shortest_distance(self, words_dict: List[str], word1: str, word2: str) -> int:
        """ Time complexity: We iterate through array once.
                             If word comparison is O(1) operation, then O(n).
                             If word comparison is O(m) operation (m - total length of both words), then O(n * m)
            Space complexity: O(1).
        """
        shortest = -1
        word1_index = -1
        word2_index = -1

        for i in range(len(words_dict)):
            # index of word1 latest occurrence
            if words_dict[i] == word1:
                word1_index = i
            # index of word2 latest occurrence
            if words_dict[i] == word2:
                word2_index = i
            # if word1 and word2 have been already seen, calculate distance
            if word1_index != -1 and word2_index != -1:
                # if it's the first calculation of shortest distance
                if shortest == -1:
                    shortest = abs(word1_index - word2_index)
                # if we calculated shortest distance before
                else:
                    shortest = min(abs(word1_index - word2_index), shortest)
        return shortest
