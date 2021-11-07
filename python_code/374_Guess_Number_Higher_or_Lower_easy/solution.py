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


# 374. Guess Number Higher or Lower https://leetcode.com/problems/guess-number-higher-or-lower/
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns 3 possible results:
#     -1: The number I picked is lower than your guess (i.e. pick < num).
#     1: The number I picked is higher than your guess (i.e. pick > num).
#     0: The number I picked is equal to your guess (i.e. pick == num).
# Return the number that I picked.


class Solution:
    def guess_number(self, n: int) -> int:
        """ Time complexity: O(log N).
            Space complexity: O(1).
        """
        # use modification of binary search
        # enumeration from 1 to n
        low = 1
        high = n
        while low < high:
            middle = low + (high - low) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) < 0:
                high = middle - 1
            else:
                low = middle + 1
        return low
