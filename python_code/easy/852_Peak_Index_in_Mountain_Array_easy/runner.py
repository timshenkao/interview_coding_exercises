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

    arr = [0, 1, 0]
    print(solution.peak_index_in_mountain_array(arr))

    arr = [0, 2, 1, 0]
    print(solution.peak_index_in_mountain_array(arr))

    arr = [0, 10, 5, 2]
    print(solution.peak_index_in_mountain_array(arr))

    arr = [3, 4, 5, 1]
    print(solution.peak_index_in_mountain_array(arr))

    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    print(solution.peak_index_in_mountain_array(arr))


if __name__ == "__main__":
    main()
