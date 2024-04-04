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
from solution import Logger


def _print_logger(logger: Logger, logs: List) -> None:
    for log in logs:
        print(logger.shouldPrintMessage(timestamp=log[0], message=log[1]))


def main():
    logger = Logger()

    logs = [[0, "A"], [0, "B"], [0, "C"], [0, "A"], [0, "B"], [0, "C"], [0, "A"], [0, "B"], [0, "C"], [0, "A"]]
    _print_logger(logger, logs)

    # logs = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
    # _print_logger(logger, logs)


if __name__ == "__main__":
    main()
