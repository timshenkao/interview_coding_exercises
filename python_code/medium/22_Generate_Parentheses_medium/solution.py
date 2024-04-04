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
    def generateParenthesis(self, n: int) -> List[str]:
        bfs = [(0, 0, "")]
        for c in range(n * 2):
            bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <= n] + [(l, r + 1, s + ')') for l, r, s in bfs if l - r]
        return [s for l, r, s in bfs]

Time: O(2^2n)
Space: O(n)


Dynamic Programming
class Solution:
    def generateParenthesis(self, n):
        ans = []

        def dfs(l: int, r: int, s: str) -> None:
            if l == 0 and r == 0:
                ans.append(s)
            if l > 0:
                dfs(l - 1, r, s + '(')
            if l < r:
                dfs(l, r - 1, s + ')')

        dfs(n, n, "")
        return ans