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


# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
# struct Node {
#     int val;
# Node *left;
# Node *right;
# Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
# set to NULL.
# Initially, all next pointers are set to NULL.
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000


class Solution:
    def connect_iterative_bfs(self, root):
        """ Time complexity: O(n). Iterate through each element
            Space complexity: O(n). We create queue and prev 1-element lists on each iteration.
                              The last level with leaves may contain N/2 nodes in case of balanced tree
        """
        if not root:
            return root
        # iterative Breadth First Search with queue
        q, prev = [(root, 1)], None
        while q:
            curr, depth = q.pop(0)
            if prev and prev[1] == depth:
                prev[0].next = curr
            prev = [curr, depth]
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))
        return root

    def connect_recursive(self, root) :
        """ Recursive
        Time complexity: O(n).
        Space complexity: O(h). h = log N . It's a perfect binary tree
        """
        if not root:
            return None

        def connectTwoNodes(p, q) -> None:
            if not p:
                # because it's perfect binary tree; if there is no left child, then there is no right child
                return
            p.next = q
            # recursive Depth First Search
            connectTwoNodes(p.left, p.right)
            connectTwoNodes(q.left, q.right)
            connectTwoNodes(p.right, q.left)

        connectTwoNodes(root.left, root.right)
        return root

    def connect_iterative_effective(self, root):
        """ Iterative
        Time complexity: O(n).
        Space complexity: O(1).
        """
        node = root  # the node that is above the current
        dummy = Node(0)  # a dummy node before needling
        # Relies on the tree being perfect (no gaps), so not generalizable to imperfect trees.
        # It's perfect binary tree; if there is no left child, then there is no right child
        while node and node.left:
            # Needle the children of the node.
            needle = dummy
            # iterate through level of nodes
            while node:
                needle.next = node.left
                needle = needle.next
                needle.next = node.right
                needle = needle.next
                node = node.next
            node = dummy.next  # Move the node to the next level, i.e. node.left
        return root
