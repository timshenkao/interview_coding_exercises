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
from solution import Foo
from threading import Thread


def print_first():
    print('first')


def print_second():
    print('second')


def print_third():
    print('third')


def main():
    a = Foo()
    t1 = Thread(target=a.second, args=(print_second,))
    t2 = Thread(target=a.third, args=(print_third,))
    t3 = Thread(target=a.first, args=(print_first,))

    t1.start()
    t3.start()
    t2.start()


if __name__ == '__main__':
    main()
