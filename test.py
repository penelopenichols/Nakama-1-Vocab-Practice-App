import csv

def main():
    with open("vocab.csv", 'r', encoding="utf-8") as vocab_file:
        vocab = csv.reader(vocab_file, delimiter=',')

        for line in vocab:
            print(line)

if __name__ == "__main__":
    main()
