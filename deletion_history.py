"""
This module is intended to scrape Wikipedia articles' revision history
Contact: Atli Jasonarson (atlijas)
Email: atj9@hi.is
"""

from itertools import chain
import warnings
from bs4 import BeautifulSoup
import requests
# NLTK needs to do some upgrading. Ignore for now.
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
from revision_history import RevisionHistory
from string import punctuation


class RevisionDeletions(RevisionHistory):
    """
    A subclass of RevisionHistory that only covers deleted parts of a Wikipedia
    article's revision histroy
    """

    def get_deletions(self):
        """
        Generates a tuple for every revision.
        Every tuple consists of deleted/added pairs.
        Some of them vary in length, which is accounted for in make_pairs()
        """
        url = f'https://{self.language}.wikipedia.org/w/index.php?title=\
        {self.wiki_page}&type=revision&diff={self.newest}&oldid={self.oldest}'
        page = requests.get(url, "html.parser")
        soup = BeautifulSoup(page.content, "html.parser")
        deleted_part = soup.find_all("del", attrs={"class": "diffchange diffchange-inline"})

        if deleted_part != []:
            return [w for w in chain(*self.formatted(deleted_part))
                    if w not in punctuation]


if __name__ == '__main__':
    RD = RevisionDeletions('is', 'Reddit')
    print([w for w in RD.get_deletions()])
