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

# 703. Kth Largest Element in a Stream  https://leetcode.com/problems/kth-largest-element-in-a-stream/
# You are part of a university admissions office and need to keep track of the kth highest test score from applicants
# in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants
# submit their scores.
# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously
# returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the
# kth highest score in the sorted list of all scores.
# Implement the KthLargest class:
#       KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
#       int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest
#       element in the pool of test scores so far.
# 0 <= nums.length <= 10^4
# 1 <= k <= nums.length + 1
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# At most 10^4 calls will be made to add.


from heapq import heappush, heappop


class Solution:
    """ TC:
            Constructor: O(n log k)
            add(val): O(log k).
        Total for m calls to add: O(n log k + m log k).
        SC: O(k). The min-heap stores at most k elements

    """
    def __init__(self, k: int, nums: List[int]):
        # Each of n insertions is O(log k) (heap push), and up to n-k pops are O(log k).
        self.k = k
        self.heap = []
        # Add all numbers to min-heap, keeping only k largest
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        # One push (O(log k)) and at most one pop (O(log k)) if size exceeds k.
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
