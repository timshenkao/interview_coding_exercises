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

    ###########################################################
    n = 2
    trust = [[1, 2]]
    print(solution.find_judge(n, trust))
    print(solution.find_judge_one_array(n, trust))

    n = 3
    trust = [[1, 3], [2, 3]]
    print(solution.find_judge(n, trust))
    print(solution.find_judge_one_array(n, trust))

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(solution.find_judge(n, trust))
    print(solution.find_judge_one_array(n, trust))

    n = 3
    trust = [[1, 2], [2, 3]]
    print(solution.find_judge(n, trust))
    print(solution.find_judge_one_array(n, trust))

    n = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    print(solution.find_judge(n, trust))
    print(solution.find_judge_one_array(n, trust))


if __name__ == "__main__":
    main()
