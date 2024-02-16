imageName = input("File Name:")
imageName = imageName.strip().lower()
seper = "."
extenName = imageName.partition(seper)[2]

if imageName.endswith(".gif"):
    print("image/" + extenName ,end="")
elif imageName.endswith(".jpg"):
    print("image/jpeg" ,end="")
elif imageName.endswith(".jpeg"):
    print("image/" + extenName ,end="")
elif imageName.endswith(".png"):
    print("image/" + extenName ,end="")
elif imageName.endswith(".pdf"):
    print("application/pdf" ,end="")
elif imageName.endswith(".txt"):
    print("text/plain",end="")
elif imageName.endswith(".zip"):
    print("application/" + extenName ,end="")
else:
    print("application/octet-stream")

