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

# 359. Logger Rate Limiter https://leetcode.com/problems/logger-rate-limiter/
# Design a logger system that receives a stream of messages along with their timestamps.
# Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will
# prevent other identical messages from being printed until timestamp t + 10).
# All messages will come in chronological order. Several messages may arrive at the same timestamp.
# Implement the Logger class:
#     Logger() Initializes the logger object.
#     bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given
#     timestamp, otherwise returns false.
# 0 <= timestamp <= 10^9
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 10^4 calls will be made to shouldPrintMessage.


class Logger:
    """ Time complexity: O(N). We iterate through list of messages once
        Space complexity: O(N). We create additional list (logger) which is no more than 10 elements.
        But each element (set) may contain O(N) strings
    """
    def __init__(self):
        self.time_lag_seconds = 10
        self.logger = []  # list of sets
        self.latest_timestamp = -1

    def _update_logger(self, timestamp: int = None, message: str = None, append: bool = False) -> None:
        # add new set for new timestamp
        if append:
            self.logger.append(set())
        if message is not None:
            self.logger[-1].add(message)
        if timestamp is not None:
            self.latest_timestamp = timestamp

    def _check_message_in_logger(self, message: str) -> bool:
        for ts in self.logger:
            if message in ts:
                return True
        return False

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # nothing in logger
        if self.latest_timestamp == -1:
            # add message to logger and update latest timestamp
            self._update_logger(timestamp, message, True)
            return True

        # there are some messages in logger but new timestamp comes
        if timestamp > self.latest_timestamp:
            # number of elements (sets) to delete from logger
            i = max((timestamp - self.latest_timestamp) - (self.time_lag_seconds - len(self.logger)), 0)
            # number of new elements (sets) to add to logger
            k = min(timestamp - self.latest_timestamp, self.time_lag_seconds)
            # deleting from logger
            while self.logger and i > 0:
                self.logger.pop(0)
                i -= 1
            # adding empty elements to logger; latest timestamp is not updated
            for _ in range(k - 1):
                self._update_logger(append=True)

            if not self._check_message_in_logger(message):
                # message is not in cleaned logger; add message to logger and update latest timestamp
                self._update_logger(timestamp, message, True)
                return True
            else:
                # message is already present in cleaned logger; just update latest timestamp
                self._update_logger(timestamp, append=True)
                return False
        # there are some messages in logger, no new timestamp
        else:
            # message is not in logger; add message to logger
            if not self._check_message_in_logger(message):
                self._update_logger(message=message)
                return True
            else:
                # message is in logger
                return False


class LoggerAnother:
    """ Time complexity: O(N). We iterate through list of messages once
        Space complexity: O(N). We create additional dictionary which may contain N elements in worst case.
        Logger is not "cleaned".
    """
    def __init__(self):
        self.record = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.record or timestamp >= self.record[message] + 10:
            self.record[message] = timestamp
            return True
        else:
            return False
