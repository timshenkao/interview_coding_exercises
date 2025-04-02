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
    def pacificAtlantic(self, matrix):
        pac, atl, m, n = set(), set(), len(matrix), len(matrix and matrix[0])
        def explore(i, j, ocean):
            ocean.add((i, j))
            if i > 0 and (i - 1, j) not in ocean and matrix[i - 1][j] >= matrix[i][j]: explore(i - 1, j, ocean)
            if j > 0 and (i, j - 1) not in ocean and matrix[i][j - 1] >= matrix[i][j]: explore(i, j - 1, ocean)
            if i + 1 < m  and (i + 1, j) not in ocean and matrix[i + 1][j] >= matrix[i][j]: explore(i + 1, j, ocean)
            if j + 1 < n  and (i, j +1) not in ocean and matrix[i][j + 1] >= matrix[i][j]: explore(i, j + 1, ocean)
        for i in range(max(m, n)):
            if i < m and (i, 0) not in pac: explore(i, 0, pac)
            if i < n and (0, i) not in pac: explore(0, i, pac)
            if i < n and (m - 1, i) not in atl: explore(m - 1, i, atl)
            if i < m and (i, n - 1) not in atl: explore(i, n - 1, atl)
        return [[x, y] for x, y in pac & atl]

    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        """BFS
         Time complexity: O(m*n).
         Space complexity: O(m*n).
        """
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(heights)
        n = len(heights[0])
        qP = collections.deque()
        qA = collections.deque()
        seenP = [[False] * n for _ in range(m)]
        seenA = [[False] * n for _ in range(m)]

        for i in range(m):
            qP.append((i, 0))
            qA.append((i, n - 1))
            seenP[i][0] = True
            seenA[i][n - 1] = True

        for j in range(n):
            qP.append((0, j))
            qA.append((m - 1, j))
            seenP[0][j] = True
            seenA[m - 1][j] = True

        def bfs(q: deque, seen: List[List[bool]]):
            while q:
                i, j = q.popleft()
                h = heights[i][j]
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if seen[x][y] or heights[x][y] < h:
                        continue
                    q.append((x, y))
                    seen[x][y] = True

        bfs(qP, seenP)
        bfs(qA, seenA)
        return [[i, j] for i in range(m) for j in range(n) if seenP[i][j] and seenA[i][j]]

    def pacificAtlantic3(self, heights: List[List[int]]) -> List[List[int]]:
        """DFS
         Time complexity: O(m*n).
         Space complexity: O(m*n).
        """
        m = len(heights)
        n = len(heights[0])
        seenP = [[False] * n for _ in range(m)]
        seenA = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, h: int, seen: List[List[bool]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            if seen[i][j] or heights[i][j] < h:
                return

            seen[i][j] = True
            dfs(i + 1, j, heights[i][j], seen)
            dfs(i - 1, j, heights[i][j], seen)
            dfs(i, j + 1, heights[i][j], seen)
            dfs(i, j - 1, heights[i][j], seen)

        for i in range(m):
            dfs(i, 0, 0, seenP)
            dfs(i, n - 1, 0, seenA)

        for j in range(n):
            dfs(0, j, 0, seenP)
            dfs(m - 1, j, 0, seenA)

        return [[i, j]
                for i in range(m)
                for j in range(n)
                if seenP[i][j] and seenA[i][j]]
