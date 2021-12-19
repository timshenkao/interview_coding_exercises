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

from python_code.helper.linked_lists import ListNode, print_list

# 707. Design Linked List  https://leetcode.com/problems/design-linked-list/
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and
# next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the
# linked list. Assume all nodes in the linked list are 0-indexed.
# Implement the MyLinkedList class:
#     MyLinkedList() Initializes the MyLinkedList object.
#     int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
#     void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
#                             the new node will be the first node of the linked list.
#     void addAtTail(int val) Append a node of value val as the last element of the linked list.
#     void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index
#                                         equals the length of the linked list, the node will be appended to the end of
#                                         the linked list. If index is greater than the length, the node will not be
#                                         inserted.
#     void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
# 0 <= index, val <= 1000


class MyLinkedList:

    def _iterate_till_index(self, index: int) -> ListNode:
        i = 0
        curr_node = self.head
        # index not included
        while i < index and curr_node:
            i += 1
            curr_node = curr_node.next_node
        return curr_node

    def __init__(self):
        self.head = ListNode()
        # when empty linked list is initialized, both head and tail point to the same dummy node
        self.tail = self.head
        self.number_of_nodes = 0

    def get(self, index: int) -> int:
        # there is less nodes than 'index' value
        # linked list is 0-indexed by condition
        if index > self.number_of_nodes - 1:
            return -1
        curr_node = self._iterate_till_index(index)
        if curr_node:
            return curr_node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        # when linked list is actually empty
        if self.number_of_nodes == 0:
            curr_node = ListNode(val)
            self.tail = curr_node
        else:
            curr_node = ListNode(val, self.head)
        self.head = curr_node
        self.number_of_nodes += 1

    def addAtTail(self, val: int) -> None:
        curr_node = ListNode(val)
        # when linked list is actually empty
        if self.number_of_nodes == 0:
            self.head = curr_node
        else:
            self.tail.next_node = curr_node
        self.tail = curr_node
        self.number_of_nodes += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # there is less nodes than 'index' value
        if index > self.number_of_nodes:
            return
        if index == self.number_of_nodes:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr_node = self._iterate_till_index(index - 1)
            temp_node = ListNode(val, curr_node.next_node)
            curr_node.next_node = temp_node
            self.number_of_nodes += 1

    def deleteAtIndex(self, index: int) -> None:
        # linked list is 0-indexed by condition
        if index > self.number_of_nodes - 1:
            return
        # delete head
        elif index == 0:
            temp_node = self.head
            if self.number_of_nodes == 1:
                dummy_node = ListNode()
                self.head = self.tail = dummy_node
            else:
                self.head = self.head.next_node
            del temp_node
        # delete tail or internal node
        else:
            curr_node = self._iterate_till_index(index - 1)
            if curr_node.next_node:
                temp_node = curr_node.next_node
                curr_node.next_node = curr_node.next_node.next_node
                if self.tail == temp_node:
                    self.tail = curr_node
                del temp_node
        self.number_of_nodes -= 1

    def print(self):
        print()
        print(self.__dict__)
        print_list(self.head)
