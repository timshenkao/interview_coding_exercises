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

    def __init__(self, w):
        self.ranges, sm = [], 0
        for weight in w:
            self.ranges.append([sm, sm + weight])
            sm += weight
        self.mn, self.mx = 1, sm
    def pickIndex(self):
        num, l, r = random.randint(self.mn, self.mx), 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.ranges[mid][1] < num:
                l = mid + 1
            elif num <= self.ranges[mid][0]:
                r = mid - 1
            else:
                return mid

Approach 1: Binary Search
Time: Constructor: O(n), pickIndex(): O(logn)
Space: O(n)


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix[-1] - 1)
        return bisect.bisect_right(range(len(self.prefix)), target,
                                   key=lambda m: self.prefix[m])

Approach 2: Built-in
Time: Constructor: O(n), pickIndex(): O(logn)
Space: undefined


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, random.random() * self.prefix[-1])

