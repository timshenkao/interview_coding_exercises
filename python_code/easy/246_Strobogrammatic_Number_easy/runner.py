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

    num = "69"
    print(solution.is_strobogrammatic(num))

    num = "88"
    print(solution.is_strobogrammatic(num))

    num = "962"
    print(solution.is_strobogrammatic(num))

    num = "1"
    print(solution.is_strobogrammatic(num))

    num = "8100018"
    print(solution.is_strobogrammatic(num))

    num = "8106018"
    print(solution.is_strobogrammatic(num))

    num = "810018"
    print(solution.is_strobogrammatic(num))

    num = "986986"
    print(solution.is_strobogrammatic(num))

    num = "9869886"
    print(solution.is_strobogrammatic(num))


if __name__ == '__main__':
    main()
