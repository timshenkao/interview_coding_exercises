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
    def longestConsecutive(self, nums):
        res, items = 0, set(nums)
        for num in items:
            if num - 1 not in items:
                cur = 1
                while num + 1 in items:
                    num, cur = num + 1, cur + 1
                if cur > res: res = cur
        return res

Union Find
Time: O(n)
Space: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        seen = set(nums)

        for num in nums:
            # `num` is the start of a sequence.
            if num - 1 in seen:
                continue
            length = 0
            while num in seen:
                num += 1
                length += 1
            ans = max(ans, length)

        return ans