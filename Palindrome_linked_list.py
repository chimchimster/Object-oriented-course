from typing import Optional


class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        d, count = self.create_dict(head1)
        x = count // 2
        while head:
            if head.val == d[count-1].val:
                head = head.next
                count -= 1
                if count == x:
                    return True
                continue
            else:
                return False

    def create_dict(self, head):
        d = {}
        count = 0
        while head:
            d[count] = head
            head = head.next
            count += 1
        return d, count


s = Solution()


print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))))
print(s.isPalindrome(ListNode(1, ListNode(1, ListNode(2, ListNode(1, None))))))
print(s.isPalindrome(ListNode(1, ListNode(2, None))))
print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(3, None)))))


