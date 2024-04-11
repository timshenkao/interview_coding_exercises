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

# 17. Letter Combinations of a Phone Number https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution:
    def letter_combinations(self, digits):
        """ Time complexity: O().
            Space complexity: O().
        """
        dic = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [""]
        for dig in digits:
            tmp = []
            for y in res:
                for x in dic[dig]:
                    tmp.append(y + x)
            res = tmp
        return res if any(res) else []

    def letter_combinations2(self, digits):
        """ Time complexity: O(n4^n).
            Space complexity: O(n4^n).
        """
        def dfs(i: int, path):
            if i == len(digits):
                ans.append("".join(path))
                return
            for letter in digit_to_letters[ord(digits[i]) - ord('0')]:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()

        if not digits:
            return []
        digit_to_letters = ["", "", 'abc', 'def', 'ghi',
                            'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        dfs(0, [])
        return ans

    def letter_combinations3(self, digits):
        """ Time complexity: O(n4^n).
            Space complexity: O(n4^n).
        """
        if not digits:
            return []
        ans = [""]
        digit_to_letters = ["", "", 'abc', 'def', 'ghi',
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for d in digits:
            temp = []
            for s in ans:
                for c in digit_to_letters[ord(d) - ord('0')]:
                    temp.append(s + c)
            ans = temp
        return ans
