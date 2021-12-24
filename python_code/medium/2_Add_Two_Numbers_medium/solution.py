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

from typing import Optional

from python_code.helper.linked_lists import ListNode

# 2. Add Two Numbers  https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and
# return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


class Solution:
    def _check_sum_advance_output(self, summ: int, transfer: int, output_curr_node: ListNode,
                                  output_prev_node: Optional[ListNode]) -> tuple:
        # check and correct for overflow
        if summ > 9:
            summ -= 10
            transfer = 1
        else:
            transfer = 0
        # fill in current node in output list and create new node
        output_curr_node.val = summ
        output_curr_node.next_node = ListNode()
        output_prev_node = output_curr_node
        output_curr_node = output_curr_node.next_node
        return transfer, output_curr_node, output_prev_node

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Time complexity: O(N). We iterate through linked lists. N = max(length og l1, length of l2)
            Space complexity: O(N). We create output linked list.
        """
        # pointers within 2 lists
        curr_node_l1 = l1
        curr_node_l2 = l2

        # output list's head
        output_head = ListNode()
        output_curr_node = output_head
        output_prev_node = None

        transfer = 0

        while curr_node_l1 and curr_node_l2:
            # sum of current nodes and transfer
            summ = curr_node_l1.val + curr_node_l2.val + transfer
            transfer, output_curr_node, output_prev_node = \
                self._check_sum_advance_output(summ, transfer, output_curr_node, output_prev_node)

            curr_node_l1 = curr_node_l1.next_node
            curr_node_l2 = curr_node_l2.next_node

        # there may be some elements either in list 1 or list 2
        # if there are still elements in list 2, use pointer from the first list
        if curr_node_l2:
            curr_node_l1 = curr_node_l2

        while curr_node_l1:
            # sum of current nodes and transfer
            summ = curr_node_l1.val + transfer
            transfer, output_curr_node, output_prev_node = \
                self._check_sum_advance_output(summ, transfer, output_curr_node, output_prev_node)
            curr_node_l1 = curr_node_l1.next_node

        if transfer:
            output_curr_node.val = 1
        else:
            output_prev_node.next_node = None
            del output_curr_node

        return output_head
