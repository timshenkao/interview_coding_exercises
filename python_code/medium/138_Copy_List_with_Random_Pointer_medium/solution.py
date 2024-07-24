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

import collections

# 138. Copy List with Random Pointer https://leetcode.com/problems/copy-list-with-random-pointer/description/
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any
# node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
# its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
# point to new nodes in the copied list such that the pointers in the original list and copied list represent the same
# list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two
# nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
# [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not
# point to any node.
# Your code will only be given the head of the original linked list.
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList_iterative(self, head: "Node") -> "Node":
        """ Time complexity: O(n)
            Space complexity: O(n)
        """
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

    def copyRandomList_recursive(self, head):
        """ Time complexity: O(n)
            Space complexity: O(n)
        """
        if not head:
            return None
        if head in self.map:
            return self.map[head]

        newNode = Node(head.val)
        self.map[head] = newNode
        newNode.next = self.copyRandomList_recursive(head.next)
        newNode.random = self.copyRandomList_recursive(head.random)
        return newNode

    map = {}
