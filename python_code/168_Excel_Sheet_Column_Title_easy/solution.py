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

# 168. Excel Sheet Column Title  https://leetcode.com/problems/excel-sheet-column-title/
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

from time import sleep
class Solution:
    def convert_to_title(self, column_number: int) -> str:
        """ Time complexity: O().
            Space complexity: O().
        """
        # handle 0
        if not column_number:
            return ''

        base = 26
        # ASCII code of A
        upper_a_code = 65
        result = list()
        while column_number:
            # ASCII code of Z is 90
            # but result of modulo is 0
            digit = (column_number + 25) % base
            column_number = (column_number - 1) // base
            result.append(chr(upper_a_code + digit))
        return ''.join([result[i] for i in reversed(range(len(result)))])
