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

# 1331. Rank Transform of an Array https://leetcode.com/problems/rank-transform-of-an-array/
# Given an array of integers arr, replace each element with its rank.
# The rank represents how large the element is. The rank has the following rules:
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
# 0 <= arr.length <= 10^5
# -10^9 <= arr[i] <= 10^9


class Solution:
    def array_rank_transform(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(nlogn)
            Space complexity: O(n)
        """
        # Space Complexity O(n) because of additional dict
        rank = {}
        # sorting Time Complexity O(nlogn)
        for a in sorted(arr):
            if a not in rank:
                rank[a] = len(rank) + 1
        x = map(rank.get, arr)
        return x
