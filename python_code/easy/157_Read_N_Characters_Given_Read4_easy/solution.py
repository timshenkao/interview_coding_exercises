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

# 157. Read N Characters Given Read4  https://leetcode.com/problems/read-n-characters-given-read4/
# Given a file and assume that you can only read the file using a given method read4, implement a method to read n
# characters.
# Method read4:
#       The API read4 reads four consecutive characters from file, then writes those characters into the buffer array
#       buf4.
# The return value is the number of actual characters read.
# Note that read4() has its own file pointer, much like FILE *fp in C.
# Definition of read4:
#     Parameter:  char[] buf4
#     Returns:    int
# buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

# Note:
# Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
# The read function will only be called once for each test case.
# You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
# 1 <= file.length <= 500
# file consist of English letters and digits.
# 1 <= n <= 1000


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        """ Time complexity: O(N). We read and iterate through all characters
            Space complexity: O(1).
        """
        read_symbols_total = 0
        read_symbols = 4
        buf4 = [""] * 4

        while read_symbols_total < n and read_symbols == 4:
            read_symbols = read4(buf4)

            for i in range(read_symbols):
                if read_symbols_total == n:
                    return read_symbols_total
                buf[read_symbols_total] = buf4[i]
                read_symbols_total += 1

        return read_symbols_total
