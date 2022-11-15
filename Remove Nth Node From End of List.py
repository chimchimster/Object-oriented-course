class ListNode(object):
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd (self, head, n):
        length = self.__check_len(head)
        index_ = abs(length - n)


        if length in (n, 0):
            head = None
            return head
        elif length == 1:
            head.next = None
            return head

        count_ = 0
        x = head.next
        while head:
            if count_ == index_:
                head.next = x.next.next
                head.next.val = x.next.val
                break
            x = head.next
            count_ += 1

        while head:
            print(head.val, end=' ')
            head = head.next

    def __check_len (self, head):
        count = 0

        while head:
            head = head.next
            count += 1
        return count


l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
s = Solution()
print(s.removeNthFromEnd(l, 2))
