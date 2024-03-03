class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        double_i = head
        while i and double_i:
            for _ in range(2):
                double_i = double_i.next
                if not double_i:
                    return False
                if double_i == i:
                    return True
            i = i.next
        return False