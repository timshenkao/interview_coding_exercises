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

# 234. Palindrome Linked List  https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        """ Time complexity: O(N).
            Space complexity: O(1).

            Note that we destroy original list.
        """
        # if list is empty, do not do anything
        if not head:
            return True

        # first, count number of nodes
        node_count = 0
        curr = head
        while curr:
            node_count += 1
            curr = curr.next_node

        # second, iterate to the middle of the list
        # inverse links while iterating
        # this way, we have 2 lists: from middle back to original head and and from middle to the end of the list
        curr = head
        prev = None
        middle = node_count // 2
        while middle:
            temp = curr
            curr = curr.next_node
            temp.next_node = prev
            prev = temp
            middle -= 1

        # if there is odd number of nodes, don't include the middle node and move pointer forward to the end of the list
        if node_count % 2 == 1:
            curr = curr.next_node

        # iterate through both lists and check values
        while curr and prev:
            if curr.val == prev.val:
                curr = curr.next_node
                prev = prev.next_node
            else:
                return False
        return True
