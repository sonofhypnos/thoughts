# Installation
Dependencies: python>=3.10 and jinja. I use poetry for dependency management.

For installation run:
```
poetry install
```

To install poetry and python, there is a shell.nix file in the root directory. You can use it to create a shell with the correct dependencies. To enter the shell run:
```
nix-shell
```

# Running locally

To run and see the blog locally, run:

```
nix-shell
poetry run python -m http.server & firefox http://0.0.0.0:8000
```

To run the jupyter-notebook run:

``` shell
nix-shell
poetry run jupyter-lab
```

# Pushing latest updates


To generate html files from the markdown files and to then publish the latest changes run:
``` shell
nix-shell
make all
```

To only generate html files run:





# Documentation
- to hide a blogpost, add "hidden" to the tags
- look at the blogpost `posts/example.md` to get an introduction to how blogposts are formatted.


## Markdown
[Markdown docs](https://python-markdown.github.io/index.html#python-markdown)
For anything related to markdown extensions (this includes the metadata headers) see:
[Markdown extension docs](https://python-markdown.github.io/extensions/)

# Todos

- [ ] thoughts on making this a general tool
  - [ ] I like having idiosyncratic things in here and I don't have to worry about supporting anything
  - [ ] my features are probably too idiosyncratic to be useful for other people.
 - [ ] in the header of the post, include a small link to the plane markdown form of the post (this should be easy.)
- [ ] Add rss feed
- [ ] think about alternative to RSS feed similar to here: https://github.com/gwern/gwern.net/issues/11
- [ ] update documentation: 
  - [ ] explain how to add tags properly
- [ ] Add a page where you can add small miscelaneous thoughts like the thoughts that you are having on configuration related things.
- [ ] archive external links like Gwern.net? (write the software in a way that someone else would want to use it?). There is a more general idea there, how you might want to handle the fact that it is difficult to write in a lot of different small and big formats right now and how you could handle this with language models. The first idea as I understand it is trying to distinguish when to trigger an RSS notification based on if the new change is a substantial or a small one.
- [ ] fix images that were created with imgur, which turns out to deprecate your images?
- [ ] add page 
- [ ] Improve design
- [ ] Add header to return to main page for notebooks also
- [x] automatically fix capitalization
- [ ] Add tags
- [ ] add page feature where you can see the original markdown file
- [ ] ask before commiting non-blog files
- [ ] support quotes in markdown better
