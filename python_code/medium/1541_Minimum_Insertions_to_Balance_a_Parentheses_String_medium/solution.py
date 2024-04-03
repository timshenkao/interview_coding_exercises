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

Time: O(n)
Space: O(1)


class Solution:
    def minInsertions(self, s: str) -> int:
        neededRight = 0   # Increment by 2 for each '('.
        missingLeft = 0   # Increment by 1 for each missing '('.
        missingRight = 0  # Increment by 1 for each missing ')'.

        for c in s:
            if c == '(':
                if neededRight % 2 == 1:
                    # e.g. '()(...'
                    missingRight += 1
                    neededRight -= 1
                neededRight += 2
            else:  # c == ')'
                neededRight -= 1
                if neededRight < 0:
                    # e.g. '()))...'
                    missingLeft += 1
                    neededRight += 2

        return neededRight + missingLeft + missingRight