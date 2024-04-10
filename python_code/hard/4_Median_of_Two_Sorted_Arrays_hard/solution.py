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

# 4. Median of Two Sorted Arrays https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6


class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        """ Time complexity: O((n+m)log(n+m)).
            Space complexity: O(1) if sorting is in-place; O(n+m) otherwise.
        """
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else:
            return arr[len(arr) // 2]

    def find_median_sorted_arrays2(self, nums1, nums2):
        """ Time complexity: O(log min(m,n)).
             Space complexity: O(1).
        """
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.find_median_sorted_arrays2(nums2, nums1)
        l = 0
        r = n
        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (n + m + 1) // 2 - partition1

            max_left1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
            max_left2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]

            min_right1 = 2**31 - 1 if partition1 == n else nums1[partition1]
            min_right2 = 2**31 - 1 if partition2 == m else nums2[partition2]
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (n + m) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) * 0.5
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                r = partition1 - 1
            else:
                l = partition1 + 1
