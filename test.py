import csv
import random


def main():
    vocab_terms = []
    vocab_definitions = []
    answer_type = input("What language do you want to answer in?: ").strip().lower()

    with open("vocab.csv", 'r', encoding="utf-8") as vocab_file:
        vocab = csv.reader(vocab_file, delimiter=',')

        if answer_type == "english":
            vocab_terms = [rows[0] for rows in vocab]
            vocab_file.seek(0)
            vocab_definitions = [rows[1] for rows in vocab]
        elif answer_type == "japanese":
            vocab_terms = [rows[1] for rows in vocab]
            vocab_file.seek(0)
            vocab_definitions = [rows[0] for rows in vocab]

    while True:
        term_number = random.randint(1, len(vocab_terms))
        print(f"What is {vocab_terms[term_number]} in {answer_type.capitalize()}?")
        print(f"A. {vocab_definitions[term_number]}")
        print(f"B. {vocab_definitions[term_number + 3]}")
        print(f"C. {vocab_definitions[term_number + 2]}")
        print(f"D. {vocab_definitions[term_number + 1]}")
        answer = input("Enter Answer: ")

        if answer == "A":
            print("Correct!")
        else:
            print(f"Incorrect! the answer was: {vocab_definitions[term_number]}")
            break


if __name__ == "__main__":
    main()
