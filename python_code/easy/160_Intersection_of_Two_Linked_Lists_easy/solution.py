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

# 160. Intersection of Two Linked Lists  https://leetcode.com/problems/intersection-of-two-linked-lists/
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.


class Solution:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        # if list is empty, do not do anything
        if not headA or not headB:
            return None

        list_a_count = 0
        list_b_count = 0

        curr_a = headA
        while curr_a:
            curr_a = curr_a.next_node
            list_a_count += 1

        curr_b = headB
        while curr_b:
            curr_b = curr_b.next_node
            list_b_count += 1

        nodes_to_wait_a = max(list_a_count, list_b_count) - list_a_count
        nodes_to_wait_b = max(list_a_count, list_b_count) - list_b_count

        curr_a = headA
        curr_b = headB
        while curr_a and curr_b:
            if nodes_to_wait_a:
                nodes_to_wait_a -= 1
                curr_b = curr_b.next_node
            elif nodes_to_wait_b:
                nodes_to_wait_b -= 1
                curr_a = curr_a.next_node
            elif curr_a == curr_b:
                return curr_a
            else:
                curr_a = curr_a.next_node
                curr_b = curr_b.next_node

        return None
