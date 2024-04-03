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

class Solution:
    def lowestCommonAncestor(
            self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent, stack = {root: None}, [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q


Approach 1: Recursive¶
Time:
�
(
    ℎ
)
O(h)
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


Approach 2: Iterative¶
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
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        q_ = collections.deque([root])
        parent = {root: None}
        ancestors = set()  # p's ancestors

        # Iterate until we find both p and q.
        while p not in parent or q not in parent:
            root = q_.popleft()
            if root.left:
                parent[root.left] = root
                q_.append(root.left)
            if root.right:
                parent[root.right] = root
                q_.append(root.right)

        # Insert all the p's ancestors.
        while p:
            ancestors.add(p)
            p = parent[p]  # `p` becomes None in the end.

        # Go up from q until we meet any of p's ancestors.
        while q not in ancestors:
            q = parent[q]

        return q

    