
# """Implementation Bubble sort"""

# def bubble_sort(data_list):
#     data_length = len(data_list)

#     for i in range(data_length):
#         print("Frist loop", i)
#         for j in range(data_length-i-1):
#             if data_list[j] > data_list[j+1]:
#                 # swap
#                 result = data_list[j]
#                 data_list[j] = data_list[j+1]
#                 data_list[j+1] = result


# if __name__ == "__main__":
#     data_list = [1, 2, 3, 4, 5, 7, 6]
#     bubble_sort(data_list)
#     print("Bubble sort is: ", data_list)



"""Eifficient Bubble sort"""

# def bubble_sort(list_item):
#     list_lenght = len(list_item)

#     for i in range(list_lenght):
#         swap = False
#         print("first loop", i)

#         for j in range(list_lenght-i-1):
#             if list_item[j] > list_item[j+1]:

#                 result = list_item[j]
#                 list_item[j] = list_item[j+1]
#                 list_item[j+1] = result
#                 swap = True
        
#         if swap == False:
#             break

# if __name__ == "__main__":
#     list_item = [1, 2, 3, 4, 5, 7, 6]
#     bubble_sort(list_item)
#     print("Bubble sorted: ", list_item)




