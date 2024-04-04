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

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solution.intersection(nums1, nums2))


if __name__ == "__main__":
    main()
