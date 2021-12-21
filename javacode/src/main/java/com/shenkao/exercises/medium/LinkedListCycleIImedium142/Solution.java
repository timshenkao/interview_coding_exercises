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

/* 142. Linked List Cycle II  https://leetcode.com/problems/linked-list-cycle-ii/
 Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
 There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
 following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
 connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
 Do not modify the linked list.
 The number of the nodes in the list is in the range [0, 10 ^ 4].
 -10 ^ 5 <= Node.val <= 10 ^ 5
 pos is -1 or a valid index in the linked-list.
 Can you solve it using O(1) (i.e. constant) memory?
*/

package com.shenkao.exercises.medium.LinkedListCycleIImedium142;


import com.shenkao.exercises.helper.ListNode;


public class Solution {
     /** Time complexity: O(N). If there is no cycle, then fast pointer iterates to the tail of linked list.
                          If there is cycle, then slow pointer iterates distance equal to cycle length +
                          distance to the start of the cycle; fast pointer iterates distance equal to
                          2 * cycle length + distance to the start of the cycle
         Space complexity: O(1).
     */
    public ListNode detectCycle(ListNode head) {
        // empty list or list with single element
        if (head == null || head.nextNode == null){
            return null;
        }

        ListNode slowPointer = head;
        ListNode fastPointer = head;

        // detect cycle if it exists
        while (fastPointer != null && fastPointer.nextNode != null) {
            slowPointer = slowPointer.nextNode;
            fastPointer = fastPointer.nextNode.nextNode;
            // if there is cycle in the list, then slow and fast will point to the same node eventually within the cycle
            if (slowPointer == fastPointer) {
                break;
            }
        }

        // either empty list or there is no cycle
        if (slowPointer != fastPointer){
            return null;
        }

        // reset slow pointer
        slowPointer = head;
        // To find the start to the cycle, both fast and slow pointers iterate at
        // the same speed: slow pointer from head of the list; fast pointer from the point of intersection within the
        // cycle
        while (fastPointer != slowPointer) {
            slowPointer = slowPointer.nextNode;
            fastPointer = fastPointer.nextNode;
        }
        return fastPointer;
    }
}
