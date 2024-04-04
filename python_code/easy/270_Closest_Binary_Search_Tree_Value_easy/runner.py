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

    root = generate_binary_tree([4, 2, 5, 1, 3])
    target = 3.714286
    print(solution.closest_value(root, target))

    root = generate_binary_tree([1])
    target = 4.428571
    print(solution.closest_value(root, target))


if __name__ == "__main__":
    main()
