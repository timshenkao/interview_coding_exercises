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
# You need to implement the function pickIndex(), which randomly picks an INDEX in the range [0, w.length - 1]
# (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability
# of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
# 1 <= w.length <= 10^4
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10^4 times.


class Solution:
    # Explicit Binary Search
    # Time complexity: Constructor: O(n), pickIndex(): O(logn)
    # Space complexity: O(n)
    def __init__(self, w):
        self.ranges_cum_sum = []
        cum_sum = 0
        # fill in array with prefix / cumulative sums
        for weight in w:
            self.ranges_cum_sum.append([cum_sum, cum_sum + weight])
            cum_sum += weight
        # array of positive integers, i.e. min integer / cumulative sum is 1
        self.min = 1
        self.max = cum_sum

    def pickIndex(self):
        # generate random integer that corresponds to some cumulative sum
        num = random.randint(self.min, self.max)
        l = 0
        r = len(self.ranges_cum_sum) - 1
        # binary search: find element that corresponds the generated random cumulative sum
        while l <= r:
            mid = (l + r) // 2
            if self.ranges_cum_sum[mid][1] < num:
                l = mid + 1
            elif num <= self.ranges_cum_sum[mid][0]:
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
