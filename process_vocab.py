import csv


def process_vocab(file='vocab.csv', language='japanese'):
    """
    Function to parse vocab for implementation into the quiz.
    Creates two lists, one for vocab terms, one for their definitions
    Supports English terms, or Japanese terms
    :param file: the file to be parsed for vocab. should be a csv file with 2 columns
    :param language: decides which csv elements should be the term. if 'english' will return first input as term. if 'japanese' the second element is the term.
    :return: returns a list of two lists dividing the terms and their definitions
    """
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
