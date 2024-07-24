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

#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """ Time complexity: O(n)
            Space complexity: O(n)
            BFS
        """
        q, res = [root], []
        while any(q):
            res.append(q[-1].val)
            q = [child for node in q for child in (node.left, node.right) if child]
        return res

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        """ Time complexity: O(n)
            Space complexity: O(n)
            BFS
        """
        if not root:
            return []
        ans = []
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                root = q.popleft()
                if i == size - 1:
                    ans.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return ans

    def rightSideView3(self, root: Optional[TreeNode]) -> List[int]:
        """ Time complexity: O(n)
            Space complexity: O(n)
            Recursive DFS
        """
        ans = []
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return
            if depth == len(ans):
                ans.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return ans
