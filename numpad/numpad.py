import pathlib


NUMPAD = {
    2: "a b c".split(),
    3: "d e f".split(),
    4: "g h i".split(),
    5: "j k l".split(),
    6: "m n o".split(),
    7: "p q r s".split(),
    8: "t u v".split(),
    9: "w x y z".split()
}
TEST_INPUT = pathlib.Path(r"C:\Users\Mike\Desktop\scripts\aqua_q_challenges\numpad\input.txt")


def numpad(digit, n):
    return NUMPAD[digit][n-1] if not digit == 0 else " "


def main():
    numbers = pathlib.Path(TEST_INPUT).read_text().split("\n")
    message = "".join(
        [
            numpad(int(digit), int(presses))
            for group in numbers
            for digit, presses in [group.split()]
        ]
    )
    print(message)


if __name__ == '__main__':
    main()
