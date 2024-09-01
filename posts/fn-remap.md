---
title: "Remaping the Fn key on my keyboard"
tags: ["linux", "keyboard"]
id: "fn-remap"
created: "2023-10-22"
---

[DONE]{.done .DONE} Remaping the Fn key on my keyboard [[blog]{.smallcaps}]{.tag tag-name="blog"} [[linux]{.smallcaps}]{.tag tag-name="linux"} [[keyboard]{.smallcaps}]{.tag tag-name="keyboard"} {#remaping-the-fn-key-on-my-keyboard}
=================================================================================================================================================================================================

Today I tried remapping the Fn-key on my keyboard after my Ctrl-key
stopped working reliably (I suspect it\'s a hardware issue). While I
first suspected this to not be possible at all, because a lot of
keyboards do not even send the Keypress Events from the Fn-keys to the
kernel, for my laptop keyboard this seems to have not been the case, as
I was able to see the keypresses with \"xev\". Next, I tried rebinding
the key with xmodmap using its keycode (151): xmodmap -e \'keycode 151 =
Control~L~\', but that did not work for mysterious reasons.

After some more failed attempts, I tried using setkeycodes, which
directly changes the map of the keyboard-driver to change which keycode
would be returned upon pressing the scan-codes sent by the keyboard.
Remapping the Fn key there did work, but for to me mysterious reasons,
the keycodes for setkeycodes are offset by 8, so I ran \"sudo
setkeycodes e063 29\" which successfully bound the key to keycode 37
according to xev when I ran it afterward. Apparently the keycodes sent
by kernel are different than the ones by xev.

Afterwards I realized I could have looked for the corresponding
[archwiki entry about keyboard
input](https://wiki.archlinux.org/title/Keyboard_input) long ago to get
an overview of how this roughly works on linux. It mentions
[complications like the
offset](https://wiki.archlinux.org/title/Keyboard_input#Identifying_keycodes_in_Xorg)
between kernel and Xorg keycodes.
