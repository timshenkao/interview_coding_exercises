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
from solution import Solution


def main():
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(solution.max_profit_additional_array(prices))
    print(solution.max_profit(prices))
    print(solution.max_profit_max(prices), '\n')

    prices = [7, 6, 4, 3, 1]
    print(solution.max_profit_additional_array(prices))
    print(solution.max_profit(prices))
    print(solution.max_profit_max(prices), '\n')

    prices = []
    print(solution.max_profit_additional_array(prices))
    print(solution.max_profit(prices))
    print(solution.max_profit_max(prices), '\n')

    prices = [-7, -1, -5, -3, -6, -4]
    print(solution.max_profit_additional_array(prices))
    print(solution.max_profit(prices))
    print(solution.max_profit_max(prices), '\n')


if __name__ == "__main__":
    main()
