# Installation
Dependencies: python==3.10 and jinja. I use poetry for dependency management.

For installation run:
```
poetry install
```

# Running locally

To run and see the blog locally, run:

```
python -m http.server & firefox http://0.0.0.0:8000
```

# Todos

- [ ] think about alternative to RSS feed similar to here: https://github.com/gwern/gwern.net/issues/11
- [ ] archive external links like Gwern.net? (write it in a way that someone else would want to use it?)
- [ ] Improve design
- [x] automatically fix capitalization
- [ ] Add tags 
- [ ] add page feature where you can see the original markdown file
