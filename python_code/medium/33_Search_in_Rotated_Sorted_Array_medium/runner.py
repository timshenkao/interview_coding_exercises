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
        1: [0, [4,5,6,7,0,1,2]],
        2: [3, [4,5,6,7,0,1,2]],
        3: [0, [1]]
    }
    for _, test in tests.items():
        print("array: ", test[1])
        print("target: ", test[0])
        print("search ", solution.search2(test[1], test[0]))
        print("search2 ", solution.search2(test[1], test[0]))
        print(" ")


if __name__ == "__main__":
    main()
