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
        1: [[1,3],[2,6],[8,10],[15,18]],
        2: [[1,4],[4,5]]
    }
    for _, test in tests.items():
        print("intervals: ", test)

        print("merge ", solution.merge(test))
        print("merge2 ", solution.merge2(test))
        print(" ")


if __name__ == "__main__":
    main()