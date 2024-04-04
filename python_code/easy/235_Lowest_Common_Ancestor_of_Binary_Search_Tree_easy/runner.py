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

from python_code.helper.binary_trees import generate_binary_tree, print_node, TreeNode
from solution import Solution


def main():
    solution = Solution()

    ###########################################################
    root = generate_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2, None, None)
    q = TreeNode(8, None, None)
    print_node(solution.lowest_common_ancestor_recursion(root, p, q))
    print_node(solution.lowest_common_ancestor_iteration(root, p, q))

    root = generate_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2, None, None)
    q = TreeNode(4, None, None)
    print_node(solution.lowest_common_ancestor_recursion(root, p, q))
    print_node(solution.lowest_common_ancestor_iteration(root, p, q))

    root = generate_binary_tree([2, 1])
    p = TreeNode(2, None, None)
    q = TreeNode(1, None, None)
    print_node(solution.lowest_common_ancestor_recursion(root, p, q))
    print_node(solution.lowest_common_ancestor_iteration(root, p, q))


if __name__ == "__main__":
    main()
