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

import itertools

# 844. Backspace String Compare https://leetcode.com/problems/backspace-string-compare/
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:
        """ Time complexity: O(N). We iterate through strings once.
            Space complexity: O(1).
        """
        s_index = len(s) - 1
        t_index = len(t) - 1

        s_num_backspaces = 0
        t_num_backspaces = 0

        while s_index > -1 or t_index > -1:
            # if characters aren't equal and aren't '#', then we have discrepancy
            if s[s_index] != t[t_index] and t[t_index] != '#' and s[s_index] != '#':
                return False
            # if characters are equal and aren't '#', then go to the next characters
            # check for boundaries
            elif s[s_index] == t[t_index] != '#' and s_index > -1 and t_index > -1:
                s_index -= 1
                t_index -= 1
            # if there is '#' in s, skip characters. There could be several consecutive '#'
            # check for boundaries
            elif s_index > -1 and s[s_index] == '#':
                s_num_backspaces += 1
                # skip '#'
                s_index -= 1
                while s_num_backspaces > 0 and s_index > -1:
                    if s[s_index] == '#':
                        s_num_backspaces += 1
                    else:
                        s_num_backspaces -= 1
                    s_index -= 1
            # if there is '#' in t, skip characters. There could be several consecutive '#'
            # check for boundaries
            elif t_index > -1 and t[t_index] == '#':
                t_num_backspaces += 1
                # skip '#'
                t_index -= 1
                while t_num_backspaces > 0 and t_index > -1:
                    if t[t_index] == '#':
                        t_num_backspaces += 1
                    else:
                        t_num_backspaces -= 1
                    t_index -= 1
            # situation when finished handling t but there are still characters in s and some of them aren't '#'
            elif s_index >= 0 and t_index < 0 and s[s_index] != '#':
                return False
            # situation when finished handling s but there are still characters in t and some of them aren't '#'
            elif s_index < 0 and t_index >= 0 and t[t_index] != '#':
                return False
        return True

    def backspace_compare_generator(self, s: str, t: str) -> bool:
        """ Time complexity: O(N). We iterate through each string once.
            Space complexity: O(1).
        """
        # this solution is concise but requires itertools
        # it's unclear whether zip_longest() will be present in future versions
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))
