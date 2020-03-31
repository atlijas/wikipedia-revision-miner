"""
This module is intended to scrape Wikipedia articles' revision history
Contact: Atli Jasonarson (atlijas)
Email: atj9@hi.is
"""

import re
from itertools import chain
from difflib import SequenceMatcher
import warnings
from bs4 import BeautifulSoup
from mwclient import Site
import requests
# NLTK needs to do some upgrading. Ignore for now.
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
from nltk.tokenize import sent_tokenize, word_tokenize
from rev_regex import revision_regex
from string import punctuation



class RevisionHistory:
    """
    A class that covers a single Wikipedia article's revision history
    """
    def __init__(self, language='en', wiki_page=None, revision=True):
        self.language = language
        self.site = Site(f'{language}.wikipedia.org')
        self.wiki_page = self.site.pages[wiki_page]
        self.rev_ids = [rev['revid'] for rev in self.wiki_page.revisions()]
        self.newest = max(self.rev_ids)
        self.oldest = min(self.rev_ids)
        self.revision = revision

    def get_revision_divs(self):
        """
        Generates a tuple for every revision.
        Every tuple consists of revised/unrevised pairs.
        Some of them vary in length, which is accounted for in make_pairs()
        """
        url = f'https://{self.language}.wikipedia.org/w/index.php?title=\
        {self.wiki_page}&type=revision&diff={self.newest}&oldid={self.oldest}'
        page = requests.get(url, "html.parser")
        soup = BeautifulSoup(page.content, "html.parser")
        unrevised_divs = soup.find_all("td", attrs={"class": "diff-deletedline"})
        revised_divs = soup.find_all("td", attrs={"class": "diff-addedline"})
        if all(lst != [] for lst in [unrevised_divs, revised_divs]):
            yield list(chain(*self.formatted(revised_divs))), \
                  list(chain(*self.formatted(unrevised_divs)))


    def make_pairs(self):
        """
        Compares revised/unrevised sentences and returns the most similar
        ones as sentence pairs
        """
        for revised_gen, unrevised_gen in self.get_revision_divs():
            for sent in revised_gen:
                best_match = None
                best_match_score = 0
                for sent2 in unrevised_gen:
                    curr_score = SequenceMatcher(None, sent, sent2).ratio()
                    if curr_score > best_match_score:
                        best_match_score = curr_score
                        best_match = sent2
                if sent != best_match and best_match_score > 0.5:
                    yield sent, best_match, best_match_score
                else:
                    pass

    def formatted(self, div):
        """
        Removes the WikiText BeautifulSoup doesn't detect
        Has to be modified for non-Icelandic usage
        See: rev_regex.py
        """
        for sub_div in div:
            sub_div = sub_div.get_text()
            sub_div = re.sub(revision_regex, '', sub_div)
            if '' != sub_div != ' ':
                if self.revision:
                    yield sent_tokenize(sub_div)
                elif not self.revision:
                    if sub_div not in punctuation:
                        yield sub_div


if __name__ == '__main__':
    R = RevisionHistory('is', 'Nasismi')
    for w in R.make_pairs():
        print(w, '\n'*2)
