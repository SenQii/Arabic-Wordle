import random
import tkinter as tk


class FontColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GREY = '\33[90m'
    RESET = '\033[39m'


class BG:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'


class Style:
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



last_word = ""
tries = 5
can_attempt = True


# def main():
#     main_Screen = tk.Tk()
#     main_Screen.title("gg")
#     main_Screen.geometry('400x600')
#
#     btn = tk.Button(
#         text="enter",
#         fg="blue",
#         bd='5',
#         command=main_Screen.destroy
#     )
#     btn.pack()
#     main_Screen.mainloop()


words_length = {
    "4": "four.txt",
    "5": "five.txt",
    "6": "six.txt"
}


def select_length():
    print("****************************************************************")
    print("أهلا بك في ووردل. \nلبدء اللعبة، أولًا عليك اختيار طول الكلمة السرية:")
    print("من 4-5 ... اختر طول الكلمة السرية المناسب وادخل الرقم:")

    x = True

    while x:
        user_length = input()
        if not user_length.isdigit():
            print("ony type numbers!!")
            continue
        if int(user_length) > 6 or int(user_length) < 4:
            print(" from 4-6 only")
            continue

        return user_length


def read_word():
    # global last_word
    words_file = select_length()

    with open(words_length.get(words_file)) as f:
        words = f.read().splitlines()
        new_word = random.choice(words)
        return new_word


# user has 6 hearts
def run(word):
    Try = 1
    while can_attempt:
        print(Style.RESET_ALL + "===========================")
        print(f"المحاولة {Try}")
        guess = input()

        # make sure his word == length of the right word
        if len(guess) != len(word):
            print("الأطوال غير متطابقة")
            continue
        else:
            for letter in range(min(len(guess), 5)):
                if guess[letter] == word[letter]:
                    print(FontColor.GREEN + guess[letter], end="")
                    continue

                elif guess[letter] in word:
                    print(FontColor.YELLOW + guess[letter], end="")

                    continue

                else:
                    print(FontColor.GREY + guess[letter], end="")
            print()
            Try += 1

            if Try  == tries:
                print(FontColor.RESET,"انتهت محاولاتك!")
                print("الكلمة كانت ",FontColor.YELLOW + word + FontColor.RESET,"... حظ أوفر")
                break

            if guess == word:
                print(Style.RESET + "\U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973")
                print(FontColor.BLUE + "كفو!!!")

                break


def start_play():
    word = read_word()
    run(word)


if __name__ == '__main__':
    # main()
    start_play()
