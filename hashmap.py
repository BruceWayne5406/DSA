#hashmap is a data structure that stores a value corresponding to some other value
#this value is stored at a particular index
#dictionary is an implementation of hashmap in python
#when you enter a key,you can retrieve the value by using a dictionary
#key is converted into the value by using a hashfunction
#the hashfunction converts each character inside the key into its corresponding ASCII value
#it then sums all of them up to come up with a single number 
#this number is then divided by the array size(let's say 10) and the remainder is the index no.
#let us make a dictionary using the hashmap data structure
#the following program helps us understand ,how does a dictionary really work internally

class HashTable:
    def __init__(self):
        self.MAX=100 #here we are assuming this as the array size
        self.arr=[None for i in range(self.MAX)]
    
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char) #ord function converts each character of the key into ASCII value,and here we are summing them up
     
        return h%self.MAX

    def add(self,key,value):#using this function we will be able to see the value i.e 130 at the 9th index on the array
        h=self.get_hash(key)
        self.arr[h]=value
    
    def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    
    def delete(self,key):
        h=self.get_hash(key)
        self.arr[h]=None


t=HashTable()
t.get_hash("march 9")
t.add("march 9",130)
print(t.arr)
print(t.get("march 9"))
print(t.delete("march 9"))

#there can be a case where using the hash function you get same index for key values of 2 different keys.
#in that case we use chaining
#in chaining both of the keys along with their respective key values are stored at the same index in the form of a list
#to get a specific key value we use linear search. This whole method is called chaining

#there is a second approach to solving this problem,i.e by linear probing
#in this method when the indices of two keys collide,
#the second key value is stored at the nearest vacant space


