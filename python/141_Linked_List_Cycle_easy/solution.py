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

# 141. Linked List Cycle  https://leetcode.com/problems/linked-list-cycle/
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
# is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """ Time complexity: O(n). We iterate through linked list once
            Space complexity: O(1).
        """
        # use fast & slow pointers
        fast = head
        slow = head
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node
            fast = fast.next_node
            # if there is cycle in the list, then slow and fast will point to the same node eventually.
            if slow == fast:
                return True
        return False
