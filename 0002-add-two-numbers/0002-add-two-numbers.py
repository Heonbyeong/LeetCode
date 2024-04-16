# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        node2 = l2
        l1_value_dist = []
        l2_value_dist = []

        l1_num = 0
        l2_num = 0
        node_sum = ""

        while node is not None:
            l1_value_dist.append(node.val)
            node = node.next

        while node2 is not None:
            l2_value_dist.append(node2.val)
            node2 = node2.next

        l1_value_dist.reverse()
        l2_value_dist.reverse()

        l1_num = int("".join(map(str, l1_value_dist)))
        l2_num = int("".join(map(str, l2_value_dist)))

        node_sum = str(l1_num + l2_num)[::-1]
        
        head = ListNode(node_sum[0])
        cur_node = head
        for i in range(1, len(node_sum)):
            cur_node.next = ListNode(node_sum[i])
            cur_node = cur_node.next

        return head
            
