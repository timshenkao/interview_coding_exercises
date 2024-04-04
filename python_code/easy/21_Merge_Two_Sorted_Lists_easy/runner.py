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

from python_code.helper.linked_lists import print_list, generate_list
from solution import Solution


def main():
    solution = Solution()

    ###########################################################
    l1 = generate_list([1, 2, 4])
    l2 = generate_list([1, 3, 4])
    head = solution.merge_two_lists(l1, l2)
    print_list(head)

    ###########################################################
    l1 = generate_list([2])
    l2 = generate_list([1])
    head = solution.merge_two_lists(l1, l2)
    print_list(head)


if __name__ == "__main__":
    main()
