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
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            s = max(A[i].start, B[j].start)
            e = min(A[i].end, B[j].end)
            if s <= e:
                res.append(Interval(s, e))
            if A[i].end < B[j].end:
                i += 1
            elif A[i].end == B[j].end:
                i += 1
                j += 1
            else:
                j += 1
        return res


Time: O(n)
Space: O(n)


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            # lo := the start of the intersection
            # hi := the end of the intersection
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans