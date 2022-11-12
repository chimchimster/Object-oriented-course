class ListNode(object):
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd (self, head, n):
        x, y, z = head, head, head
        count_ = 0
        length = self.__check_len(head)
        index_ = abs(length - n - 1)

        while x:
            if count_ == index_:
                if length in (n, 0):
                    x = None
                    return x
                elif length == 1:
                    x.next = None
                    return x
                else:
                    break

            count_ += 1

        count_ = 1
        node = y
        result = ListNode()
        result.next = node
        result.val = node.val
        while node:
            to_check_next = z.next
            if count_ >= index_ - 1:
                first_el = node
                first_el.val = node.val
                n = first_el.next = to_check_next.next
                v = first_el.next.val = first_el.next.next.val

                result.next = ListNode(v, n)
                result.next = ListNode(val=0, next=None)
                break

            result.next = ListNode(node.val, node.next.next)
            count_ += 1
            
            s = ''
            while result.next:
                s += str(result.next.val) + ' ,'
                result.next = result.next.next
            s = s.strip(', ')
            print(f'[{s[::-1]}]')

    def __check_len (self, head):
        count = 0

        while head:
            head = head.next
            count += 1
        return count


l = ListNode(6, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None))))))
s = Solution()
print(s.removeNthFromEnd(l, 2))
