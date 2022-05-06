# sinefilcom-export

Export sinefil.com watched movies list.

Usage:

```
pip install scrapy
scrapy runspider sinefilcom_export.py -a {your sinefil.com username}
```

Exported file will be a csv with movie title and year. e.g:

```
Title,Year
Batman Begins, 2005
Vanilla Sky, 2001
...
```
