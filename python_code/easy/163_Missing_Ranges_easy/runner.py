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

    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(solution.find_missing_ranges(nums, lower, upper))

    nums = []
    lower = 1
    upper = 1
    print(solution.find_missing_ranges(nums, lower, upper))

    nums = []
    lower = -3
    upper = -1
    print(solution.find_missing_ranges(nums, lower, upper))

    nums = [-1]
    lower = -1
    upper = -1
    print(solution.find_missing_ranges(nums, lower, upper))

    nums = [-1]
    lower = -2
    upper = -1
    print(solution.find_missing_ranges(nums, lower, upper))


if __name__ == "__main__":
    main()
