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

# 49. Group Anagrams  https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.



class Solution:
    def _calculate_str_signature(self, s: str) -> str:
        # empty string
        if not s:
            return ""
        # non-empty string
        temp = dict()
        # calculate frequencies of a character
        for i in range(len(s)):
            _ = temp.setdefault(s[i], 0)
            temp[s[i]] += 1

        result = list()
        # signature is a character followed
        for key in sorted(temp.keys()):
            result.append(key + str(temp[key]))
        return "".join(result)

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """ Time complexity: O(N * M * log M). N - number of strings, M - length of the longest string. We iterate
                             through list of strings once and compute signatures. Log appears because of sorted() in
                             auxiliary function
            Space complexity: O(N * M). We create list of lists that contain the same number of letters / characters as
                              in original list of strings.
        """
        # empty list
        if not strs:
            return [[""]]

        signatures = dict()
        for elem in strs:
            # calculate signature of a string
            str_signature = self._calculate_str_signature(elem)
            # we have seen a string with the same signature
            if str_signature in signatures:
                signatures[str_signature].append(elem)
            # we haven't seen such signature yet
            else:
                signatures[str_signature] = [elem]

        result = list()
        # there is list of strings per each signature
        for _, v in signatures.items():
            result.append(v)

        return result

    def group_anagrams_no_sorting(self, strs: List[str]) -> List[List[str]]:
        """ Time complexity: O(N * M). N - number of strings, M - length of the longest string. We iterate
                             through list of strings once and compute signatures. All signatures have fixed format.
            Space complexity: O(N * M). We create list of lists that contain the same number of letters / characters
                              as in original list of strings.
            M <= 100 by definition
        """
        # empty list
        if not strs:
            return [[""]]

        signatures = dict()
        for elem in strs:
            # calculate signature of a string; all characters are lowercase English letters by condition
            list_signature = [0] * 26
            for ch in elem:
                list_signature[ord(ch) - ord('a')] += 1
            tuple_signature = tuple(list_signature)
            # we have seen a string with the same signature
            if tuple_signature in signatures:
                signatures[tuple_signature].append(elem)
            # we haven't seen such signature yet
            else:
                signatures[tuple_signature] = [elem]

        result = list()
        # there is list of strings per each signature
        for _, v in signatures.items():
            result.append(v)

        return result
