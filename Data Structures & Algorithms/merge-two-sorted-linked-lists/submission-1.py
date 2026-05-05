# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(0)
        prev = dummy

        temp1 = list1
        temp2 = list2

        while temp1 and temp2: 

            if temp1.val >=temp2.val:

                prev.next = temp2
                temp2 = temp2.next

            else:
                prev.next = temp1
                temp1 = temp1.next

            prev = prev.next

        while temp1: 

            prev.next = temp1
            temp1 = temp1.next

            prev = prev.next

        while temp2:

            prev.next = temp2

            temp2 = temp2.next

            prev = prev.next

        head = dummy.next

        return head    







                    
        