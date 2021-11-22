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

from math import inf
from typing import List

# 121. Best Time to Buy and Sell Stock https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution:
    def max_profit_additional_array(self, prices: List[int]) -> int:
        """ Time complexity: O(n). We iterate through prices once.
            Space complexity: O(n). We create additional list of profits.
        """
        # we iterate backwards
        curr_max = prices[-1]
        # generate list of profits
        profits = [0 for _ in prices]
        for i in reversed(range(len(prices))):
            curr_max = max(curr_max, prices[i])
            profits[i] = curr_max - prices[i]

        return max(profits)

    def max_profit(self, prices: List[int]) -> int:
        """ Time complexity: O(n). We iterate through prices once.
            Space complexity: O(1).
        """
        min_price = inf
        max_profit = 0

        for price in prices:
            # check if current price is less than previously seen prices
            if price < min_price:
                min_price = price
            # current price is not smallest seen so far
            # check and update maximum possible profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
