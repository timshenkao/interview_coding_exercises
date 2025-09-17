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

# 11. Container With Most Water https://leetcode.com/problems/container-with-most-water/description/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            water_capacity = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water_capacity)
            # we are decreasing width each iteration
            # Moving the shorter line might increase the height, potentially increasing the area, while moving the
            # taller line cannot increase the area (since the height is limited by the shorter line).
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
