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

    # ###########################################################
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.search_iteration(nums, target))

    # ###########################################################
    nums = [-10, -2, -1, 0, 3, 5, 9, 12, 13, 15, 20, 22, 24, 32]
    target = 32
    print(solution.search_iteration(nums, target))

    ###########################################################
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(solution.search_iteration(nums, target))


if __name__ == '__main__':
    main()
