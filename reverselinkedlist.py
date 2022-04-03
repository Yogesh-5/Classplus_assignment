def reverse(head):
    # first i will make two variable first on is prev and second one is current.
    #after that i will assign prev as None
    #and assign current as head
    prev = None
    current = head
    
    # afterthat i will use loop and this loop will run until current != Null
    while(current):
        # i will create one next variable which represent the next node of current node.
        next = current.next
        # Here i set pointer of next to prev.
        current.next = prev
        # here i will set prev to current and in next i will set current to next of current/
        prev = current
        current = next
    
    # atlast i will return prev.
    return prev      
   
