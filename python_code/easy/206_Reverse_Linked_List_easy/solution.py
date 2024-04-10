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

# 206. Reverse Linked List  https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        # if list is empty, do not do anything
        if not head:
            return head

        curr = head
        prev = None
        # iterate through the list and invert pointers
        while curr:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        return prev
