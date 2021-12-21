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
from python_code.helper.linked_lists import generate_list_cycle, print_node


def main():
    solution = Solution()

    values = [3, 2, 0, -4]
    pos = 1
    head = generate_list_cycle(values, pos)
    print_node(solution.detect_cycle(head))

    values = [1, 2]
    pos = 0
    head = generate_list_cycle(values, pos)
    print_node(solution.detect_cycle(head))

    values = [1]
    pos = -1
    head = generate_list_cycle(values, pos)
    print_node(solution.detect_cycle(head))


if __name__ == '__main__':
    main()
