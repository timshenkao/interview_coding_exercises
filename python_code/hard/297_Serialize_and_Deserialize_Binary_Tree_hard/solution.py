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

class Codec:

    def serialize(self, root):
        q, s = root and collections.deque([root]), ""
        while q:
            node = q.popleft()
            if node is None:
                s += "null#"
            else:
                s += str(node.val) + "#"
                q += [node.left, node.right]
        return s


    def deserialize(self, data):
        data = data and collections.deque(data.split("#"))
        q, root = data and collections.deque([TreeNode(int(data.popleft()))]), None
        while q:
            node = q.popleft()
            if not root:
                root = node
            l, r = data.popleft(), data.popleft()
            if l != "null":
                node.left = TreeNode(int(l))
                q.append(node.left)
            if r != "null":
                node.right = TreeNode(int(r))
                q.append(node.right)
        return root


Approach 1: BFS
Time: O(n)
Space: O(n)



class Codec:
    def serialize(self, root: "TreeNode") -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        s = ""
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node:
                s += str(node.val) + " "
                q.append(node.left)
                q.append(node.right)
            else:
                s += "n "

        return s

    def deserialize(self, data: str) -> "TreeNode":
        """Decodes your encoded data to tree."""
        if not data:
            return None

        vals = data.split()
        root = TreeNode(vals[0])
        q = collections.deque([root])

        for i in range(1, len(vals), 2):
            node = q.popleft()
            if vals[i] != "n":
                node.left = TreeNode(vals[i])
                q.append(node.left)
            if vals[i + 1] != "n":
                node.right = TreeNode(vals[i + 1])
                q.append(node.right)

        return root


Approach 2: DFS
Time: O(n)
Space:  O(n)


class Codec:
    def serialize(self, root: "TreeNode") -> str:
        """Encodes a tree to a single string."""
        s = []

        def preorder(root: "TreeNode") -> None:
            if not root:
                s.append("n")
                return

            s.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return " ".join(s)

    def deserialize(self, data: str) -> "TreeNode":
        """Decodes your encoded data to tree."""
        q = collections.deque(data.split())

        def preorder() -> "TreeNode":
            s = q.popleft()
            if s == "n":
                return None

            root = TreeNode(s)
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()