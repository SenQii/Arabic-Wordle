import random


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


last_word = ""
tries = 5
can_attempt = True


words_length = {
    "4": "four.txt",
    "5": "five.txt",
    "6": "six.txt"
}


def select_length():
    print("****************************************************************")
    print("أهلا بك في ووردل."
          "\nلبدء اللعبة، أولًا عليك اختيار طول الكلمة السرية (4-6):")
    x = True

    while x:
        user_length = input()
        if not user_length.isdigit():
            print("أدخل أرقام فقط")
            continue
        if int(user_length) > 6 or int(user_length) < 4:
            print("ادخل من 4-6 فقط")
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
    trys = 1
    while can_attempt:
        print(FontColor.RESET + "===========================")
        print(f"المحاولة {trys}")
        guess = input()

        # check for guess length & lang
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
            trys += 1

            if trys == tries:
                print(FontColor.RESET, "انتهت محاولاتك!")
                print("الكلمة كانت ", FontColor.YELLOW + word + FontColor.RESET, "... حظ أوفر")
                break

            if guess == word:
                print(FontColor.RESET + "\U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973 \U0001F973")
                print(FontColor.BLUE + "كفو!!!", FontColor.RESET)

                break

    print("اكتب 1 للعب مرة أخرى أو 0 للإلغاء")
    ثانية = input()

    if (ثانية == 1 ):
        run(word)
    else:
        return

def start_play():
    word = read_word()
    run(word)


if __name__ == '__main__':
    start_play()
