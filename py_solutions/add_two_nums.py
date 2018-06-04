 # coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def to_representation(self):
        cur = self
        values = []
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        
        print(", ".join(values))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not(l1 and l2):
            return l1 or l2
        
        sum = l1.val + l2.val 
        res = ListNode(sum % 10)
        cur = res
        this_n = l1.next
        another_n = l2.next

        while this_n or another_n:
            if not this_n:
                this_n = ListNode(0)
            if not another_n:
                another_n = ListNode(0)
            sum = int(sum / 10) + this_n.val + another_n.val
            cur.next = ListNode(sum % 10)
            cur = cur.next
            this_n = this_n.next
            another_n = another_n.next
        
        if sum >= 10:
            cur.next = ListNode(int(sum / 10))
        
        return res


# def valid_braces(braces):
#     if not braces:
#         return False

#     stack = []
#     stack.append(braces[0])

#     for brace in braces[1:]:
#         if stack and is_pair(stack[-1], brace):
#             stack.pop()
#         else:
#             stack.append(brace)
    
#     return len(stack) == 0


# class Braces(object):
#     def __init__(self, braces):
#         self.braces = braces
    
#     def valid(self):
#         return True

#     def is_pair(self, left, right):
#         brace_pairs = {
#             '{':'}',
#             '[':']',
#             '(':')'
#         }
#         return brace_pairs.get(left) == right



if __name__ == '__main__':
    assert valid_braces('') == False
    assert valid_braces('{[({})]}') == True
    assert valid_braces('{}{})(}') == False