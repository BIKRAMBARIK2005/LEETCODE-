# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        s = []
        curr = head

        while curr != None:
            s.append(curr.val)
            curr = curr.next

        l = len(s)

        s1 = []
        s2 = []
        s3 = []
        s4 = []

        if l % 2 == 0:          # Even length
            for i in range(l // 2):
                s1.append(s[i])

            for j in range(l // 2, l):
                s2.append(s[j])

            if s1 == s2[::-1]:
                return True

        else:                   # Odd length
            for i in range(l // 2):
                s3.append(s[i])

            for j in range(l // 2 + 1, l):
                s4.append(s[j])

            if s3 == s4[::-1]:
                return True

        return False