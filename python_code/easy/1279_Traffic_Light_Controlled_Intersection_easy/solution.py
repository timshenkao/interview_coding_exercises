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

# 1279. Traffic Light Controlled Intersection  https://leetcode.com/problems/traffic-light-controlled-intersection/
# There is an intersection of two roads.
# First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2.
# Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4.
# There is a traffic light located on each road before the intersection. A traffic light can either be green or red.
#     Green means cars can cross the intersection in both directions of the road.
#     Red means cars in both directions cannot cross the intersection and must wait until the light turns green.
# The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A,
#  it is red on road B and when the light is green on road B, it is red on road A.
# Initially, the traffic light is green on road A and red on road B. When the light is green on one road, all cars can
# cross the intersection in both directions until the light becomes green on the other road.
# No two cars traveling on different roads should cross at the same time.
# Design a deadlock-free traffic light controlled system at this intersection.


class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green_roadId = 1

    def car_arrived(
            self,
            carId: int,                      # ID of the car
            roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,                  # Direction of the car
            turnGreen: Callable[[], None], # Use turnGreen() to turn light to green on current road
            crossCar: Callable[[], None]   # Use crossCar() to make car cross the intersection
    ) -> None:
        self.lock.acquire()
        if roadId != self.green_roadId:
            self.green_roadId = roadId
            turnGreen()
        crossCar()
        self.lock.release()
