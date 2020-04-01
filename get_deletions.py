from revision_deletions import RevisionDeletions

def get_file(file):
    with open(file, 'r', encoding='utf-8') as infile:
        infile = infile.readlines()
    return infile

all_wikipedia_pages = get_file('all_is_wikipedia_articles.txt')

i = 0
with open('deletions.txt', 'a', encoding='utf-8') as f:
    for page in all_wikipedia_pages:
        if page[0].isdigit():
            pass
        else:
            i += 1
            deletions = RevisionDeletions('is', page.strip())
            print('[' + str(i) + '/' + str(len(all_wikipedia_pages)) + ']')
            try:
                for word in deletions.get_deletions():
                    if not word[0] == '.':
                        f.write(word + ' ')
                        f.flush()
            except:
                continue
