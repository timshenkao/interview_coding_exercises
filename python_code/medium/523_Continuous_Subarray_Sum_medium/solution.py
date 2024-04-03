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
    def checkSubarraySum(self, nums, k):
        if not k: return any(nums[i] == nums[i - 1] == 0 for i in range(1, len(nums)))
        mods, sm = set(), 0
        for i, num in enumerate(nums):
            sm = (sm + num) % k
            if (sm in mods and num or (i and not nums[i - 1])) or (not sm and i): return True
            mods |= {sm}
        return False

Time: O(n)
Space: O(n)



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        prefixToIndex = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            if k != 0:
                prefix %= k
            if prefix in prefixToIndex:
                if i - prefixToIndex[prefix] > 1:
                    return True
            else:
                # Set a new key if it's absent because the previous index is better.
                prefixToIndex[prefix] = i

        return False