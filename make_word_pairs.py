from difflib import SequenceMatcher
from reynir.bincompress import BIN_Compressed

bin = BIN_Compressed()

def get_file(file):
    with open(file, 'r', encoding='utf-8') as infile:
        f = [line.strip().split('\t') for line in infile.read().splitlines()]
    return f

data = [w for w in get_file('data/revision_no_punct.txt') if len(w) == 2]

for sent_pair in data:
    unrev = sent_pair[0]
    rev = sent_pair[1]
    for unrevised_word in unrev.split():
        for revised_word in rev.split():
            word_similarity = SequenceMatcher(None,
                                              unrevised_word,
                                              revised_word).ratio()
            if 1 > word_similarity > 0.85:
                if (bin.lookup(unrevised_word) != [] != bin.lookup(revised_word)):
                    continue
                else:
                    print(unrevised_word, '\t', revised_word)
