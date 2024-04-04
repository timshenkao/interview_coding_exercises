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
    def letterCombinations(self, digits):
        dic, res = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, [""]
        for dig in digits:
            tmp = []
            for y in res:
                for x in dic[dig]: tmp.append(y + x)
            res = tmp
        return res if any(res) else []


Approach 1: DFS
Time: O(n4^n)
Space: O(4^n)



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToLetters = ["", "", 'abc', 'def', 'ghi',
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []

        def dfs(i: int, path: List[chr]) -> None:
            if i == len(digits):
                ans.append("".join(path))
                return

            for letter in digitToLetters[ord(digits[i]) - ord('0')]:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return ans

Approach 2: Iterative
Time: O(n4^n)
Space: O(4^n)



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = [""]
        digitToLetters = ["", "", 'abc', 'def', 'ghi',
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for d in digits:
            temp = []
            for s in ans:
                for c in digitToLetters[ord(d) - ord('0')]:
                    temp.append(s + c)
            ans = temp

        return ans