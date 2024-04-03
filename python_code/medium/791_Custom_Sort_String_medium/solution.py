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
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = set(T)
        t2 = set(S)
        from collections import Counter as ct
        c = ct(T)
        s = [char * c[char] for char in S if char in t]
        add = [char * c[char] for char in t - t2]
        return "".join(s + add)


Time: O(∣order∣+∣s∣)
Space: O(26)



class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in order:
            while count[ord(c) - ord('a')] > 0:
                ans += c
                count[ord(c) - ord('a')] -= 1

        for c in string.ascii_lowercase:
            for _ in range(count[ord(c) - ord('a')]):
                ans += c

        return ans