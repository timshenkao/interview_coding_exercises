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

from typing import List, Set


# 350. Intersection of Two Arrays II https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.


class Solution:
    def _intersect(self, set1: Set, set2: Set) -> Set:
        return set(elem for elem in set1 if elem in set2)

    def _fillin_map(self, arr: List[int], intersection: Set) -> dict:
        result = dict()
        for i in arr:
            if i in intersection:
                result[i] = result.get(i, 0) + 1
        return result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Time complexity: O(N).
            Space complexity: O(N).
        """
        set1 = set(nums1)
        set2 = set(nums2)

        # the set with smaller cardinality goes first to make less iterations in helper function
        if len(set1) < len(set2):
            intersection = self._intersect(set1, set2)
        else:
            intersection = self._intersect(set2, set1)

        # fill in dictionaries with frequencies
        nums1_map = self._fillin_map(nums1, intersection)
        nums2_map = self._fillin_map(nums2, intersection)

        result = []
        for k in nums1_map:
            freq = min(nums1_map[k], nums2_map[k])
            for i in range(freq):
                result.append(k)
        return result
