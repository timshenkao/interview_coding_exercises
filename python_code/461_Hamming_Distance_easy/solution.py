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

# 461. Hamming Distance  https://leetcode.com/problems/hamming-distance/
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.


class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        """ Time complexity: O(1). Size (number of bits) of integer number is fixed, we have a constant time complexity.
            Space complexity: O(1).
            Interesting example of bit manipulation.
        """
        # xor contains 1s at positions of difference
        xor = x ^ y
        distance = 0
        # until xor becomes 0, use Kernighan's approach
        while xor:
            distance += 1
            # remove the rightmost bit of '1' without shifting
            # (xor - 1) is used as a mask to zero rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance

    def hamming_distance_shift(self, x: int, y: int) -> int:
        """ Time complexity: O(1). Size (number of bits) of integer number is fixed, we have a constant time complexity.
            Space complexity: O(1).
            Interesting example of bit manipulation.
        """
        # xor contains 1s at positions of difference
        xor = x ^ y
        distance = 0
        while xor:
            # check if the rightmost bit is 1
            if xor & 1:
                distance += 1
            # shift xor to the right by 1 bit / remove rightmost bit
            xor = xor >> 1
        return distance

    def hamming_distance_bin(self, x: int, y: int) -> int:
        """ Time complexity: O(1). Size (number of bits) of integer number is fixed, we have a constant time complexity.
            Space complexity: O(1).
            Interesting example of bit manipulation.
        """
        bin_string = bin(x ^ y)
        distance = 0
        for ch in bin_string[2:]:
            distance += int(ch)
        return distance
