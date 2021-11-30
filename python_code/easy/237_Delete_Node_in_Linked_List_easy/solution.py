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

from typing import List, Optional

from python_code.helper.linked_lists import ListNode, generate_list

# 237. Delete Node in a Linked List  https://leetcode.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node in a singly-linked list.
# You will not be given access to the head of the list, instead you will be given access to the node to be deleted
# directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.


class Solution:
    def __init__(self, values: Optional[List[int]] = None):
        if values:
            self.head = generate_list(values)
        else:
            self.head = None

    def delete_node(self, node: ListNode) -> None:
        """ Time complexity: O(1).
            Space complexity: O(1).
        """
        # we "delete" / skip the next node actually
        if node.next_node:
            node.val = node.next_node.val
            node.next_node = node.next_node.next_node
        else:
            node.val = None
            node.next_node = None
