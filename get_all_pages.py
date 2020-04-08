from mwclient import Site
language = 'is'
SITE = Site(f'{language}.wikipedia.org')
ALL_PAGES = SITE.allpages()

for page in ALL_PAGES:
    print(page.name)
