
# EX2 ---------------------------------------------------------
# def cmmd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# input_string = input("Enter numbers separated by spaces: ")

# number_strings = input_string.split()

# numere = []
# for num_str in number_strings:
    
#         numar = int(num_str)  
#         numere.append(numar)

# cmmd_lista = numere[0]
# for num in numere[1:]:
#     cmmd_lista = cmmd(cmmd_lista, num)

# print(f"Cel mai mare divizor comun al listei este: {cmmd_lista}")




# EX2 ---------------------------------------------------------------


# input_string = input("Enter a string: ")
# input_string = input_string.lower()
# vowel_count = 0
# vowels = "aeiou"
# for char in input_string:
#     if char in vowels:
#         vowel_count += 1

# print(f"Number of vowels in the string: {vowel_count}")



# EX3 ---------------------------------------------------------------


# nStr = input("Enter first string: ")
# pattern = input("Enter second string: ")
# print(nStr)
# print(pattern)

# count = 0
# flag = True
# start = 0

# while flag:
#     a = nStr.find(pattern, start)  
    
#     if a == -1:          
#         flag = False
#     else:               
#         count += 1        
#         start = a + 1
# print("Stringul 2 apare in stringul 1 de atatea ori:")
# print(count)
# EX5 ---------------------------------------------------------





# EX5 ---------------------------------------------------------------
# def spiral_order(matrix):
#     result = []
#     rows, cols = len(matrix), len(matrix[0])



# matrix = [
#     ["f", "i", "r", "s"],
#     ["n", "_", "l", "t"],
#     ["o", "b", "a", "_"],
#     ["h", "t", "y", "p"]
# ]

# # Call the spiral_order function and print the result
# result_string = spiral_order(matrix)
# print(result_string)

# EX6 ---------------------------------------------------------------

# def is_palindrome(number):
#     num_str = str(number)

#     # Check if the string is the same when reversed
#     return num_str == num_str[::-1]

# number=int(input("Introduceti un numar:"))

# if is_palindrome(number):
#     print(f"{number} este palindrome.")
# else:
#     print(f"{number} nu este palindrome.")


# EX7 --------------------------------------------------------------

# def extract(text):
    
#     number_str = ""
#     for char in text:
#         if char.isdigit():
#             number_str += char
#         elif number_str:
#             break
    
    
#     if number_str:
#         return int(number_str)
#     else:
#         return 0


# text1 = "An apple is 123 USD"
# number1 = extract(text1)
# print(f"Extracted number from '{text1}': {number1}")

# text2 = "abc123abc"
# number2 = extract(text2)
# print(f"Extracted number from '{text2}': {number2}")
# text3 = "abc123abc12"
# number3 = extract(text3)
# print(f"Extracted number from '{text3}': {number2}")


#EX8 --------------------------------------------------



# numar=42
# print(bin(numar)[2:])
# string=str(bin(numar)[2:])
# count=0
# print(string)
# for char in string:
#     if int(char)==1:
#         count=count+1

# print(f"numarul are fix {count} cifre de 1")


#EX9 --------------------------------------------------


# string = "an apple is not a tomato ooooo r reee eee ee oooo"
# string = string.lower()

# dict = {}

# for char in string:
#     if char.isalpha(): 
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1

# rezultat = max(dict, key=dict.get)
# nrAparitii = dict[rezultat]

# print(f"Litera'{rezultat}'a aparut de {nrAparitii}.")


#EX10 --------------------------------------------------

string="I have Python exam today so blalal asdfasd aasdf ipsum idle asfa"


pattern=" "
count=0
for char in string:
    if char in pattern:
        count +=1
    
print(f"in text avem {count+1} cuvinte")

print(len(string.split()))
