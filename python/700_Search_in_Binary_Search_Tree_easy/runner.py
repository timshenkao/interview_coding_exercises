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
from solution import Solution, TreeNode
from typing import Optional


def print_bst(root: Optional[TreeNode]) -> None:
    print()
    if root:
        print('node: ', root, '; value: ', root.val, '; left : ', root.left, '; right : ', root.right)
        if root.left:
            print_bst(root.left)
        if root.right:
            print_bst(root.right)


def print_node(node: Optional[TreeNode]) -> None:
    print()
    print('node: ', node, '; value: ', node.val, '; left : ', node.left, '; right : ', node.right)


def main():
    solution = Solution()

    ###########################################################
    n4 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n4, n3)
    n1 = TreeNode(7)
    root = TreeNode(4, n2, n1)

    print_bst(solution.search_BST(root, 5))


if __name__ == '__main__':
    main()
