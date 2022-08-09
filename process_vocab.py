import csv


def process_vocab(file='vocab.csv', language='japanese'):
    vocab_terms = []
    vocab_definitions = []

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

    return [vocab_terms, vocab_definitions]
