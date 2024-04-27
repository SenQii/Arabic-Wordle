import random


# ASCII codes for colored op
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
    RESET = '\033[0m'


# globals
LAST_WORD = ""
TRIES = 5
words_length = {
    4: "./words/four.txt",
    5: "./words/five.txt",
    6: "./words/six.txt"
}


#  prompt user to select word length
def select_length():
    print("لبدء اللعبة، أولًا عليك اختيار طول الكلمة السرية (4-6):")

    while True:
        user_length = input()

        # case: non digit inp
        if not user_length.isdigit():
            print("أدخل أرقام فقط")
            continue

        user_length = int(user_length)
        # case: out of range inpt
        if user_length > 6 or user_length < 4:
            print("ادخل من 4-6 فقط")
            continue

        return user_length


# get the selected length => read file => return random word
def read_word():
    words_file = select_length()
    file_name = words_length.get(words_file, "./words/five.txt")  # "five" as default in case err

    with open(file_name) as selected_file:
        words = selected_file.read().splitlines()
        new_word = random.choice(words)

        return new_word


# main func | user guess till attempts run out \ won
def run(word):
    attempt = 1

    while True:
        print(FontColor.RESET + "===========================")
        print(f"المحاولة {attempt}")
        guess = input()  # every loop take users guess

        # case: umatched input length
        if len(guess) != len(word):
            print("الأطوال غير متطابقة")
            continue

        # for every letter
        for letter in range(len(guess)):

            # case: right letter & right place:
            if guess[letter] == word[letter]:
                print(FontColor.GREEN + guess[letter], end="")
                continue

            # case: right letter but wrong place:
            elif guess[letter] in word:
                print(FontColor.YELLOW + guess[letter], end="")
                continue

            # case wrong letter
            else:
                print(FontColor.GREY + guess[letter], end="")

        print()

        #  WIN
        if guess == word:
            print(FontColor.RESET + "\U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973")
            print(FontColor.BLUE + "كفو!!!", FontColor.RESET)

            break

        #  LOSE
        if attempt == TRIES:
            print(FontColor.RESET, "انتهت محاولاتك!")
            print("الكلمة كانت ", FontColor.YELLOW + word + FontColor.RESET, "... حظ أوفر")
            break

        attempt += 1  # TO THE NEXT TRY

    print("اكتب 1 للعب جولة أخرى")
    replay = input()

    if replay == "1":
        start_play()
    else:
        return


def start_play():
    print("****************************************************************")
    print("أهلا بك في ووردل.")

    word = read_word()
    run(word)


