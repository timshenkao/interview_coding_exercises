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

# 203. Remove Linked List Elements  https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has
# Node.val == val, and return the new head.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        # if there is no nodes in the list
        if not head:
            return head

        # dummy node that points to the beginning of the created list
        sentinel = ListNode()
        prev = sentinel
        curr = head
        while curr:
            # skip nodes with val
            if curr.val == val:
                # check whether still to skip and list is over
                while curr and curr.val == val:
                    curr = curr.next_node

            # "add" next node to the created list
            prev.next_node = curr
            # check whether list is over
            if curr:
                curr = curr.next_node
            prev = prev.next_node
        return sentinel.next_node
