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

from python_code.helper.linked_lists import MultiDoubleListNode

# 430. Flatten a Multilevel Doubly Linked List https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an
# additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing
# these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel
# data structure.
# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly
# linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before
# curr.next in the flattened list.
# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
# The number of Nodes will not exceed 1000.
# 1 <= Node.val <= 105


class Solution:
    def _subflatten(self, head: Optional[MultiDoubleListNode]) -> \
            (Optional[MultiDoubleListNode], Optional[MultiDoubleListNode]):
        curr_node = head
        tail = None
        while curr_node:
            if curr_node.child_node:
                temp = curr_node.next_node
                child_head, child_tail = self._subflatten(curr_node.child_node)
                curr_node.next_node = child_head
                child_tail.next_node = temp
                curr_node.child_node = None
                curr_node = temp
            else:
                if not curr_node.next_node:
                    tail = curr_node
                curr_node = curr_node.next_node
        return head, tail

    def flatten(self, head: Optional[MultiDoubleListNode]) -> Optional[MultiDoubleListNode]:
        """ Time complexity: O(N). N - total number of elements
            Space complexity: O(N). In extreme case, nodes are chained with each other only with the child pointers.
            In this case, the recursive calls would pile up, and it would take NNN space in the function call stack.
        """
        if not head:
            return None
        head, _ = self._subflatten(head)
        return head
