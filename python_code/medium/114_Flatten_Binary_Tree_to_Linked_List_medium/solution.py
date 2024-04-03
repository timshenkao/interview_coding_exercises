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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node: return
            left, right = traverse(node.left), traverse(node.right)
            if node.left: left.right, node.right, node.left = node.right, node.left, None
            return right if right else left if left else node
        traverse(root)

DFS
Approach 1: Recursive¶
Time:
�
(
    �
)
O(n)
Space:
�
(
    ℎ
)
O(h)

C++
Java
Python

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left  # flattened left
        right = root.right  # flattened right

        root.left = None
        root.right = left

        # Connect the original right subtree to the end of the new right subtree.
        rightmost = root
        while rightmost.right:
            rightmost = rightmost.right
        rightmost.right = right

Approach 2: Iterative (stack)¶
Time:
�
(
    �
)
O(n)
Space:
�
(
    ℎ
)
O(h)

C++
Java
Python

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]

        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if stack:
                root.right = stack[-1]
            root.left = None

Approach 3: Morris-like¶
Time:
�
(
    �
)
O(n)
Space:
�
(
    1
)
O(1)

C++
Java
Python

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        while root:
            if root.left:
                # Find the rightmost root
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                # Rewire the connections
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            # Move on to the right side of the tree
            root = root.right

