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

from python_code.helper.binary_trees import TreeNode

# 700. Search in a Binary Search Tree  https://leetcode.com/problems/search-in-a-binary-search-tree/
# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.


class Solution:
    def search_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ Time complexity: O(N). We iterate through the tree in Breadth First Search style
            Space complexity: O(1).
        """
        # if tree is empty, do not do anything
        if not root:
            return None

        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    def search_BST_recursion(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ Time complexity: O(h). h - height of the tree, h = log N. In-order traversal.
            Space complexity: O(1).
        """
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            return self.search_BST(root.right, val)
        else:
            return self.search_BST(root.left, val)
