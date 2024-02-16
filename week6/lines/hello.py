
# user input
inpt = input("Input:")

# capital and small vowels

list1 = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

# result variable

result = ""

# iterate input character by character

for i in inpt:

    # if i(character) is in the vowels list

    if i in list1:

        # result is the same

        result = result

    # else if i(character) is not in the vowels list

    else:

        # add i(character) in to the result variable

        result = result + i

# print the result
        
print(result)

