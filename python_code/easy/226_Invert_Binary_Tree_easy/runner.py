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

from python_code.helper.binary_trees import generate_binary_tree, print_binary_tree
from solution import Solution


def main():
    solution = Solution()

    ###########################################################
    root = generate_binary_tree([4, 2, 7, 1, 3, 6, 9])
    print_binary_tree(root)
    print()
    print_binary_tree(solution.invert_tree_recursion(root))
    print()

    root = generate_binary_tree([2, 1, 3])
    print_binary_tree(root)
    print()
    print_binary_tree(solution.invert_tree_recursion(root))
    print()

    root = generate_binary_tree([])
    print_binary_tree(root)
    print()
    print_binary_tree(solution.invert_tree_recursion(root))
    print()


if __name__ == "__main__":
    main()
