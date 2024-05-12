# Definition for singly-linked list.
from functools import reduce

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        t1 = []
        t2 = []
        
        # Linked List to Python List
        while l1 != None:
            t1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            t2.append(l2.val)
            l2 = l2.next

        # Reverse the list
        t1.reverse()
        t2.reverse()

        # python list to integer
        a = reduce(lambda a,b: a*10+b, t1)
        b = reduce(lambda a,b: a*10+b, t2)
        
        # sum of two ints
        r = a + b

        # Integer to list
        if r == 0:
            res.append(0)
        while r != 0:
            b = r % 10
            res.append(b)
            r = r // 10
        
        # Python List to Linked List
        a = ListNode()
        b = a
        i = 0
        while i < len(res):
            a.val = res[i]
            if i == len(res) - 1:
                a.next = None
            else:
                a.next = ListNode()
                a = a.next
            i += 1
        
        return b
                
        

# Tests
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
Solution().addTwoNumbers(l1, l2)

l3 = ListNode(0, None)
l4 = l3
Solution().addTwoNumbers(l3, l4)

l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
Solution().addTwoNumbers(l5, l6)

