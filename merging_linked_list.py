from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        str_list = [self.val]
        cur = self.next
        while cur:
            str_list.append(cur.val)
            cur = cur.next
        return str_list.__str__()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


a3 = ListNode(4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)



b3 = ListNode(4)
b2 = ListNode(3, b3)
b1 = ListNode(1, b2)

result = Solution()
print(result.mergeTwoLists(a1, b1))
