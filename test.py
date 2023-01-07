#this is a python script

#print("Hello Wurld")

#end
def mul_five(num):
    #takes a number and multiplies it by 5
    num=num*5
    return num

"""
print(mul_five(5)) #25
print(mul_five(10)) #50
"""

def list_mul_five(listo):
    #iterate through the list, multiplying every num by 5
    for i in range(0,len(listo)):

        listo[i] = listo[i] * 5

    return listo

"""
print(list_mul_five([0,1,2,3]))
"""

def reverse_list(listo):
    #takes a list and reverses it
    #create a new list, then going backwards, add each value

    new_list = []

    for i in range(len(listo)-1,-1,-1):
        new_list.append(listo[i])

    return new_list

"""
print(reverse_list([0,1,2,3]))
"""

class Operations:

    def add(self,num1,num2):
        new_num = num1 + num2
        return new_num

    def subtract(self,num1,num2):
        new_num = num1-num2
        return new_num

    def multiply(self,num1,num2):
        new_num = num1*num2
        return new_num

    def divide(self,num1,num2):
        new_num = num1//num2 #doesn't get decimal
        return new_num

"""
nums = Operations()
print("12 ",nums.add(10,2))
print("8 ",nums.subtract(10,2))
print("20 ",nums.multiply(10,2))
print("5 ",nums.divide(10,2))
"""

def fizz_buzz(num):

    #if divisible by 3 then fizz, by 5 buzz, and by 3 and 5 fizzbuzz

    print("fizz_buzz up to",num)

    for i in range(num+1):

        if (i % 3 == 0) and (i % 5 == 0) and (i > 0):
            print(i,": fizzbuzz")
        elif (i % 3 == 0) and (i > 0):
            print(i,": fizz")
        elif (i % 5 == 0) and (i > 0):
            print(i,": buzz")
        else:
            print(i)

"""
fizz_buzz(15)
fizz_buzz(100)
"""

def read_string(filename):

    file1 = open(filename,"a")

    file1.write("to grow is to be human") #why did it override the text?
    file1.close()

    file1 = open(filename,"r+")
    for line in file1:
        print(line)

    file1.close()

"""
read_string("text.txt")
"""

def reverse_2(listo):

    for i in range(0,len(listo)//2):
        print(i)
        temp = listo[i] #temporarily take the current value
        listo[i] = listo[len(listo)-1-i] #make the current value the opposite
        listo[len(listo)-1-i] = temp #make the last one what the current value was

    return listo
"""
print(reverse_2([0,3,5,7,10]))
print(reverse_2([0,2,8,10]))
print(reverse_2(["a",2,8,10,45,78,8889,"b"]))
"""

def tester(list):

    #goes through the numbers in the list, tries dividing 10 by the numbers

    try:
        for item in list:
            print(10/item)
    except:
        print("I cannee do it")
"""
tester([1,5,10])
tester([3,6,0])
"""

def recursive(x,y,num):
#spaces times the number of num, then x * y
    print(" "*num,str(x+y))

    if num >= 1:
        recursive(x*y,x*y,num-1)
        recursive(x*y,x*y,num-1)

#recursive(3,3,3)

class node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
        cur_node.next=new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = linked_list()
my_list.display() #should show nothing
my_list.append(5)
my_list.append(15)
my_list.display()
