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
        1: [1, 1, 2, [[1,1,1],[1,1,0],[1,0,1]]],
        2: [0,0,0,[[0,0,0],[0,0,0]]]
    }
    for _, test in tests.items():
        print("sr: ", test[0])
        print("sc: ", test[1])
        print("color: ", test[2])
        print("image: ", test[3])
        print("flood_fill ", solution.flood_fill(test[3], test[0], test[1], test[2]))
        print("flood_fill2 ", solution.flood_fill2(test[3], test[0], test[1], test[2]))
        print(" ")


if __name__ == "__main__":
    main()
