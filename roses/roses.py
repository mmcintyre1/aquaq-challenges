from itertools import islice
import re



def chunk(it, size):
    """Creates an iterator from a passed in iterable and builds n-sized tuples as a return."""
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def make_hex(string):
    # replace non hexdecimal characters with 0
    string = re.sub("[^a-fA-F0-9]", "0", string)
    # pad string to multiple of 3
    string = string.ljust(len(string) + (3 - len(string) % 3))
    # split into 3 sections
    chunks = list(chunk(string, len(string) // 3))
    # first two digits of each section
    print("".join(["".join(x[:2]) for x in chunks]))


def main():
    test = "do you think that maybe like, 1 in 10 people could be actually robots?"
    hex_string = make_hex(test)


if __name__ == '__main__':
    main()