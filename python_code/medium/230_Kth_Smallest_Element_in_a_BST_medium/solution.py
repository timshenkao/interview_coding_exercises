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
    def __init__(self):
        self.k, self.res = 0, None
    def kthSmallest(self, root, k):
        if self.k < k and root.left: self.kthSmallest(root.left, k)
        self.k += 1
        if self.k == k: self.res = root.val
        if self.k < k and root.right: self.kthSmallest(root.right, k)
        return self.res


Approach 1: Binary Search¶
Time:
�
(
    �
    2
)
O(n
2
)
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def countNodes(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + countNodes(root.left) + countNodes(root.right)

        leftCount = countNodes(root.left)

        if leftCount == k - 1:
            return root.val
        if leftCount >= k:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - 1 - leftCount)  # leftCount < k

Approach 2: Inorder Traversal¶
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 0
        ans = 0

        def traverse(root: Optional[TreeNode]) -> None:
            nonlocal rank
            nonlocal ans
            if not root:
                return

            traverse(root.left)
            rank += 1
            if rank == k:
                ans = root.val
                return
            traverse(root.right)

        traverse(root)
        return ans


Approach 3: Stack¶
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root:
            stack.append(root)
            root = root.left

        for _ in range(k - 1):
            root = stack.pop()
            root = root.right
            while root:
                stack.append(root)
                root = root.left

        return stack[-1].val


