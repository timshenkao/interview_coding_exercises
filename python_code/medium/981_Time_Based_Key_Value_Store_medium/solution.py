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
import collections

# 981. Time Based Key-Value Store https://leetcode.com/problems/time-based-key-value-store/description/
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
#       TimeMap() Initializes the object of the data structure.
#       void set(String key, String value, int timestamp) Stores the key key with the value value at the given time
#       timestamp.
#       String get(String key, int timestamp) Returns a value such that set was called previously, with
#       timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest
#       timestamp_prev. If there are no values, it returns "".
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.


class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""


class TimeMap2:
    """ Time complexity: Constructor: O(1), set(): O(1), get(): O(log n)
        Space complexity: O(n)
        where n is number keys added
    """
    def __init__(self):
        self.values = collections.defaultdict(list)
        self.timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        i = self.binary_search(self.timestamps[key], timestamp)
        return self.values[key][i] if i >= 0 else ""

    def binary_search(self, timestamps, timestamp):
        if len(timestamps) == 0:
            return -1
        l, r = 0, len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid] == timestamp:
                return mid
            if timestamps[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        mid = (l + r) // 2
        if timestamps[mid] <= timestamp:
            return mid
        else:
            return -1
