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

# 252. Meeting Rooms https://leetcode.com/problems/meeting-rooms/description/
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all
# meetings.
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6


class Solution:
    def can_attend_meetings(self, intervals):
        """ Time complexity: O(nlogn).
            Space complexity: O(1). The sort() function in Python is in-place
        """
        intervals.sort(key=lambda x: x[1])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
