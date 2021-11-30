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

    n = 2
    print(solution.fibonacci_recursion(n))
    print(solution.fibonacci_iteration(n))

    n = 3
    print(solution.fibonacci_recursion(n))
    print(solution.fibonacci_iteration(n))

    n = 20
    print(solution.fibonacci_recursion(n))
    print(solution.fibonacci_iteration(n))

    n = 30
    print(solution.fibonacci_recursion(n))
    print(solution.fibonacci_iteration(n))


if __name__ == '__main__':
    main()
