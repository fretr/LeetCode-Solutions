# Definition for singly-linked list.
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

        # initialize our output linked list
        l3 = ListNode()

        # initialize our first node in our output linked list
        nextNode = l3

        # initialize the carry over between addition
        carryOver = 0

        # until there are no more values to add or there is no more carry over ...
        while l1 != None or l2 != None or (carryOver > 0):

            # add the l1 node value and go to the next node
            if l1 != None:
                carryOver += l1.val
                l1 = l1.next

            # add the l2 node value and go to the next node
            if l2 != None:
                carryOver += l2.val
                l2 = l2.next

            # add the carry over to the current node of the output linked list
            nextNode.val += carryOver % 10

            # calculate carry over
            carryOver = carryOver // 10

            # if there is more processing to do, we'll create another node
            if l1 != None or l2 != None or carryOver > 0:
                nextNode.next = ListNode()
                nextNode = nextNode.next

        # return output linked list
        return l3







        
