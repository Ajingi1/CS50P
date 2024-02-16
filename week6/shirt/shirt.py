from PIL import Image, ImageOps
import sys



def main():
    check = check_valid()
    image_work(check)


def check_valid():
    ext = (".jpg", ".jpeg", ".png")
    file_1_name, file_1_ext = sys.argv[1].split(".")
    file_2_name, file_2_ext = sys.argv[2].split(".")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 3:
        if not (sys.argv[1].endswith(ext) and sys.argv[2].endswith(ext)):
            sys.exit("Invalid input")
        elif not (file_1_ext.__eq__(file_2_ext)):
            sys.exit("Input and output have different extensions")
        elif (file_1_ext.__eq__(file_2_ext)):
            return True


def image_work(check):
    shirt = Image.open("shirt.png")
    size = shirt.size
    inp_img = Image.open(sys.argv[1])
    inp_img = ImageOps.fit(inp_img, size)
    inp_img.paste(shirt, mask = shirt)
    inp_img.save(sys.argv[2])
if __name__ == "__main__":
    main()
