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

    nums = [1, 2, 3, 1]
    k = 3
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 2, 3, 4]
    k = 1
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    k = 2
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    k = 0
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 2, 3, 4]
    k = 5
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 2, 3, 1]
    k = 5
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = []
    k = 0
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1]
    k = 0
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, -1]
    k = 1
    print(solution.contains_nearby_duplicate_optimized(nums, k))

    nums = [1, 1]
    k = 0
    print(solution.contains_nearby_duplicate_optimized(nums, k))


if __name__ == "__main__":
    main()
