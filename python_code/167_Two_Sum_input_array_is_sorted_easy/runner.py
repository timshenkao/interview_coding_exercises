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

    numbers = [2, 7, 11, 15]
    target = 9
    print('arr: ', numbers, ' target: ', target)
    print(solution.two_sum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
    print('arr: ', numbers, ' target: ', target)
    print(solution.two_sum(numbers, target))

    numbers = [-1, 0]
    target = -1
    print('arr: ', numbers, ' target: ', target)
    print(solution.two_sum(numbers, target))

    numbers = [5, 25, 75]
    target = 100
    print('arr: ', numbers, ' target: ', target)
    print(solution.two_sum(numbers, target))


if __name__ == '__main__':
    main()
