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


# 739. Daily Temperatures https://leetcode.com/problems/daily-temperatures/
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that
# answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 1 <= temperatures.length <= 10 ^ 5
# 30 <= temperatures[i] <= 100


class Solution:
    def daily_temperatures_brute(self, temperatures: List[int]) -> List[int]:
        """ Time complexity: O(n ^ 2). Nested loop.
            Space complexity: O(n). We create output array.
        """
        # create output array
        result = [0] * len(temperatures)
        first_pointer = 0
        # don't include last element as there is no future elements for it
        while first_pointer < len(temperatures) - 1:
            second_pointer = first_pointer + 1
            # iterate until higher temperature found
            while second_pointer < len(temperatures) - 1 \
                    and temperatures[first_pointer] >= temperatures[second_pointer]:
                second_pointer += 1
            # edge case when end of array is reached but no higher temperature found
            if second_pointer == len(temperatures) - 1 and temperatures[first_pointer] >= temperatures[second_pointer]:
                result[first_pointer] = 0
            else:
                result[first_pointer] = second_pointer - first_pointer
            first_pointer += 1
        return result

    def daily_temperatures_monotonic_stack(self, temperatures: List[int]) -> List[int]:
        """ Time complexity: O(N). We iterate once through array. In the worst case, every element will be pushed and
                             popped once.
            Space complexity: O(n). We create output array and use stack.
        """
        # create output array
        result = [0] * len(temperatures)
        monotonic_stack = list()  # keep track of indices
        for i in range(len(temperatures)):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while monotonic_stack and temperatures[monotonic_stack[-1]] < temperatures[i]:
                last_index = monotonic_stack.pop()
                result[last_index] = i - last_index
            monotonic_stack.append(i)
        return result

    def daily_temperatures_no_stack(self, temperatures: List[int]) -> List[int]:
        """ Time complexity: O(N). We iterate once through array.
            Space complexity: O(n). We create output array.
        """
        # create output array
        result = [0] * len(temperatures)
        highest_temperature = 0  # by definition 30 <= temperatures[i] <= 100
        i = len(temperatures) - 1
        # iterate backwards
        while i >= 0:
            # update highest temperature
            # we don't need the very temperature; we skip the day when we see the highest temperature, i.e.
            # there is no higher temperature and result is 0 for this day
            if temperatures[i] >= highest_temperature:
                highest_temperature = temperatures[i]
                i -= 1
                continue
            # it's not the highest temperature; there is higher temperature in future
            skip_days = 1
            # how does this loop affect TC? O(N^2) ???
            while temperatures[i + skip_days] <= temperatures[i]:
                skip_days += result[i + skip_days]
            result[i] = skip_days
            i -= 1
        return result
