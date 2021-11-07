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

# 21. Merge Two Sorted Lists  https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.


class Solution:
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Time complexity: O(n). We iterate through linked list once
            Space complexity: O(1).
        """
        # if one of the lists is empty, return the other one (possibly non-empty).
        if not l1:
            return l2
        if not l2:
            return l1

        # use fast & slow pointers
        first = l1
        second = l2
        # dummy node to have pointer to the beginning of the list
        # in some sense, we built new list and curr is the last node in that list
        # we compare values from both lists and decide which node to connect to
        sentinel = ListNode(0)
        curr = sentinel
        while first and second:
            if first.val <= second.val:
                curr.next_node = first
                first = first.next_node
            else:
                curr.next_node = second
                second = second.next_node
            curr = curr.next_node

        # as lists could be of different length, we join the remaining elements from either of the lists
        curr.next_node = first or second
        return sentinel.next_node
