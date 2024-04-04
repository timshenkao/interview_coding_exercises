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


def main():
    solution = Solution()

    logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

    print("Using first comparator")
    print(solution.reorder_log_files_comparator(logs1))
    print(solution.reorder_log_files_comparator(logs2))

    print("Using second comparator")
    print(solution.reorder_log_files_comparator(logs1))
    print(solution.reorder_log_files_comparator2(logs2))


if __name__ == "__main__":
    main()
