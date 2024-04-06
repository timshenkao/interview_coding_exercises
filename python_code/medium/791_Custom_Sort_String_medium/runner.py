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

    tests = {
        1: ["cba", "abcd"],
        2: ["bcafg", "abcd"]
    }
    for _, test in tests.items():
        print("order: ", test[0], "s: ", test[1])
        print("custom_sort_string ", solution.custom_sort_string(test[0], test[1]))
        print("custom_sort_string_unoptimal ", solution.custom_sort_string_unoptimal(test[0], test[1]))
        print(" ")


if __name__ == "__main__":
    main()
