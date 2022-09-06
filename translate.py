# It is funny program that can translate english to japanese (actually it is not japanes LOL)

def from_eng_to_jap(txt):
    japnese = {
        'A': "ka", 'B': "tu", "C": "mi", 'D': 'te', 'E': 'ku', 'F': 'lu', 'G': 'ji',
        'H': 'ri', 'I': 'ki', 'J': 'zu', 'K': 'me', 'L': 'ta', 'M': 'rn', 'N': 'to',
        'O': 'mo', 'P': 'no', 'Q': 'ke', 'R': 'shi', 'S': 'ar', 'T': 'chi', 'U': 'do',
        'V': 'ru', 'W': 'ei', 'X': 'na', 'Y': 'fu', 'Z': 'zi'
    }
    translated = ''
    for ch in txt:
        translated += japnese.get(ch.upper(), ch).lower()
    return translated


def from_jap_to_eng(txt):
    english = {
        "ka": 'A', "tu": "B", "mi": "C", 'te': 'D', 'ku': 'E', 'lu': 'F', 'ji': 'G',
        'ri': 'H', 'ki': 'I', 'zu': 'J', 'me': 'K', 'ta': 'L', 'rn': 'M', 'to': 'N',
        'mo': 'O', 'no': 'P', 'ke': 'Q', 'shi': 'R', 'ar': 'S', 'chi': 'T', 'do': 'U',
        'ru': 'V', 'ei': 'W', 'na': 'X', 'fu': 'Y', 'zi': 'Z'
    }
    translated = ""
    i = 0
    while i < len(txt)-1:
        if txt[i:i+2] in english:
            translated += english[txt[i:i+2]]
            i += 2
            continue
        if txt[i:i+3] in english:
            translated += english[txt[i:i+3]]
            i += 3
            continue
        else:
            translated += txt[i]
            i += 1

    return translated


if __name__ == "__main__":
    prompt = """
1.To translate from English to Japanese
2.To translate form Japanese to English
Choice: """

    choice = int(input(prompt))
    txt = input("Enter Text to translate: ")
    if choice == 1:
        print(from_eng_to_jap(txt))
    elif choice == 2:
        print(from_jap_to_eng(txt).lower())
