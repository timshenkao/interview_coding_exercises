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
    def verticalOrder(self, root):
        q, arrays = root and collections.deque([(root, 0)]) or None, collections.defaultdict(list)
        while q:
            new = collections.deque()
            for node, ind in q:
                arrays[ind].append(node.val)
                if node.left:
                    new.append((node.left, ind - 1))
                if node.right:
                    new.append((node.right, ind + 1))
            q = new
        return [arr for i, arr in sorted(arrays.items())]



Time:
�
(
    �
)
O(n)
Space:
�
(
    �
)
O(n)

C++
Java
Python

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        range_ = [0] * 2

        def getRange(root: Optional[TreeNode], x: int) -> None:
            if not root:
                return

            range_[0] = min(range_[0], x)
            range_[1] = max(range_[1], x)

            getRange(root.left, x - 1)
            getRange(root.right, x + 1)

        getRange(root, 0)  # Get the leftmost and the rightmost x index.

        ans = [[] for _ in range(range_[1] - range_[0] + 1)]
        q = collections.deque([(root, -range_[0])])  # (TreeNode, x)

        while q:
            node, x = q.popleft()
            ans[x].append(node.val)
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))

        return ans
