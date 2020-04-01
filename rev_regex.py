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
                    r'Mynd:.*?',
                    ]
revision_regex = re.compile('|'.join([r for r in revision_patterns]))
