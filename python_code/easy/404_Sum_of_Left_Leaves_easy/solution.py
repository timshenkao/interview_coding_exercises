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

# 404. Sum of Left Leaves  https://leetcode.com/problems/sum-of-left-leaves/
# Given the root of a binary tree, return the sum of all left leaves.
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000


class Solution:
    def sum_of_left_leaves(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree or single node
        if not root or (not root.left and not root.right):
            return 0
        # there is left child which is a leaf
        # add its value to the sum from right child
        if root.left and (not root.left.left and not root.left.right):
            return root.left.val + self.sum_of_left_leaves(root.right)
        # otherwise add sums from both left and right children
        else:
            return self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)


    def sum_of_left_leaves_iteration(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree or single node
        if not root or (not root.left and not root.right):
            return 0

        queue = [root]
        result = 0
        # use queue and traverse in Breadth-First Search style
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left:
                # leaf detected
                if not curr_node.left.left and not curr_node.left.right:
                    result += curr_node.left.val
                # not leaf, handle later
                else:
                    queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return result

    def sum_of_left_leaves_morris(self, root: Optional[TreeNode]) -> int:
        """ Time complexity: O(N). We check / visit some nodes once and others - twice.
            Space complexity: O(1). We don't keep stack or queue or make recursive calls.
            Morris traversal algorithm works by temporarily modifying the input tree: it becomes not tree because of
            temporarily added loop edge from in-order predecessor to root.
            Before we explore a left subtree, we find the left subtree root's in-order predecessor (which will never
            have a right child), and make root its right child (right link point back up to the root).
            Then we explore the left subtree.
            When we're done exploring the left subtree, the link back up to the root will allow us to return to the root
            and explore the right subtree.
            When we follow the link back up, we also remove it so that the input tree is restored.
        """
        # empty tree or single node
        if not root or (not root.left and not root.right):
            return 0

        result = 0
        curr_node = root
        while curr_node is not None:
            # there is no left child, proceed to right child
            if curr_node.left is None:
                curr_node = curr_node.right
            else:
                temp = curr_node.left
                # Check if it's a leaf node.
                if not temp.left and not temp.right:
                    result += temp.val
                # Find the inorder predecessor for current node (left subtree).
                # check if we connected inorder predecessor back to current node
                while temp.right is not None and temp.right is not curr_node:
                    temp = temp.right
                # We've not visited the inorder predecessor yet.
                # We have to explore current node's left subtree.
                # Before doing this, we will put a link back so that we can get back to the current node
                if temp.right is None:
                    temp.right = curr_node
                    curr_node = curr_node.left
                # We have already visited the inorder predecessor.
                # We need to remove the link we added, and then handle the right subtree
                else:
                    temp.right = None
                    curr_node = curr_node.right
        return result
