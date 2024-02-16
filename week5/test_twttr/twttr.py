def main():
    # user input
    inpt = input("Input:")
    print(shorten(inpt))

    
def shorten(word):

    # result variable
    result = ""
    # capital and small vowels
    list1 = ('AIOUEaeioue')
    # iterate input character by character
    for i in word:
        # if i(character) is in the vowels list
        if i in list1:
            # result is the same
            result = result
        # else if i(character) is not in the vowels list
        else:
            # add i(character) in to the result variable
            result = result + i
    # return the result
    return result

if __name__ == "__main__":
    main()
