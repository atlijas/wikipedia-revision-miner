import re

revision_patterns = [
                    r"'{2,}",
                    r'\[\[[^\]]+\|',
                    r'(\[\[)|(\]\])',
                    r'(\[\[)|(\]\])',
                    r'<ref.*?\/ref>',
                    r'{{.*?}}',
                    r'==.*?==',
                    r'&lt;ref&gt;.*?&lt;/ref&gt;',
                    r'File:.*',
                    r'<ref.*?\/ref>',
                    r'ref.*?\/ref',
                    r'>.*?',
                    r'>{{.*',
                    r'>.*?<',
                    r'Flokkur:.*?',
                    r'flokkur:.*?',
                    r'Mynd:.*?',
                    r'<div.*?'
                    r'<br.*?',
                    r':[0-9]{1,}.*?'
                    r'[a-zA-Z]{2}:.*?'
                    r'•.*?'
                    ]
revision_regex = re.compile('|'.join([r for r in revision_patterns]))
