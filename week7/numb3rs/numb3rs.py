import re
import sys



def main():
    print(validate(input("IPv4 Address: ")))

    
def validate(ip):

    matche =  re.search(r"^((1[0-9]{2}|2[0-4][0-9]|25[0-5])|([1-9]|[0-9])|([0-9]))\.((1[0-9]{2}|2[0-4][0-9]|25[0-5])|([1-9]|[0-9])|([0-9]))\.((1[0-9]{2}|2[0-4][0-9]|25[0-5])|([1-9]|[0-9])|([0-9]))\.((1[0-9]{2}|2[0-4][0-9]|25[0-5])|([1-9]|[0-9])|([0-9]))$", ip)
    if not matche:
        return False
    else:
        return True

if __name__ == "__main__":
    main()

