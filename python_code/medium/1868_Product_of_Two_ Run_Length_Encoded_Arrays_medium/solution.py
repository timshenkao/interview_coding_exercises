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

# 1868. Product of Two Run-Length Encoded Arrays
# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/
# Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive
# repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi]
# describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.
# For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]].
# Another way to read this is "three 1's followed by five 2's".
# The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:
#       Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
#       Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
#       Compress prodNums into a run-length encoded array and return it.
# You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2
# respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment
# of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.
# Return the product of encoded1 and encoded2.
# Note: Compression should be done such that the run-length encoded array has the minimum possible length.
# 1 <= encoded1.length, encoded2.length <= 10^5
# encoded1[i].length == 2
# encoded2[j].length == 2
# 1 <= val_i, freq_i <= 10^4 for each encoded1[i].
# 1 <= val_j, freq_j <= 10^4 for each encoded2[j].
# The full arrays that encoded1 and encoded2 represent are the same length.


class Solution:
    def find_rle_array(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """ Time complexity: O(∣encoded1∣+∣encoded2∣)
            Space complexity: O(∣encoded1∣+∣encoded2∣)
        """
        ans = []
        i = 0  # encoded1's index
        j = 0  # encoded2's index

        while i < len(encoded1) and j < len(encoded2):
            mult = encoded1[i][0] * encoded2[j][0]
            min_freq = min(encoded1[i][1], encoded2[j][1])
            if ans and mult == ans[-1][0]:
                ans[-1][1] += min_freq
            else:
                ans.append([mult, min_freq])
            encoded1[i][1] -= min_freq
            encoded2[j][1] -= min_freq
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return ans
