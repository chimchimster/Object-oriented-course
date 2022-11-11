class Solution(object):
    def removeNthFromEnd (self, head, n):
        count_ = 0
        tail = body = head
        element_pop = None

        while head:
            if count_ == (self.__check_len(head) - n):
                if self.__check_len(head) == 2:
                    head.next = tail
                    return head
                elif self.__check_len(head) == 1:
                    head.next = None
                    return head
                elif self.__check_len(head) == 0:
                    head = None
                    return head
                else:
                    element_pop = tail

            head = head.next
            tail = head

            count_ += 1

        result_ = body

        while result_:
            if result_.next == element_pop:
                body.next = result_.next.next
            else:
                body.next = result_

            result_ = result_.next

        return body

    def __check_len (self, head):
        count = 0

        while head:
            head = head.next
            count += 1

        return count