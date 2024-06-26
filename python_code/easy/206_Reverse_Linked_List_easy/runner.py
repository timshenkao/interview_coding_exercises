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

from solution import Solution
from python_code.helper.linked_lists import generate_list, print_list


def main():
    solution = Solution()

    head1 = generate_list([1, 2, 3, 4, 5, 6])
    print_list(solution.reverse_list(head1))

    head1 = generate_list([1, 2, 3, 4, 5])
    print_list(solution.reverse_list(head1))


if __name__ == "__main__":
    main()
