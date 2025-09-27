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

from collections import Counter

# 347. Top K Frequent Elements https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
# order.
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List


class Solution:
    def top_k_frequent(self, nums, k):
        """ Time complexity: if k is not specified, then O(n log n).
                             if k is specified, then O(n log k) = O(n) since k << n and k - constant
            https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
            Space complexity: O(n).
        """
        return [key for (key,val) in Counter(nums).most_common(k)]

    def top_k_frequent_bucket(self, nums, k):
        """ Time complexity: O(n)
            Space complexity: O(n).
        """
        count = {}
        # calculate frequencies of integers
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # hand made priority queue
        # array of lists where index i stores elements with frequency i.
        pq = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            pq[value].append(key)

        result = []
        for i in range(len(pq) - 1, 0, -1):  # iterate backwards
            values = pq[i]
            for val in values:
                result.append(val)
                if len(result) == k:
                    return result
        return []

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """ Time complexity: O(n + m log k) where m - number of unique elements.
                             In worst case, when m = n and k = n O(n log n)
            Space complexity: O(n) = O(m + k).
            This approach is better when m << n and k << n
        """
        from heapq import heappush, heappop
        # Count frequency of each element
        freq_dict= {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        # Use min-heap to keep k most frequent elements
        # Building heap: O(m log k), where m is unique elements (m ≤ n). Each of m insertions is O(log k),
        # and up to m-k pops are O(log k).
        heap = []
        for num, frequency in freq_dict.items():
            heappush(heap, (frequency, num))
            if len(heap) > k:
                heappop(heap)

        # Extract elements from heap
        # O(k) to iterate heap.
        return [num for _, num in heap]
