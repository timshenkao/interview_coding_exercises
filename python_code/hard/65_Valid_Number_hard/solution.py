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
    def isNumber(self, s):
        s = s.strip()
        pointSeen = eSeen = numberSeen = False
        numberAfterE = True
        for i, c in enumerate(s):
            if "0" <= c <= "9":
                numberSeen = numberAfterE = True
            elif c == ".":
                if eSeen or pointSeen:
                    return False
                pointSeen = True
            elif c == "e":
                if eSeen or not numberSeen:
                    return False
                numberAfterE = False
                eSeen = True
            elif c in "-+":
                if i and s[i - 1] != "e":
                    return False
            else:
                return False
        return numberSeen and numberAfterE
    
Time: O(n)
Space: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seenNum = False
        seenDot = False
        seenE = False

        for i, c in enumerate(s):
            if c == ".":
                if seenDot or seenE:
                    return False
                seenDot = True
            elif c == "e" or c == "E":
                if seenE or not seenNum:
                    return False
                seenE = True
                seenNum = False
            elif c in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False
                seenNum = False
            else:
                if not c.isdigit():
                    return False
                seenNum = True

        return seenNum