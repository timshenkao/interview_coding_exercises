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

import bisect
import itertools
import random


# 528. Random Pick with Weight https://leetcode.com/problems/random-pick-with-weight/description/
# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1]
# (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability
# of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
# 1 <= w.length <= 104
# 1 <= w[i] <= 105
# pickIndex will be called at most 104 times.


class Solution:
    # Explicit Binary Search
    # Time complexity: Constructor: O(n), pickIndex(): O(logn)
    # Space complexity: O(n)
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


class Solution2:
    # Built-in Binary Search
    # Time complexity: Constructor: O(n), pickIndex(): O(logn)
    # Space complexity: O(n)
    def __init__(self, w):
        self.prefix = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix[-1] - 1)
        return bisect.bisect_right(range(len(self.prefix)), target, key=lambda m: self.prefix[m])
