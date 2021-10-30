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

# 876. Middle of the Linked List  https://leetcode.com/problems/middle-of-the-linked-list/
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        # if list is empty, do not do anything
        if not head:
            return head

        # count total number of nodes in the list
        node_count = 0
        pointer = head
        while pointer:
            node_count += 1
            pointer = pointer.next_node

        # skip necessary number of nodes in the list
        middle_count = node_count // 2
        pointer = head
        while middle_count:
            middle_count -= 1
            pointer = pointer.next_node

        return pointer
