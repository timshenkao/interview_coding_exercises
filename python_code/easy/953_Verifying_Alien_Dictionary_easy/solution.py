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

# 953. Verifying an Alien Dictionary https://leetcode.com/problems/verifying-an-alien-dictionary/
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
# the given words are sorted lexicographically in this alien language.
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.


class Solution:
    def is_alien_sorted(self, words, order):
        """ Time complexity: O(n).
            Space complexity: O(26) = O(1).
        """
        # TC: O(26) = O(1)   SC: O(26) = O(1)
        ind = {c: i for i, c in enumerate(order)}
        # TC O(n)
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            # TC O(1)
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] == ind[s2]:
                    continue
                else:
                    return False
        return True

    def is_alien_sorted2(self, words, order):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        # TC: O(26) = O(1)   SC: O(26) = O(1)
        dict = {c: i for i, c in enumerate(order)}
        # TC: O(n)   SC: O(n) We create new list of integers
        words = [[dict[c] for c in word] for word in words]
        # TC: O(n)   SC: O(1)
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
