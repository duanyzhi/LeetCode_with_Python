""""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

head->2 是表头：
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = ListNode(0)
        sum_result = output
        while l1 or l2:
            if l1 is None:
                sum_result.data += l2.data
            elif l2 is None:
                sum_result.data += l1.data
            else:
                sum_result.data += l1.data + l2.data
            if sum_result.data > 9:
                sum_result.data -= 10
                sum_result.next_node = ListNode(1)  # 进位
            else:
                if l1 is not None and l1.next_node or l2 is not None and l2.next_node:
                    sum_result.next_node = ListNode(0)

            if l1 is not None and l1.next_node or l2 is not None and l2.next_node:
                if l1 is None:
                    l2 = l2.next_node
                elif l2 is None:
                    l1 = l1.next_node
                else:
                    l1 = l1.next_node
                    l2 = l2.next_node
                sum_result = sum_result.next_node
            else:
                 return output


# 构建一个基本链表结构，链表是由node组成，一个node包含一个value和一个指向其他node的指针(pointer)
class ListNode(object):
    def __init__(self, data):
        self.data = data   # value
        self.next = None  # next初始化为None，可以随时改成指向其他node

    @property
    def next_node(self):
        return self.next

    @next_node.setter
    def next_node(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        # super(UnorderedList, self).__init__()
        self.head = None

    def add(self, item):
        temp = ListNode(item)
        temp.next_node = self.head
        self.head = temp


def List_Print(list_node):
    while list_node.next_node is not None:
        print(list_node.data)
        list_node = list_node.next_node
    print(list_node.data)

first_num = list(input("Please input your first list nums:"))
second_num = list(input("Please input your second list nums:"))

list1 = UnorderedList()
for ii in range(len(first_num)):
    list1.add(int(first_num[ii]))

list2 = UnorderedList()
for jj in range(len(second_num)):
    list2.add(int(second_num[jj]))

S = Solution()
result = S.addTwoNumbers(list1.head, list2.head)
List_Print(result)
