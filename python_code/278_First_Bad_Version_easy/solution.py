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

# 278. First Bad Version  https://leetcode.com/problems/first-bad-version/
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes
# all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


class Solution:
    def first_bad_version(self, n: int) -> int:
        """ Time complexity: O(log N).
            Space complexity: O(1).
        """
        # we have no array, so we can enumerate from 1 to n
        left_index = 1
        right_index = n

        # use modification of binary search
        while left_index < right_index:
            middle = left_index + (right_index - left_index) // 2
            # if middle element is bad, then the first bad element is in the left half
            if isBadVersion(middle):
                right_index = middle
            # otherwise it is in the right half
            else:
                left_index = middle + 1
        # when left_index = right_index
        return left_index
