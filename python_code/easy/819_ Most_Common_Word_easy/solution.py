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

# 819. Most Common Word https://leetcode.com/problems/most-common-word/
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        """ Time complexity: O(n). But constant could be high as we iterate through the whole string and list of words
        several times.
            Space complexity: O(n). In the worst case scenario, we keep all words.
        """
        # Time O(n) to remove punctuation
        # Space O(n) in worst case for new string
        # substitute punctuation with spaces
        out_string = "".join(c.lower() if c not in ('!','.',';', '?', ',', "'") else ' ' for c in paragraph)

        # Time O(n) to split
        # Space O(n) in worst case for new list
        # split() removes all whitespaces in Python, split(' ') removes just 1 space
        out_list = out_string.split()

        # remove banned words
        # Time O(n) if time to check that word is not in banned list is O(1)
        # If checking time is O(k) (where k - number of words in banned list), then total time is O(n * k)
        out_list = [w for w in out_list if w not in banned]

        out_dict = {}
        max = 0
        max_elem = ""

        for elem in out_list:
            if elem in out_dict:
                out_dict[elem] += 1
            else:
                out_dict[elem] = 1
            if out_dict[elem] > max:
                max = out_dict[elem]
                max_elem = elem
        return max_elem
