import pandas as pd


student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
