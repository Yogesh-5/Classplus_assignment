def count_bits_in_integer(q):
# At first i will create one variable i.e. count it will return the number of bits in ana integer.

    count = 0
    # after that i will use while condition and it will runs until q greater than 0.
    while(q):

    # afterthat i will use 'and' operator and update q by q & q-1 and will increase the count by one.  
        q = q & (q-1)
        count += 1
    
    #atlast i will return count
    return count
q = 8
print(count_bits_in_integer(q)) 




