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

from python_code.helper.binary_trees import generate_binary_tree
from solution import Solution


def main():
    solution = Solution()

    ###########################################################
    root = generate_binary_tree([1, 2, 3, 4, 5])
    print(solution.diameter_of_binary_tree_recursion(root))

    root = generate_binary_tree([1, 2])
    print(solution.diameter_of_binary_tree_recursion(root))

    root = generate_binary_tree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None,
                                 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])
    print(solution.diameter_of_binary_tree_recursion(root))


if __name__ == "__main__":
    main()
