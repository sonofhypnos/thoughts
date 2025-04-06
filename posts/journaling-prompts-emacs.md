---
title: Journal prompts in Emacs
tags: emacs
    journaling
id: "journaling-prompts-emacs"
date: 2022-01-30
---




While I enjoy journaling in Emacs and, asking oneself the same questions
every day becomes boring for me really quickly. My new solution is to
give myself a random prompt from a list of nice introspective questions
I stole from <https://clearerthinking.org>[^1] . This is pretty easily
implemented in Elisp [^2]:

``` {.elisp}
;list with your prompts
(setq custom/journal-prompts '("What is on your mind?"
                               "What did you achieve today?"
                               "What worried you today?"))
(defun custom/random-phrase ()
  "command to insert prompt at cursor"
    (interactive)
    (insert (seq-random-elt custom/journal-prompts)))
```

Happy random journaling!

Footnotes
---------

[^1]: If you are really curious, you can just take a look at [my
    config](https://github.com/sonofhypnos/emacs-config).

[^2]: In the beginning I had high aspirations by weighting how often I
    get to see a prompt by how useful it was, but this (at least so far)
    turned out to be an overengineered solution, because it's very easy
    to just generate a new prompt, so I did not bother with that in the
    end.
