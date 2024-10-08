---
title: Figuring out YASnippet
id: "figuring-out-yasnippet"
date: 2022-03-19
---




Today I finally took the time to figure to the YASnippet Emacs package
to create a template for my new blogposts. Turns out there was not a lot
to understand. To create a new template you run \`M-x\`
\`yas-new-snippet\`. In the then opening buffer you just enter your
template in plain text and hit \`C-c C-c\` when you're done.

The three other elements that I needed for my simple snippets:

-   \`\$0\` denotes where the cursor should end up after the snippet is
    inserted.

-   Emacs lisp code to be evaluated with the snipped can be inserted
    within backquotes. Example: the following snippet enters the current
    date in iso-format:

``` {.commonlisp org-language="emacs-lisp" tangle="yes"}
`(format-time-string "%Y-%m-%d")` $0
```

-   Elements to be completed at point are entered with {N: default
    value} as an example here is the template for a for-loop in C:

``` {.c tangle="yes"}
for (${1:i = 0}; ${2:i < N}; ${3:i++}) {
    $0
        }
```
