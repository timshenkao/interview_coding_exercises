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
# 733. Flood Fill https://leetcode.com/problems/flood-fill/
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the
# pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
# of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
# color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n


class Solution:
    def flood_fill(self, image, sr, sc, new_color):
        """ Time complexity: O(n^2), n - width / length of image.
            Space complexity: O(n^2).
        """
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != new_color:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = new_color
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        q.append((x, y))
        return image

    def flood_fill2(self, image, sr, sc, new_color):
        """ Time complexity: O(n^2), n - width / length of image. Recursive DFS
            Space complexity: O(n^2).
        """
        def dfs(i: int, j: int) -> None:
            if i < 0 or i == len(image) or j < 0 or j == len(image[0]):
                return
            if image[i][j] != start_color or (i, j) in seen:
                return

            image[i][j] = new_color
            seen.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        start_color = image[sr][sc]
        seen = set()
        dfs(sr, sc)
        return image
