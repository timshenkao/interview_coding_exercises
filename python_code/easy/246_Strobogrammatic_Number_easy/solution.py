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

# 246. Strobogrammatic Number  https://leetcode.com/problems/strobogrammatic-number/
# Given a string num which represents an integer, return true if num is a strobogrammatic number.
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).


class Solution:
    def is_strobogrammatic(self, num: str) -> bool:
        """Time complexity: O(n). We iterate through string once.
            Space complexity: O(1). We create additional dict of fixed size.
        """
        strob_digit = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left = 0
        right = len(num) - 1

        while left <= right:
            if (not num[left] in strob_digit) or (not num[right] in strob_digit):
                return False
            elif num[right] != strob_digit[num[left]]:
                return False
            left += 1
            right -= 1
        return True
