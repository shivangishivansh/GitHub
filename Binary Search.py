##Binary Search
#For binary search, first we need sorted list.

def binary_search(list1,element1):
    Lower_bound = 0
    upper_bound = len(list1)

    while Lower_bound < upper_bound:
        mid_bound = (Lower_bound + upper_bound) // 2
        if list1[mid_bound] == element1:
           print(f"Value is found at {mid_bound} position")
           break
        elif list1[mid_bound] < element1:
            Lower_bound = mid_bound + 1  #We have already check mid_bound. so instead we now go for mid-1
        else:
            upper_bound = mid_bound - 1  #We have already check mid_bound. so instead we now go for mid+1
    else:
        print("Number is not found")


List1 = []
listlength = int(input("How many elements you want to add into the list"))
for i in range(listlength):
    element = int(input("Please enter the number"))
    List1.append(element)

List2 = sorted(List1)
print("This is the list you enterd", List2)
number_to_be_found = int(input("Please enter the number you want to search"))
binary_search(List2,number_to_be_found)