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

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                if num:
                    #print(i, num)
                    i += num
                    num = 0
                if i >= len(word) or word[i] != c:
                    #print(i, c)
                    return False
                i += 1
        return i == len(word) if num == 0 else i + num == len(word)


Time: O(n)
Space: O(1)


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # word's index
        j = 0  # abbr's index

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if not abbr[j].isdigit() or abbr[j] == '0':
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num

        return i == len(word) and j == len(abbr)