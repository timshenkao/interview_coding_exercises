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

from collections import OrderedDict
from typing import List

# 412. Fizz Buzz  https://leetcode.com/problems/fizz-buzz/
# Given an integer n, return a string array resultwer (1-indexed) where:
#     resultwer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     resultwer[i] == "Fizz" if i is divisible by 3.
#     resultwer[i] == "Buzz" if i is divisible by 5.
#     resultwer[i] == i (as a string) if none of the above conditions are true.
# 1 <= n <= 104


class Solution:
    def fizz_buzz(self, n: int) -> List[str]:
        """ Time complexity: O(n). We iterate from 1 to n.
            Space complexity: O(n). We create output list of strings.
        """
        fizz = "Fizz"
        buzz = "Buzz"
        fizz_buzz = "FizzBuzz"

        result = list()
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                result.append(fizz_buzz)
            elif i % 3 == 0:
                result.append(fizz)
            elif i % 5 == 0:
                result.append(buzz)
            else:
                result.append(str(i))
        return result

    def fizz_buzz_lookup(self, n: int) -> List[str]:
        """ Time complexity: O(n). We iterate from 1 to n. We perform fixed amount of computations on each iteration.
            Space complexity: O(n). We create output list of strings.
        """
        # Lookup for all fizzbuzz mappings
        fizz_buzz_dict = OrderedDict({3: "Fizz", 5: "Buzz"})

        result = list()
        i_result = list()
        for i in range(1, n + 1):
            i_result.clear()
            for key in fizz_buzz_dict.keys():
                # If the number is divisible by key,
                # then add the corresponding string mapping to current i_result
                if i % key == 0:
                    i_result.append(fizz_buzz_dict[key])

            if not i_result:
                i_result.append(str(i))
            result.append("".join(i_result))
        return result
