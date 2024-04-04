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
from solution import MyLinkedList


def main():
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.print()

    ll.addAtIndex(1, 2)
    ll.print()

    print(ll.get(0))
    print(ll.get(1))
    print(ll.get(2))
    print(ll.get(3))

    ll.deleteAtIndex(1)
    ll.print()

    print(ll.get(1))

    ll.deleteAtIndex(1)
    ll.print()

    ll2 = MyLinkedList()
    ll2.addAtHead(84)
    ll2.addAtTail(2)
    ll2.addAtTail(39)
    ll2.get(3)
    ll2.get(1)
    ll2.addAtTail(42)
    ll2.addAtIndex(1, 80)
    ll2.addAtHead(14)
    ll2.addAtHead(1)
    ll2.addAtTail(53)
    ll2.addAtTail(98)
    ll2.addAtTail(19)
    ll2.addAtTail(12)
    ll2.get(2)
    ll2.addAtHead(16)
    ll2.addAtHead(33)
    ll2.addAtIndex(4, 17)
    ll2.addAtIndex(6, 8)
    ll2.addAtHead(37)
    ll2.addAtTail(43)
    ll2.print()

    ll2.deleteAtIndex(11)
    ll2.print()

    ll2.addAtHead(80)
    ll2.addAtHead(31)
    ll2.addAtIndex(13, 23)
    ll2.addAtTail(17)
    ll2.get(4)
    ll2.addAtIndex(10, 0)
    ll2.addAtTail(21)
    ll2.addAtHead(73)
    ll2.addAtHead(22)
    ll2.addAtIndex(24, 37)
    ll2.addAtTail(14)
    ll2.addAtHead(97)
    ll2.addAtHead(8)
    ll2.get(6)
    ll2.deleteAtIndex(17)
    ll2.print()

    ll2.addAtTail(50)
    ll2.addAtTail(28)
    ll2.addAtHead(76)
    ll2.addAtTail(79)
    ll2.get(18)
    ll2.deleteAtIndex(30)
    ll2.print()

    ll2.addAtTail(5)
    ll2.addAtHead(9)
    ll2.addAtTail(83)
    ll2.deleteAtIndex(3)
    ll2.print()

    ll2.addAtTail(40)
    ll2.deleteAtIndex(26)
    ll2.print()

    ll2.addAtIndex(20, 90)
    ll2.deleteAtIndex(30)
    ll2.print()

    ll2.addAtTail(40)
    ll2.addAtHead(56)
    ll2.addAtIndex(15, 23)
    ll2.addAtHead(51)
    ll2.addAtHead(21)
    ll2.get(26)
    ll2.addAtHead(83)
    ll2.get(30)
    ll2.addAtHead(12)
    ll2.deleteAtIndex(8)
    ll2.print()

    ll2.get(4)
    ll2.addAtHead(20)
    ll2.addAtTail(45)
    ll2.get(10)
    ll2.addAtHead(56)
    ll2.get(18)
    ll2.addAtTail(33)
    ll2.get(2)
    ll2.addAtTail(70)
    ll2.addAtHead(57)
    ll2.addAtIndex(31, 24)
    ll2.addAtIndex(16, 92)
    ll2.addAtHead(40)
    ll2.addAtHead(23)
    ll2.deleteAtIndex(26)
    ll2.print()

    ll2.get(1)
    ll2.addAtHead(92)
    ll2.addAtIndex(3, 78)
    ll2.addAtTail(42)
    ll2.get(18)
    ll2.addAtIndex(39, 9)
    ll2.get(13)
    ll2.addAtIndex(33, 17)
    ll2.get(51)
    ll2.addAtIndex(18, 95)
    ll2.addAtIndex(18, 33)
    ll2.addAtHead(80)
    ll2.addAtHead(21)
    ll2.addAtTail(7)
    ll2.addAtIndex(17, 46)
    ll2.get(33)
    ll2.addAtHead(60)
    ll2.addAtTail(26)
    ll2.addAtTail(4)
    ll2.addAtHead(9)
    ll2.get(45)
    ll2.addAtTail(38)
    ll2.addAtHead(95)
    ll2.addAtTail(78)
    ll2.get(54)
    ll2.addAtIndex(42, 86)


if __name__ == "__main__":
    main()
