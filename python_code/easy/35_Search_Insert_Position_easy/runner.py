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

    nums = [1, 3, 5, 6]
    target = 5
    print(solution.search_insert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(solution.search_insert(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    print(solution.search_insert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    print(solution.search_insert(nums, target))

    nums = [1]
    target = 0
    print(solution.search_insert(nums, target))

    nums = [1, 3]
    target = 0
    print(solution.search_insert(nums, target))


if __name__ == "__main__":
    main()
