# wikipedia-revision-miner

### Basic usage

```python
from revision_history import RevisionHistory
language = 'is'
R = RevisionHistory(f'{language}', 'Knattspyrna')
for w in R.make_pairs():
    print(w, '\n'*2)
```
