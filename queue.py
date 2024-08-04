
from collections import deque

#queue is a data structure that follows the rule FIFO i.e first in first out
#deque is also an implementation of queue in python
#even list can be implemented as a queue in python

stock_prices=[]
stock_prices.insert(0,500)# all the prices are inserted at 0th index in queue
stock_prices.insert(0,800)# as each element is inserted at 0th index, every last element is being shifted one step towards right
stock_prices.insert(0,1000)
stock_prices.insert(0,1500)
stock_prices.pop()#now 500 will get deleted as queue follows "FIFO"


print(stock_prices)

#using list as a queue is not the most efficient method.
#while allocating more memory space,all elements have to be copied initially and then new elements are added in the extra space made.
#instead it is better to use deque , for better time and space complexity.

d1=deque()
d1.appendleft(5)# for implementing a queue elements are always added to the left.
d1.appendleft(8)
d1.appendleft(1)

print(d1)

d1.pop()
print(d1)# here we can see "FIFO" implementation.