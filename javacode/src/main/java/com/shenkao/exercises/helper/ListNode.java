/* Copyright (c) 2021 - present, Timur Shenkao
 * All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.shenkao.exercises.helper;

public class ListNode {
     public int val;
     public ListNode nextNode;

    ListNode(int x, ListNode next) {
        val = x;
        nextNode = next;
    }

    ListNode(int x) {
        this(0, null);
    }

     ListNode() {
        this(0);
     }
}
