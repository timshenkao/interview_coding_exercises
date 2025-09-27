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
import heapq
import random

# 215. Kth Largest Element in an Array https://leetcode.com/problems/kth-largest-element-in-an-array/
#  Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


class Solution:
    def find_kth_largest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    def find_kth_largest2(self, nums: List[int], k: int) -> int:
        """ Time complexity: O(n log k)
            Space complexity: O(k).
        """
        min_heap = []
        # Add all numbers to min-heap, keeping only k largest
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # this removal happens (n-k) times
        return min_heap[0]

    def find_kth_largest_recursive(self, nums: List[int], k: int) -> int:
        """ Time complexity: O(n) to O(n^2)
            Space complexity: O(1) if recursion stack not considered
                              Recursion stack is O(log n) average, O(n) worst case
            It fails on test case with 100 005 array elements and k = 50 000
        """
        def quick_select(l: int, r: int, z: int) -> int:
            pivot = nums[r]
            next_swapped = l

            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[next_swapped], nums[i] = nums[i], nums[next_swapped]
                    next_swapped += 1
            nums[next_swapped], nums[r] = nums[r], nums[next_swapped]

            count = next_swapped - l + 1  # Number of nums >= pivot
            if count == z:
                return nums[next_swapped]
            if count > z:
                return quick_select(l, next_swapped - 1, z)
            return quick_select(next_swapped + 1, r, z - count)

        return quick_select(0, len(nums) - 1, k)

    def find_kth_largest_recursive2(self, nums: List[int], k: int) -> int:
        """ Time complexity: O(n) to O(n^2). Average O(n)
            Space complexity: O(1) if recursion stack not considered
                              Recursion stack is O(log n) average, O(n) worst case
            It fails on test case with 100 005 array elements and k = 50 000
        """
        def quick_select(l: int, r: int, z: int) -> int:
            rand_index = random.randint(0, r - l) + l
            nums[rand_index], nums[r] = nums[r], nums[rand_index]
            pivot = nums[r]
            next_swapped = l
            # Partition: move elements > pivot to left, <= pivot to right
            # i.e. somewhat sort array in decreasing order
            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[next_swapped], nums[i] = nums[i], nums[next_swapped]
                    next_swapped += 1
            # Place pivot in its final position
            nums[next_swapped], nums[r] = nums[r], nums[next_swapped]

            count = next_swapped - l + 1  # Number of nums >= pivot
            if count == z:
                return nums[next_swapped]
            # If kth largest is in left partition (larger values)
            if count > z:
                return quick_select(l, next_swapped - 1, z)
            # If kth largest is in right partition (smaller values)
            return quick_select(next_swapped + 1, r, z - count)

        return quick_select(0, len(nums) - 1, k)
