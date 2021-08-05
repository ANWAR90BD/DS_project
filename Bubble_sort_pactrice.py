
# def bubble_sort(data):
#     data_length = len(data)

#     for i in range(data_length):
#         for j in range(data_length-i-1):
#             if data[j] > data[j+1]:

#                 temp = data[j]
#                 data[j] = data[j+1]
#                 data[j+1] = temp


# if __name__ == "__main__":
#     data = [12, 25, 75, 84, 4, 5, 6, 7, 10]
#     bubble_sort(data)
#     print("Bubble sort is: ", data)

    

# def bubble_sort(data_list):
#     n = len(data_list)

#     for i in range(n):
#         for j in range(n-i-1):
#             if data_list[j] < data_list[j+1]:
#                 return data_list[j]

#             if data_list[j] > data_list[j+1]:
#                 temp = data_list[j]
#                 data_list[j] = data_list[j+1]
#                 data_list[j+1] = temp




# if __name__ == "__main__":
#     data_list = [1, 2, 5, 45, 85, 75, 35]
#     bubble_sort(data_list)
#     print("sorted list: ", data_list)







# def sorted_list(list):
#     n = len(list)

#     for i in range(n-1):
#         mid_index = i
#         for j in range(i+1, n):
#             if list[j] < list[mid_index]:
#                 mid_index = j
            
#         if mid_index != i:
#             result = list[i]
#             list[i] = list[mid_index]
#             list[mid_index] = result


# if __name__ == "__main__":
#     list = [12, 24, 45, 78, 45, 50]
#     sorted_list(list)
#     print(list)


# n = 5
# for i in range(n-1):
#     print("first loop: ", i)
#     for j in range(i+1, n):
#         print("Second loop", j)




# def bubble_sort(list):
#     n = len(list)

#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:

#                 result = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = result
            

# if __name__ == "__mian__":
#     list = [12, 5, 6, 4, 87, 50]
#     bubble_sort(list)
#     print(list)



# def bubble_sort(list):
#     n = len(list)

#     for i in range(n):
#         print("first loop", i)
#         for j in range(n-1-i):
#             if list[j] > list[j+1]:

#                 result = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = result
#                 #print("second loop: ", j)

# if __name__ == "__main__":
#     list = [1, 2, 3, 4, 7, 6]
#     bubble_sort(list)
#     print(list)



def bubble_sort(list):
    n = len(list)

    for i in range(n):
        swap = False
        print("frist loop", i)

        for j in range(n-i-1):
            if list[j] > list[j+1]:
                result = list[j]
                list[j] = list[j+1]
                list[j+1] = result
                swap = True
                #print("second loop", j)
        
        if swap == False:
            break
            
if __name__ == "__main__":
    list = [1, 2, 3, 4, 7, 6]
    bubble_sort(list)
    print(list)
