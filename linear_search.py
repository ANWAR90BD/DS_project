# list = [12, 25, 65, 78, 89, 45, 50]
# search = 50

# for i in range(len(list)):
#     result = list[i]
#     if result == search:
#         print("Found in index: ", i)
#     print("Not found this list")


# list = [12, 25, 65, 78, 89, 45, 50]
# search = 50
# found = False
# for i in range(len(list)):
#     result = list[i]
#     if result == search:
#         found = True
#         break
# if found == True:
#     print("Foun in index: ",i)
# else:
#     print("Not found this list")


# def linear_search(list, found, search):
#     for i in range(len(list)):
#         result = list[i]
#         if result == search:
#             found = True
#             break
#     if found == True:
#         return "Found here in index", i
#     else:
#         return "Not found in list"

# list = [12, 56, 78, 56, 87, 98]
# search = 87
# found = False

# print(linear_search(list, found, search))




# def linear_search(list, found, search):
#     for i in range(len(list)):
#         result = list[i]
#         if result == search:
#             found = True
#             break
#     if found == True:
#         print("Found here in index:",i)
#     else:
#         print("Not found in list")

# list = [12, 56, 78, 56, 87, 98]
# search = 87
# found = False

# linear_search(list, found, search)


# Recursive function to search x in arr[l..r]
def recSearch( arr, l, r, x):
	if r < l:
		return -1
	if arr[l] == x:
		return l
	if arr[r] == x:
		return r
	return recSearch(arr, l+1, r-1, x)

# Driver Code
arr = [12, 34, 54, 2, 3]
n = len(arr)
x = 3
index = recSearch(arr, 0, n-1, x)
if index != -1:
	print ("Element", x,"is present at index %d" %(index))
else:
	print ("Element %d is not present" %(x))

# Contributed By Harshit Agrawal
