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
package com.shenkao.exercises.medium.LinkedListCycleIImedium142;

import com.shenkao.exercises.helper.ListNode;
import com.shenkao.exercises.helper.MyLinkedList;


public class  Runner{
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] values = {3, 2, 0, -4};
        int pos = 1;
        ListNode head = MyLinkedList.generateListCycle(values, pos);
        MyLinkedList.printNode(solution.detectCycle(head));

        values = new int[] {1, 2};
        pos = 0;
        head = MyLinkedList.generateListCycle(values, pos);
        MyLinkedList.printNode(solution.detectCycle(head));

        values = new int[] {1};
        pos = -1;
        head = MyLinkedList.generateListCycle(values, pos);
        MyLinkedList.printNode(solution.detectCycle(head));

    }
}
