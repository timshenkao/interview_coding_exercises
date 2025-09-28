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

# 43. Multiply Strings https://leetcode.com/problems/multiply-strings/
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
# represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """ Time complexity: O(m * n). Iterate through each pair of digits in num1 and num2
            Space complexity: O(m + n) auxiliary space for the result array.
        """
        if num1 == "0" or num2 == "0":
            return "0"
        # Initialize result array (max size is len(num1) + len(num2))
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        # Multiply each digit pair and store in result array
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2
                pos1, pos2 = i + j, i + j + 1

                result[pos2] += product
                result[pos1] += result[pos2] // 10
                result[pos2] %= 10

        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        result_str = "".join([chr(digit + ord("0")) for digit in result[i:]])
        return result_str if result_str else "0"
