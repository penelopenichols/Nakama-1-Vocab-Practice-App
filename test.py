from process_vocab import *

def main():
    #print(process_vocab(language='english'))

    vocab_terms = []
    vocab_definitions = []
    file = 'vocab.csv'
    language = 'japanese'

    with open(file, 'r', encoding="utf-8-sig") as vocab_file:
        vocab = csv.reader(vocab_file, delimiter=',')
        if language == "english":
            vocab_terms = [rows[0] for rows in vocab]
            vocab_file.seek(0)
            vocab_definitions = [rows[1] for rows in vocab]
        elif language == "japanese":
            vocab_terms = [rows[1] for rows in vocab]
            vocab_file.seek(0)
            vocab_definitions = [rows[0] for rows in vocab]
    print(vocab_terms)
    print(vocab_definitions)
"""
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
            """


if __name__ == "__main__":
    main()
