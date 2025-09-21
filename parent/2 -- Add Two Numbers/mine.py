# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ANALYSIS:
        # - We need to add two numbers represented by linked lists
        # - We can iterate through both lists and add the values
        # - We can keep track of the remainder
        # - We can create a new linked list to store the result
        # Time complexity: O(n) 
        # Space complexity: O(n)

        ans_node = ListNode(0)
        curr_1 = l1
        curr_2 = l2
        curr_ans = ans_node
        prev_ans = None

        rem = 0
        ans = []
        curr_sum = 0

        while curr_1 or curr_2:            
            val1 = val2 = 0
            if curr_1:
                val1 = curr_1.val
            if curr_2:
                val2 = curr_2.val


            curr_sum = val1 + val2 + rem
            print(curr_sum)
            if curr_sum > 9:
                #remainder logic
                ans.append(curr_sum - 10)
                curr_ans.val = (curr_sum - 10)
                rem = 1
            else:
                ans.append(curr_sum)
                curr_ans.val = curr_sum
                rem = 0
            
            curr_ans.next = ListNode()
            prev_ans = curr_ans
            curr_ans = curr_ans.next


            if curr_1:
                curr_1 = curr_1.next
                
            if curr_2:
                curr_2 = curr_2.next
                
            
        if rem:
            curr_ans.next = ListNode()

            prev_ans = curr_ans
            curr_ans = curr_ans.next
            prev_ans.val = rem
        
        if prev_ans:
            prev_ans.next = None

        return ans_node
