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
        1: [1,2,3,4],
        2: [-1,1,0,-3,3]    }
    for _, test in tests.items():
        print("array: ", test)
        print("product_except_self ", solution.product_except_self(test))
        print("product_except_self2 ", solution.product_except_self2(test))
        print("product_except_self_optimal ", solution.product_except_self_optimal(test))
        print(" ")


if __name__ == "__main__":
    main()
