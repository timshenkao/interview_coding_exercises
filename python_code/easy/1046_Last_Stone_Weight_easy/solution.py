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

# 1046. Last Stone Weight https://leetcode.com/problems/last-stone-weight/
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#   If x == y, both stones are destroyed
#   If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#   At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

from heapq import heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ Time complexity: O(n log n). Push O(log n). Pop O(log n)
            Space Complexity**: O(n). The heap stores at most n elements.
        """
        heap = []
        for stone in stones:
            # heapq supports MIN heap; for MAX heap, invert the sign
            # heapq has "undocumented" functions for MAX heaps:
            #       _heapify_max, _heappush_max, _heappop_max, _siftdown_max,_siftup_max.
            heappush(heap, -stone)

        while len(heap) > 1:
            # stone1 is the heaviest by now
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            if stone1 != stone2:
                # negative values are kept in heap because of MAX heap
                # push neagtive value back to heap
                heappush(heap, -(-stone1 - (-stone2)))
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]
