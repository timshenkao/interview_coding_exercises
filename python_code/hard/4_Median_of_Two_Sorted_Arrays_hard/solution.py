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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0: return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else: return arr[len(arr) // 2]

Divide and Conquer
Time: O(logmin(m,n))
Space: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = n1

        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1
            maxLeft1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
            maxLeft2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]
            minRight1 = 2**31 - 1 if partition1 == n1 else nums1[partition1]
            minRight2 = 2**31 - 1 if partition2 == n2 else nums2[partition2]
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r = partition1 - 1
            else:
                l = partition1 + 1