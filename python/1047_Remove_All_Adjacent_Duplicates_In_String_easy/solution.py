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

# 1047. Remove All Adjacent Duplicates In String https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
# adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def remove_duplicates(self, s: str) -> str:
        """ Time complexity: O(n). We iterate through the whole string once.
            Space complexity: O(n). In the worst case scenario, we add all symbols to the final string.
        """
        final_symbols = []
        for elem in s:
            if final_symbols and elem == final_symbols[-1]:
                final_symbols.pop()
            else:
                final_symbols.append(elem)
        return ''.join(final_symbols)
