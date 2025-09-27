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

# 2622. Cache With Time Limit https://leetcode.com/problems/cache-with-time-limit/
# Write a class that allows getting and setting key-value pairs, however a time until expiration is associated with
# each key.
# The class has three public methods:
#    set(key, value, duration): accepts an integer key, an integer value, and a duration in milliseconds. Once the
#        duration has elapsed, the key should be inaccessible. The method should return true if the same un-expired key
#        already exists and false otherwise. Both the value and duration should be overwritten if the key already exists
#    get(key): if an un-expired key exists, it should return the associated value. Otherwise it should return -1.
#    count(): returns the count of un-expired keys.
# 0 <= key, value <= 10^9
# 0 <= duration <= 1000
# 1 <= actions.length <= 100
# actions.length === values.length
# actions.length === timeDelays.length
# 0 <= timeDelays[i] <= 1450
# actions[i] is one of "TimeLimitedCache", "set", "get" and "count"
# First action is always "TimeLimitedCache" and must be executed immediately, with a 0-millisecond delay


class Solution:
    def set (self, key, value, duration):
        pass

    def get(self, key):
        pass

    def count(self):
        pass
