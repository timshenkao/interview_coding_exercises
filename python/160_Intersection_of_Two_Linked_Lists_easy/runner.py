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
from solution import Solution, ListNode
from typing import Optional


def print_list(head: Optional[ListNode]) -> None:
    print()
    while head.next_node:
        print('node: ', head, '; value: ', head.val, '; next node: ', head.next_node)
        head = head.next_node
    print('node: ', head, '; value: ', head.val, '; next node: ', head.next_node)


def print_node(node: Optional[ListNode]) -> None:
    print()
    print('node: ', node, '; value: ', node.val, '; next node: ', node.next_node)


def main():
    solution = Solution()

    ###########################################################
    e0 = ListNode(5, None)
    e1 = ListNode(4, e0)
    e2 = ListNode(8, e1)
    e3 = ListNode(1, e2)
    e4 = ListNode(6, e3)
    head1 = ListNode(5, e4)
    b1 = ListNode(6, e2)
    head2 = ListNode(4, b1)

    print_node(solution.get_intersection_node(head1, head2))


if __name__ == '__main__':
    main()
