#Here in this question i will use hare-tortoise algorithm for finding the middle element.

def middle(head):
    # Atfirst i will take variable first one is slow and second one is fast and assign value of both elements as head.
    slow = head
    fast = head
    
    #i will use loop and this loop will run fast and fast.next != Null.
    while(fast and fast.next):
        # here i will inrement the value of slow by one step and increment the value of fist by 2 step.
        slow = slow.next
        fast = fast.next.next
    
    #atlast i will return slow.
    return slow


