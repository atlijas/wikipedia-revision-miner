# Wikipedia Revision Miner

WikipediaRevisionMiner (WRM) is a toolkit used for mining Wikipedia articles'
revision history. Additional regular expressions to [rev_regex.py](rev_regex.py) are needed
in order to use WRM for other languages than Icelandic. Apart from that, it's
language independent.

### Basic usage

```python
from revision_history import RevisionHistory

language = 'is'
RH = RevisionHistory(f'{language}', 'Knattspyrna')
for sentence_pair in RH.make_pairs():
    print(sentence_pair)
```
