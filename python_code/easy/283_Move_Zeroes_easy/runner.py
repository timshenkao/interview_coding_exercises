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

    nums = [0, 1, 0, 3, 12]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [0, 1, 0, 3, 0, -9, 0, 12]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [0]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [1, 2, 3]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = []
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [0, 0, 0]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [0, 0, 0, 0, 12]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')

    nums = [1, 2, 0, 0, 3]
    print(nums)
    solution.move_zeros(nums)
    print(nums, '\n')


if __name__ == "__main__":
    main()
