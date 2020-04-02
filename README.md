# WikipediaRevisionMiner

WikipediaRevisionMiner (WRM) is a toolkit used for mining Wikipedia articles'
revision history.

### Basic usage

```python
from revision_history import RevisionHistory

language = 'is'
RH = RevisionHistory(f'{language}', 'Knattspyrna')
for sentence_pair in RH.make_pairs():
    print(sentence_pair)
```
