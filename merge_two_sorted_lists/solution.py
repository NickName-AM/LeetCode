# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        node = ListNode()
        head = node

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
        
        if not list1:
            node.next = list2
        
        elif not list2:
            node.next = list1
        
        return head.next


        
            


a = Solution

# list1 = ListNode(1, ListNode(2, ListNode(4, None)))
# list2 = ListNode(1, ListNode(3, ListNode(4, None)))

list1 = None
list2 = ListNode(0)

r = a().mergeTwoLists(list1,list2)

while r:
    print(r.val)
    r = r.next
