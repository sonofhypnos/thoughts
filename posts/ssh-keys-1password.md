---
title: "Backing up ssh-keys"
tags: []
id: "ssh-keys-1password"
created: "2024-05-21"
---

[DONE]{.done .DONE} Backing up ssh-keys [[blog]{.smallcaps}]{.tag tag-name="blog"} {#backing-up-ssh-keys}
==================================================================================

After watching this [excellent video on more advanced and new things in
git](https://www.youtube.com/watch?v=aolI_Rz0ZqY), I decided to setup
signing my git commands through ssh.

That is easily done through:

``` {.bash org-language="sh"}
ssk-keygen -f ~/.ssh/git
git config --global commit.gpgsign true
git config --global user.signingkey ~/.ssh/git
```

Next I got a bit concerned though, because so far I had always just
taken for granted that I might loose my ssh-keys if I start using a
different device. I have backups and all, but it seemed prudent to put
these into my password Manager also (I use 1password, because I started
with that, but today I\'d probably choose bitwarden instead as it\'s
open source).

You can add your ssh-key programmatically to 1password like so:

``` {.bash org-language="sh"}
op item create --category=ssh-key --title="$key_name" \
    --vault='Private' --session="$OP_SESSION" \
    "Keys.private[password]=$private_key_content" \
    "Keys.public[concealed]=$public_key_content"
```
