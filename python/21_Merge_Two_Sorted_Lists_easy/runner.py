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


def main():
    solution = Solution()

    ###########################################################
    e1 = ListNode(4, None)
    e2 = ListNode(2, e1)
    l1 = ListNode(1, e2)

    b1 = ListNode(4, None)
    b2 = ListNode(3, b1)
    l2 = ListNode(1, b2)

    head = solution.merge_two_lists(l1, l2)
    print_list(head)

    ###########################################################
    l1 = ListNode(2, None)

    l2 = ListNode(1, None)

    head = solution.merge_two_lists(l1, l2)
    print_list(head)


if __name__ == '__main__':
    main()
