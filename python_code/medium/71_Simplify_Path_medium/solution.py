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

from typing import List

# 71. Simplify Path  https://leetcode.com/problems/simplify-path/
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
# Your task is to transform this absolute path into its simplified canonical path.
# The rules of a Unix-style file system are as follows:
#       A single period '.' represents the current directory.
#       A double period '..' represents the previous/parent directory.
#       Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
#       Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
#       For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#       The path must start with a single slash '/'.
#       Directories within the path must be separated by exactly one slash '/'.
#       The path must not end with a slash '/', unless it is the root directory.
#       The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        components = [component for component in path.split('/') if component]
        stack = []

        # Process each component
        for component in components:
            if component == '.':
                continue  # Current directory, ignore
            elif component == '..':
                if stack:  # Go to parent by popping last directory
                    stack.pop()
            else:
                stack.append(component)  # Valid directory/file name
        return '/' + '/'.join(stack) if stack else '/'
