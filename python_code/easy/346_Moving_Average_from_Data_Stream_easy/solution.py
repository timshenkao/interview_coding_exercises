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

# 346. Moving Average from Data Stream https://leetcode.com/problems/moving-average-from-data-stream/
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
#     Constructor initializes the object with the size of the window size.
#     next() returns the moving average of the last size values of the stream.


class MovingAverage:
    """ Time complexity: O(1) if operations of the oldest element  removal or new element addition take O(1).
                         O(n) otherwise.
        Space complexity: O(n). We create additional array / list to keep values
    """
    def __init__(self, size: int):
        self.windows_size = size
        self.current_elems = []
        self.current_sum = 0

    def next(self, val: int) -> float:
        # if there is values less than window size, than just add new value to the list and calculate average
        if len(self.current_elems) < self.windows_size:
            self.current_elems.append(val)
            self.current_sum += val
            return self.current_sum / len(self.current_elems)
        # if there is values more or equal than window size, than remove the oldest value to the list
        # and calculate average
        else:
            oldest_value = self.current_elems.pop(0)
            self.current_elems.append(val)
            self.current_sum += (val - oldest_value)
            return self.current_sum / self.windows_size
