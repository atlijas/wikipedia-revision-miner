from sys import path
path.append('..')

def get_file(file):
    with open(file, 'r', encoding='utf-8') as infile:
        infile = infile.readlines()
    return infile

all_wikipedia_pages = get_file('data/all_is_wikipedia_articles.txt')
i = 0


with open('bla.txt', 'a', encoding='utf-8') as f:
    for page in all_wikipedia_pages:
        if page[0].isdigit():
            pass
        else:
            i += 1
            deletions = RevisionHistory('is', page.strip())
            print('[' + str(i) + '/' + str(len(all_wikipedia_pages)) + ']')
            try:
                for revised, unrevised, score in deletions.make_pairs():
                    f.write(unrevised + '\t')
                    f.write(revised + '\n')
                    f.flush()
            except:
                continue
