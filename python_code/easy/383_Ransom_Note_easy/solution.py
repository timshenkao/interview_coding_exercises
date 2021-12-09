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


# 383. Ransom Note  https://leetcode.com/problems/ransom-note/
# Given two stings ransom_note and magazine, return true if ransom_note can be constructed from magazine and
# false otherwise.
# Each letter in magazine can only be used once in ransom_note.
# 1 <= ransom_note.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        """ Time complexity: Formally O(max(N, M)). Where N - length of ransom_ransom_note; M - length of magazine.
                             But in reality, it's O(M)
            Space complexity: O(1). We create additional dictionary but it can be just 26 elements at most as both
            strings consist of lowercase English letters
        """
        if not magazine and ransom_note:
            return False

        available_characters = dict()
        for ch in magazine:
            freq = available_characters.setdefault(ch, 0)
            available_characters[ch] = freq + 1

        for ch in ransom_note:
            # there is no such letter in magazine
            if ch not in available_characters:
                return False
            # all such letters from magazine are "used"
            elif available_characters[ch] == 0:
                return False
            else:
                available_characters[ch] -= 1
        return True
