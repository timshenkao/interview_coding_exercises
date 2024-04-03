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
    def missingElement(self, nums: List[int], k: int) -> int:
        cur = nums[0]
        for num in nums[1:]:
            if num - cur - 1 >= k:
                break
            else:
                k -= num - cur - 1
            cur = num
        return cur + k

Binary Search
Time: O(logn)
Space: O(1)