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

    file = "abc"
    n = 4
    buf = [''] * n
    print(solution.read(buf, n))

    file = "abcde"
    n = 5
    buf = [''] * n
    print(solution.read(buf, n))

    file = "abcdABCD1234"
    n = 12
    buf = [''] * n
    print(solution.read(buf, n))

    file = "leetcode"
    n = 5
    buf = [''] * n
    print(solution.read(buf, n))
    

if __name__ == '__main__':
    main()