# import package
import emoji

# collect input from user
input_em = input("Input:")

# condition when user put :thumbsup:
if input_em == ":thumbsup:":

    # creat empty str variable
    input_mod = ""

    # iterate throught input
    for i in input_em:
        # put input str in to this empty variable
        input_mod = input_mod + i
        # s detected put underscore after it
        if i == "s":
            input_mod = input_mod + "_"
    #  print the variable that store str
    print("Output:", emoji.emojize(input_mod))

# if , detected divide the input in to two from first space you detected
elif "," in input_em:
    # put the first part to fir and second part to sec
    fir, sec = input_em.split(" ")

    # use the fir and sec here
    print("Output:", fir, emoji.emojize(sec.strip(), language='alias'))
# else if none of these conditio detected use the first variable 
else:
    print("Output:", emoji.emojize(input_em))

