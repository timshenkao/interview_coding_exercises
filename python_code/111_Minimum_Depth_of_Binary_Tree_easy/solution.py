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

# 111. Minimum Depth of Binary Tree  https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.


class Solution:
    def min_depth_recursion(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return 0

        # node is a leaf
        if not root.left and not root.right:
            return 1

        # either left or right child is missing
        if not root.left or not root.right:
            return max(self.min_depth_recursion(root.left), self.min_depth_recursion(root.right)) + 1
        # both children are present
        else:
            return min(self.min_depth_recursion(root.left), self.min_depth_recursion(root.right)) + 1

    def min_depth_bfs_iteration(self, root):
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(N) if we have to keep the whole tree.
        """
        # empty tree
        if not root:
            return 0

        queue = [(root, 1)]
        while queue:
            curr_node, curr_depth = queue.pop(0)
            if not curr_node.left and not curr_node.right:
                return curr_depth
            if curr_node.left:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth + 1))
