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

    s = "III"
    print(s, " --> ", solution.roman_to_integer_brute(s))
    print(s, " --> ", solution.roman_to_integer_optimal(s))

    s = "IV"
    print(s, " --> ", solution.roman_to_integer_brute(s))
    print(s, " --> ", solution.roman_to_integer_optimal(s))

    s = "IX"
    print(s, " --> ", solution.roman_to_integer_brute(s))
    print(s, " --> ", solution.roman_to_integer_optimal(s))

    s = "LVIII"
    print(s, " --> ", solution.roman_to_integer_brute(s))
    print(s, " --> ", solution.roman_to_integer_optimal(s))

    s = "MCMXCIV"
    print(s, " --> ", solution.roman_to_integer_brute(s))
    print(s, " --> ", solution.roman_to_integer_optimal(s))


if __name__ == "__main__":
    main()
