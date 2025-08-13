def first_non_repeating_letter(s):
    l_s = s.lower()
    for l_char in l_s:
        if l_s.count(l_char) == 1:
            npchar = s[(l_s.index(l_char))]
            return npchar
    return ""
while True:
    npchar = first_non_repeating_letter(input("Give a word: "))
    print(f"The first non repeating letter is: {npchar}")

