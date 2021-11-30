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

# 414. Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not
# exist, return the maximum number.


class Solution:
    def third_max(self, nums: List[int]) -> int:
        """ Time complexity: O(N). We iterate through array once.
            Space complexity: O(1). Additional array has constant size.
        """
        maxes = [None, None, None]
        for i in range(len(nums)):
            # if first maximum hasn't been set yet
            if not maxes[0]:
                maxes[0] = nums[i]
            # update first maximum
            elif nums[i] > maxes[0]:
                maxes[0], maxes[1], maxes[2] = nums[i], maxes[0], maxes[1]
            # if equals to the first maximum
            elif nums[i] == maxes[0]:
                continue
            # if second maximum hasn't been set yet
            elif not maxes[1]:
                maxes[1] = nums[i]
            # update second maximum
            elif nums[i] > maxes[1]:
                maxes[1], maxes[2] = nums[i], maxes[1]
            # if equals to the second maximum
            elif nums[i] == maxes[1]:
                continue
            # if third maximum hasn't been set yet
            elif not maxes[2]:
                maxes[2] = nums[i]
            # update third maximum
            elif nums[i] >= maxes[2]:
                maxes[2] = nums[i]

        if maxes[2] is not None:
            return maxes[2]
        else:
            return maxes[0]

    def third_max_set(self, nums: List[int]) -> int:
        """ Time complexity: O(N). We iterate through array once.
            Space complexity: O(1). Additional set has constant size.
            This solution can be updated to find k-th maximum (add parameter k to method and substitute 3 to k)
        """
        maxes = set()
        for num in nums:
            maxes.add(num)
            if len(maxes) > 3:
                maxes.remove(min(maxes))

        if len(maxes) == 3:
            return min(maxes)
        return max(maxes)
