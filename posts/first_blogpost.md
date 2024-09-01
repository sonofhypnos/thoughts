---
title: Migrating From Lazyblorg to Python
date: 2024-08-30
---

Today I switched my blog away from [lazyblorg](https://github.com/novoid/lazyblorg). While I really liked the philosophy and the fact that I could just write a blogpost anywhere in my org files, I had become frustrated with all the features I couldn't use in lazyblorg, like footnotes. I then asked claude to write me a simple blogging site with markdown which taught me that python actually already has markdown support in it's standard library. So parsing markdown for a blogpost turned out as easy as:

```python
md = markdown.Markdown(extensions=["meta", "footnotes", "fenced_code"])
html = md.convert(content)
return html, md.Meta
```

where the metadata currently only contains the title and the date of the blogpost.

Another reason I decided to switch to markdown, is that it would make it easier to manually post my writing on lesswrong as well as here (since I can just paste the markdown into the editor on lesswrong). Sure I could connect my blog to my lesswrong account via RSS, but I think I like having only writing more "important" things as full blogposts on lesswrong and writing lots of small post on my main blog and then maybe posting them as a shortform on lesswrong. [Here]((https://raw.githubusercontent.com/sonofhypnos/thoughts/63ac38e2525e58042232fb7cf79c303b41c36eff/generate_blog.py)) is the full source file as of me writing this post and [here](/generate_blog.py) is the current one (if it still exists). I am currently using jinja for convenience for the templates, but maybe I decide later I want python as my only dependency.



