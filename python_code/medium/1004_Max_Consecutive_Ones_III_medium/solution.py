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
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros, res = [-1] + [i for i, c in enumerate(A) if not c] + [len(A)], 0
        for j in range(K + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - K - 1] - 1)
        return res or K and len(A)


class Solution:


Time: O(n)
Space: O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0

        l = 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans