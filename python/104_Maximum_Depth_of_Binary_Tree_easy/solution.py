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
from helper import TreeNode

# 104. Maximum Depth of Binary Tree  https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
# farthest leaf node.


class Solution:
    def max_depth_recursion(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return 0

        depth_left = self.max_depth_recursion(root.left)
        depth_right = self.max_depth_recursion(root.right)
        return max(depth_left, depth_right) + 1

    def max_depth_iteration(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return 0

        # use stack for Depth First Search
        # keep "depth" of a node along with node
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            # pop node and its depth from stack
            curr_node, curr_depth = stack.pop()
            # current node can be None
            if curr_node:
                # update max depth value
                max_depth = max(curr_depth, max_depth)
                # push to stack children with their depths
                stack.append((curr_node.left, curr_depth + 1))
                stack.append((curr_node.right, curr_depth + 1))
        return max_depth
