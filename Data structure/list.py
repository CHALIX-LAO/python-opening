# Traverse the LIST
def traverse_list(lst):
    for item in lst:
        print(item)
my_list = [1, 2, 3, 4, 5]
traverse_list(my_list)

# Accessing elements in a LIST
def access_elements(lst):
    print("First element:", lst[0])
    print("Second to last element:", lst[-2])         


my_list = [10, 20, 30, 40, 50]
access_elements(my_list)

# lenght of the list
def length(lthelist):
    return len(lthelist)
x= length([1,2,3,4,5])
print("Length of the list:", x)

# decrement of list by 1
def decrement_list(lst):
    return [x - 1 for x in lst]
y= decrement_list([5, 10, 15, 20])
print("Decremented list:", y)
