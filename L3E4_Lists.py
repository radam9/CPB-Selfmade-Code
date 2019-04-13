#Lists, reverse indexing works in lists
list1 = [1,2,3]
list2 = ['string',100,23.2]
print(len(list1))
print(len(list2))
#list works just like strings, so you can apply slicing and indexing
list = ['one','two','three']
print(list[0])
print(list[1:])
#Concatenation
list_a = ['four','five']
print(list + list_a)
new_list = list + list_a
print(new_list)
#unlike strings, lists are mutable, you can change parts of it
new_list[0] = "ONE ALL CAPS"
print(new_list)
#add an element to the end of the list (append)
new_list.append('six')
print(new_list)
#removing an item of a list
popped_item = new_list.pop() #it removed only the last element
print(new_list)
print(popped_item)
item = new_list.pop(3)
print(item)
print(new_list)
#sorts and reverse methods for Lists
list = ['a','x','e','b','c']
list_num = [4,1,8,3]
list.sort() #the list is changed and sorted, so you lose the initial order
print(list)
list_num.sort()#the returned value of the .sort() method is None,
#so if you put it inside the print() it will print None
print(list_num)
#reverse method, reverses everything in the list. same properties as sort()
list_num.reverse()
print(list_num)
#how to create a list using multiplication
mlist = [0] * 3
print(mlist)
