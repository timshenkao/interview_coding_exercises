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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, mn, mx):
            if not node: return True
            if node.val<mn or node.val>mx: return False
            return validate(node.left,mn,node.val-1) and validate(node.right,node.val+1,mx)
        return validate(root, -float("inf"),float("inf"))

    def isValidBST2(self, root) -> bool:
        """ DFS Recursive
        Time complexity: O(n). 
        Space complexity: O(n).
        """        
        def isValidBST(root, minNode, maxNode) -> bool:
            if not root:
                return True
            if minNode and root.val <= minNode.val:
                return False
            if maxNode and root.val >= maxNode.val:
                return False

            return isValidBST(root.left, minNode, root) and \
                isValidBST(root.right, root, maxNode)

        return isValidBST(root, None, None)

    def isValidBST3(self, root) -> bool:
        """ Iterative Stack
        Time complexity: O(n).
        Space complexity: O(n).
        """
        stack = []
        pred = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and pred.val >= root.val:
                return False
            pred = root
            root = root.right

        return True
