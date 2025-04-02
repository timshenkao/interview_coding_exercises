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
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1): dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """ Combinations. Dynamic Programming
        Time complexity: O(∣coins∣∣amount∣)
        Space complexity: O(∣amount∣)
        """
        # dp[i] := the minimum number Of coins to make up i
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
