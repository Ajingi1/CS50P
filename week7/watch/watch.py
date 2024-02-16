import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matche = re.search(r'src="([^"]*)"', s)
        final = re.search(r'(https?://)(?:www\.)?youtube.com/embed(.+)', matche.group(1))
        proto = final.group(1)
        vd_id = final.group(2)
        result = f"https://youtu.be{vd_id}"
        return result
    except AttributeError:
        return None

    # http://youtube.com/embed/xvFZjo5PgG0
    # https://youtube.com/embed/xvFZjo5PgG0
    # https://www.youtube.com/embed/xvFZjo5PgG0
    # https://youtu.be/xvFZjo5PgG0



...


if __name__ == "__main__":
    main()
