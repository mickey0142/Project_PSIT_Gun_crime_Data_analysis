"""076: Run Length Encoding: 2012"""
def main():
    """Encoding string"""
    word = input() + " "
    cou = 0
    text1 = word[0]
    text2 = word[0]
    for i in word:
        text1, text2 = text2, i
        if text1 == text2:
            cou += 1
        else:
            print(str(cou) + text1, end = "")
            cou = 1

main()
