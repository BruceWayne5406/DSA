#stack is a kind of data structure that fiollows the "last in first out" principle
#one of the implementations of stack is navigating different webpages in a web browser
#has mainly 3 operations i.e push , pop and peek
#undo functionality in any editor is an implementation of stack
#it uses stack to remember the last set of functions

s=[] #let us use this empty list as a stack
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)

s.pop()
print(s)

s.pop()
print(s)

s.pop()
print(s)