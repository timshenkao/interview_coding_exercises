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


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next_node = next_node


class MultiDoubleListNode:
    # Definition for multilevel doubly-linked list.
    def __init__(self, val: int = 0, next_node=None, prev_node=None, child_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
        self.child_node = child_node


def generate_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    temp = head = None
    # creating nodes in reverse order
    for i in reversed(range(len(values))):
        head = ListNode(values[i], temp)
        temp = head
    return head


def generate_list_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None
    head = generate_list(values)
    if pos >= 0:
        # get pointer to an internal node
        i = 0
        curr_node = head
        while i < pos:
            i += 1
            curr_node = curr_node.next_node
        # get pointer to the tail node
        tail = curr_node
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = curr_node
    return head


def generate_multi_double_list(values: List[int]) -> Optional[MultiDoubleListNode]:
    if not values:
        return None

    prev = temp = head = None
    i = 0
    while i <= len(values) - 1:
        if values[i] is not None:
            temp = MultiDoubleListNode(values[i], prev_node=prev)
            if prev:
                prev.next_node = temp
            prev = temp
            if i == 0:
                head = temp
            i += 1
        else:
            none_count = -1
            while i <= len(values) - 1 and values[i] is None:
                none_count += 1
                i += 1

            child_node = generate_multi_double_list(values[i:])
            prev = head
            while none_count:
                prev = prev.next_node
                none_count -= 1
            prev.child_node = child_node
            break
    return head


def locate_node(head: ListNode, value: int) -> Optional[ListNode]:
    """ Given the head of a singly-linked list and value, return ListNode that contains the value.
    """
    temp = head
    while temp:
        if temp.val == value:
            return temp
        temp = temp.next_node
    return None


# PRINT FUNCTIONS
def print_list(head: Optional[ListNode]) -> None:
    print()
    i = 0
    if head:
        visited_nodes = set()
        while head.next_node:
            if head not in visited_nodes:
                print("node ", i, ": ", head, "; value: ", head.val, "; next node: ", head.next_node)
                visited_nodes.add(head)
                head = head.next_node
                i += 1
            else:
                break
        if not head.next_node:
            print("node ", i, ": ", head, "; value: ", head.val, "; next node: ", head.next_node)
    else:
        print("node 0: ", head, "; value: ", None, "; next node: ", None)


def print_node(node: Optional[ListNode]) -> None:
    print()
    if node:
        print("node: ", node, "; value: ", node.val, "; next node: ", node.next_node)
    else:
        print("node: ", node, "; value: ", None, "; next node: ", None)


def print_multi_double_list(head: Optional[MultiDoubleListNode]) -> None:
    print()
    i = 0
    children = list()
    if head:
        while head.next_node:
            print("node ", i, ": ", head, "; value: ", head.val, "; next node: ", head.next_node,
                  "; previous node: ", head.prev_node, "; child node: ", head.child_node)
            head = head.next_node
            i += 1
            # if node has a child, add it to list of children
            if head.child_node:
                children.append(head.child_node)
        print("node ", i, ": ", head, "; value: ", head.val, "; next node: ", head.next_node,
              "; previous node: ", head.prev_node, "; child node: ", head.child_node)
        # print children lists
        while children:
            print_multi_double_list(children.pop(0))
    else:
        print("node 0: ", head, "; value: ", None, "; next node: ", None, "; previous node: ", None,
              "; child node: ", None)
