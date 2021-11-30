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
from python_code.helper.linked_lists import print_list, locate_node, print_node
from solution import Solution


def main():
    head = [4, 5, 1, 9]
    node = 5
    solution = Solution(head)
    node_to_delete = locate_node(solution.head, node)
    solution.delete_node(node_to_delete)
    print_list(solution.head)

    head = [4, 5, 1, 9]
    node = 1
    solution = Solution(head)
    node_to_delete = locate_node(solution.head, node)
    solution.delete_node(node_to_delete)
    print_list(solution.head)

    head = [0, 1]
    node = 0
    solution = Solution(head)
    node_to_delete = locate_node(solution.head, node)
    solution.delete_node(node_to_delete)
    print_list(solution.head)

    head = [-3, 5, -99]
    node = 5
    solution = Solution(head)
    node_to_delete = locate_node(solution.head, node)
    solution.delete_node(node_to_delete)
    print_list(solution.head)


if __name__ == '__main__':
    main()
