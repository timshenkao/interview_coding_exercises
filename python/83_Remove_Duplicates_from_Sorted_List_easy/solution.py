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

# 83. Remove Duplicates from Sorted List  https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Time complexity: O(n). We iterate through linked list once.
            Space complexity: O(1).
        """
        prev_node = head
        current_node = head

        while current_node and current_node.next_node:
            current_node = current_node.next_node
            if current_node.val != prev_node.val:
                prev_node = prev_node.next_node
            else:
                prev_node.next_node = current_node.next_node
        return head
