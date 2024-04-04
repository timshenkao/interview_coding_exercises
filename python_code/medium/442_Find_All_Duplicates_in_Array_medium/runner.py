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

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution.find_duplicates_cycle_sort(nums))
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution.find_duplicates_optimal(nums))

    nums = [1, 1, 2]
    print(solution.find_duplicates_cycle_sort(nums))
    nums = [1, 1, 2]
    print(solution.find_duplicates_optimal(nums))

    nums = [1]
    print(solution.find_duplicates_cycle_sort(nums))
    nums = [1]
    print(solution.find_duplicates_optimal(nums))

    nums = [5, 4, 6, 7, 9, 3, 10, 9, 5, 6]
    print(solution.find_duplicates_cycle_sort(nums))
    nums = [5, 4, 6, 7, 9, 3, 10, 9, 5, 6]
    print(solution.find_duplicates_optimal(nums))


if __name__ == "__main__":
    main()
