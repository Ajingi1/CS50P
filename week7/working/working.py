
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    inp = re.search(r'([0-9]{1,2}):?([0-9][0-9])?\s*(AM|PM)?\s*to\s*([0-9]{1,2}):?([0-9][0-9])?\s(AM|PM)?',s, re.IGNORECASE)


    if not inp:
        raise ValueError
    else:
        srth = int(inp.group(1))

        srtst = inp.group(3)

        enh = int(inp.group(4))

        enst = inp.group(6)
        if (srtst == "PM" and srth < 11):
            srth = srth + 12

        if (enst == "PM" and enh < 11):
            enh = enh + 12

        if ((srtst == "AM" and srth == 12 ) or (srth == 24)):
            srth = f"{00:02}"


        if not (inp.group(2) == None and inp.group(5) == None):
            srtm = int(inp.group(2))
            enm = int(inp.group(5))
            if (srtm > 59 or enm > 59):
                raise ValueError
            return f"{srth:02}:{srtm:02} to {enh:02}:{enm:02}"
        else:
            return f"{srth:02}:{00:02} to {enh:02}:{00:02}"

if __name__ == "__main__":
    main()
