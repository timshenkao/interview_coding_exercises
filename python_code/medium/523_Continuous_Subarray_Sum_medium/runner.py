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

from python_code.helper.linked_lists import generate_list, print_list
from solution import Solution


def main():
    solution = Solution()

    tests = {
        1: [6, [23,2,4,6,7]],
        2: [6, [23,2,6,4,7]],
        3: [13, [23,2,6,4,7]],
        4: [6, [1,2,12]]
    }
    for _, test in tests.items():
        print("array: ", test[1], " k: ", test[0])
        print("check_subarray_sum ", solution.check_subarray_sum(test[1], test[0]))
        print(" ")


if __name__ == "__main__":
    main()
