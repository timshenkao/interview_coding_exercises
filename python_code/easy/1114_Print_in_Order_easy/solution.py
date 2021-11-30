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

from threading import Lock
from typing import Callable

# 1114. Print in Order https://leetcode.com/problems/print-in-order/
# Suppose we have a class Foo.
# The same instance of Foo will be passed to three different threads.
# Thread A will call first(), thread B will call second(), and thread C will call third().
# Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed
# after second().
# Note: We do not know how the threads will be scheduled in the operating system, even though the numbers in the input
# seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.


class Foo:
    def __init__(self):
        self.first_lock = Lock()
        self.first_lock.acquire()

        self.second_lock = Lock()
        self.second_lock.acquire()

    def first(self, print_first: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print_first()
        # Notify the thread that is waiting for the first job to be done.
        self.first_lock.release()

    def second(self, print_second: Callable[[], None]) -> None:
        # Wait for the first job to be done
        with self.first_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            print_second()
            # Notify the thread that is waiting for the second job to be done.
            self.second_lock.release()

    def third(self, print_third: Callable[[], None]) -> None:
        # Wait for the second job to be done.
        with self.second_lock:
            # printThird() outputs "third". Do not change or remove this line.
            print_third()
