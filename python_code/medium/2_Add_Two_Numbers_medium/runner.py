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

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print_list(solution.add_two_numbers(generate_list(l1), generate_list(l2)))

    l1 = [0]
    l2 = [0]
    print_list(solution.add_two_numbers(generate_list(l1), generate_list(l2)))

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print_list(solution.add_two_numbers(generate_list(l1), generate_list(l2)))


if __name__ == "__main__":
    main()
