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

    tests = {
        1: [9, [2, 7, 11, 15]],
        2: [6, [3, 2, 4]],
        3: [6, [3, 3]],
        4: [-8, [-1, -2, -3, -4, -5]],
        5: [-8, [-1, -2, -3, -10, -9]],
        6: [6, [4, 1]],
             }
    for _, test in tests.items():
        print("array: ", test[1], "target: ", test[0])
        print("brute force ", solution.two_sum_brute(test[1], test[0]))
        print("sorting ", solution.two_sum_sorting(test[1], test[0]))
        print("optimal ", solution.two_sum_optimal(test[1], test[0]))
        print(" ")


if __name__ == "__main__":
    main()
