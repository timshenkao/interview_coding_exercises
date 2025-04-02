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

import collections


class Solution:
    def numIslands(self, grid):
        res, n, m = 0, len(grid), len(grid[0]) if grid else 0
        def explore(i, j):
            grid[i][j] = "-1"
            if i > 0 and grid[i - 1][j] == "1": explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1": explore(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1": explore(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1": explore(i, j + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1": explore(i, j); res += 1
        return res

    def numIslands2(self, grid):
            """ BFS
            Time complexity: O(m*n)
            Space complexity: O(min(m, n))
            """
            dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            m = len(grid)
            n = len(grid[0])

            def bfs(r, c):
                q = collections.deque([(r, c)])
                grid[r][c] = '2'  # Mark '2' as visited.
                while q:
                    i, j = q.popleft()
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if x < 0 or x == m or y < 0 or y == n:
                            continue
                        if grid[x][y] != '1':
                            continue
                        q.append((x, y))
                        grid[x][y] = '2'  # Mark '2' as visited.

            ans = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        bfs(i, j)
                        ans += 1

            return ans

    def numIslands3(self, grid):
        """ DFS
        Time complexity: O(m*n)
        Space complexity: O(m *n)
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            if grid[i][j] != '1':
                return

            grid[i][j] = '2'  # Mark '2' as visited.
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        return ans
