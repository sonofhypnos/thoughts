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
- [ ] checkout how gwern is doing his link repository would be really interesting.
- [ ] https://github.com/gwern/archiver-bot could be useful for archiving my stuff?
- [ ] Improve design
- [ ] add page feature where you can see the original markdown file
