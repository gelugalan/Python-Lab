#--------------------Ex1-----------------------

def fibonacci(n):
    listN=[]
    n1,n2=0,1
    for i in range(n):
        listN.append(n1)
        n1,n2=n2,n1+n2
    return listN

n=int(input("Introduceti n= "))
print(n)
print(fibonacci(n))

#--------------------Ex2-----------------------
# def prim(n):
#     nr=0;
#     for i in range(1,n):
#         if n % i==0:
#             nr+=1
#     if nr==1:
#         return True
#     else:
#         return False

# def getprim(listn):
#     listPrim=[]
#     for num in listn:
#         if prim(num)==True:
#             listPrim.append(num)
#     return listPrim

# n = int(input("Introduceți n = "))
# listNum = list(range(2, n))
# print(listNum)

# print(getprim(listNum))

#--------------------Ex3-----------------------

# def functionMat(a, b):
#     intersection = list(set(a) & set(b))
#     union = list(set(a) | set(b))
#     a_minus_b = list(set(a) - set(b))
#     b_minus_a = list(set(b) - set(a))
#     return intersection, union, a_minus_b, b_minus_a

# # Example usage:
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# result = functionMat(a, b)

# print("A intersected with B:", result[0])
# print("A reunited with B:", result[1])
# print("A - B:", result[2])
# print("B - A:", result[3])

#--------------------Ex4-----------------------

# def compose(notes, moves, start_position):
#     song = []
#     current_position = start_position
#     song.append(notes[current_position])
#     for move in moves:
        
        
#         current_position = (current_position + move) % len(notes)
#         song.append(notes[current_position])

#     return song


# musical_notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]

# start_position = 2

# result = compose(musical_notes, moves, start_position)
# print(result)


#--------------------Ex5-----------------------
# def manageMatrix(matrix):
#     n = len(matrix)  # Obține numărul de rânduri (dimensiunea matricei)
    
#     for row in range(n):
#         for col in range(n):
#             if col < row:
#                 matrix[row][col] = 0
#     return matrix

# def generate_matrix(n):
#     matrix = []
#     num = 1  # Inițializați numărul de la care să începeți

#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(num)
#             num += 1  # Incrementați numărul pentru următoarea poziție
#         matrix.append(row)
#     return matrix

# n = int(input("Introduceți dimensiunea matricei (n): "))
# matrix = generate_matrix(n)

# result_matrix=manageMatrix(matrix)

# for row in result_matrix:
#     print(row)


#--------------------Ex6-----------------------
#--------------------Ex7-----------------------


# def is_palindrome(number):
#         return str(number) == str(number)[::-1]

# def find_palindromes(numbers):
#     palindrome_count = 0
#     greatest_palindrome = None

#     for number in numbers:
#         if is_palindrome(number):
#             palindrome_count += 1
#             if greatest_palindrome is None or number > greatest_palindrome:
#                 greatest_palindrome = number

#     return (palindrome_count, greatest_palindrome)


# numbers = [121, 12321, 45654, 123, 78987]
# result = find_palindromes(numbers)
# print("Number of palindromes:", result[0])
# print("Greatest palindrome:", result[1])
   

#--------------------Ex8-----------------------

# def filter_strings(x=1, string_list=[], flag=True):
#     result = []

#     for s in string_list:
#         filtered_chars = []
#         for char in s:
#             char_code = ord(char)
#             if (flag and char_code % x == 0) or (not flag and char_code % x != 0):
#                 filtered_chars.append(char)
#         result.append(filtered_chars)

#     return result


# x = 2
# strings = ["test", "hello", "lab002"]
# flag = False

# filtered_lists = filter_strings(x, strings, flag)
# print(filtered_lists)


#--------------------Ex9-----------------------

# def find_obstructed_seats(heights):
#     obstructed_seats = []

#     for row in range(0,len(heights)):
#         for col in range(len(heights[0])):
#             spectator_height = heights[row][col]
#             can_see_game = True

#             for r in range(0, row):
#                 if heights[r][col] >= spectator_height:
#                     can_see_game = False
#                     break

#             if not can_see_game:
#                 obstructed_seats.append((row, col))

#     return obstructed_seats

# field = [
#     [1, 2, 3, 2, 1, 1],
#     [2, 4, 4, 3, 7, 2],
#     [5, 5, 2, 5, 5, 4],
#     [6, 6, 7, 6, 7, 5]
# ]

# obstructed = find_obstructed_seats(field)
# print(obstructed)

#--------------------Ex10-----------------------

# def combine_lists(*args):
#     max_length = max(len(lst) for lst in args)
#     result = []

#     for i in range(max_length):
#         tuple_items = tuple(lst[i] if i < len(lst) else None for lst in args)
#         result.append(tuple_items)

#     return result

# # Example usage:
# list1 = [1, 2, 3,5]
# list2 = [5, 6, 7]
# list3 = ["a", "b", "c"]

# result = combine_lists(list1, list2, list3)
# print(result)
#--------------------Ex11-----------------------

# def custom_sort(tuple_list):
#     def key_function(item):

#         if len(item[1]) >= 3:
#             return item[1][2]
#         else:
           
#             return '\0' 

    
#     sorted_list = sorted(tuple_list, key=key_function)
#     return sorted_list


# input_list = [('abc', 'bcd'), ('abc', 'zza')]
# sorted_result = custom_sort(input_list)
# print(sorted_result)

#--------------------Ex12-----------------------

def group_by_rhyme(words):
    rhyme_groups = {}
    
    for word in words:
       
        rhyme = word[-2:] 
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            
            rhyme_groups[rhyme] = [word]
    result = list(rhyme_groups.values())
    
    return result

# Example usage:
words = ['ana', 'banana', 'carte', 'arme', 'parte','farte','carme']
result = group_by_rhyme(words)
print(result)
