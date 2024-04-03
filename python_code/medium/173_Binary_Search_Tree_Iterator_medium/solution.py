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

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node != None:
            self.stack += (node,)
            node = node.left


Approach 1: Recursive¶
Time: Constructor:
�
(
    �
)
O(n), next():
�
(
    1
)
O(1), hasNext():
�
(
    1
)
O(1)
Space:
�
(
    �
)
O(n)

C++
Java
Python

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.i = 0
        self.vals = []
        self._inorder(root)

    def next(self) -> int:
        self.i += 1
        return self.vals[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.vals)

    def _inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self._inorder(root.left)
        self.vals.append(root.val)
        self._inorder(root.right)

Approach 2: Iterative¶
Time: Constructor:
�
(
    ℎ
)
O(h), next():
�
(
    ℎ
)
O(h), hasNext():
�
(
    1
)
O(1)
Space:
�
(
    ℎ
)
O(h)

C++
Java
Python

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._pushLeftsUntilNull(root)

    def next(self) -> int:
        root = self.stack.pop()
        self._pushLeftsUntilNull(root.right)
        return root.val

    def hasNext(self) -> bool:
        return self.stack

    def _pushLeftsUntilNull(self, root: Optional[TreeNode]) -> None:
        while root:
            self.stack.append(root)
            root = root.left