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

# 56. Merge Intervals  https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
# of the non-overlapping intervals that cover all the intervals in the input.
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4


class Solution:
    def merge(self, intervals):
        """ Time complexity: O(nlogn).
            Space complexity: O(n).
        """
        res = []
        # TC: O(nlogn) SC: O(1)
        intervals.sort(key = lambda x: x[1])
        for intr in intervals:
            if not res:
                res.append([intr[0], intr[1]])
            else:
                s = intr[0]
                while res and res[-1][1] >= intr[0]:
                    s = min(s, res.pop()[0])
                res.append([s, intr[1]])
        return res

    def merge2(self, intervals):
        """ Time complexity: O(nlogn).
            Space complexity: O(n).
        """
        ans = []
        # TC: O(nlogn) SC: O(n)
        for interval in sorted(intervals):
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
