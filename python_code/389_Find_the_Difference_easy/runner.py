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

    s = "abcd"
    t = "abcde"
    print(solution.find_the_difference(s, t))
    print(solution.find_the_difference_bit_manipulation(s, t))

    s = ""
    t = "y"
    print(solution.find_the_difference(s, t))
    print(solution.find_the_difference_bit_manipulation(s, t))

    s = "a"
    t = "aa"
    print(solution.find_the_difference(s, t))
    print(solution.find_the_difference_bit_manipulation(s, t))

    s = "ae"
    t = "aea"
    print(solution.find_the_difference(s, t))
    print(solution.find_the_difference_bit_manipulation(s, t))


if __name__ == '__main__':
    main()
