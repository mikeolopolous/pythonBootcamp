import pandas as pd


student_data_frame = pd.read_csv("./nato_alphabet/nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

word = input("Enter a word: ").upper()
result = [nato_alphabet[letter] for letter in word ]
print(result)
