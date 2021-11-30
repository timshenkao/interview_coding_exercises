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

    num1 = "11"
    num2 = "123"
    print(solution.add_strings(num1, num2))

    num1 = "456"
    num2 = "77"
    print(solution.add_strings(num1, num2))

    num1 = "0"
    num2 = "0"
    print(solution.add_strings(num1, num2))

    num1 = "1"
    num2 = "9"
    print(solution.add_strings(num1, num2))

    num1 = "1"
    num2 = "19"
    print(solution.add_strings(num1, num2))

    num1 = "6994"
    num2 = "36"
    print(solution.add_strings(num1, num2))


if __name__ == '__main__':
    main()
