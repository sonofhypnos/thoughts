---
title: Software Setup
tags: linux 
id: computer-setup
date: 2025-10-14
---

Today I am writing about my software setup.

For the last 4 years, I have been using Linux. I switched from Windows to Linux in my first year as a computer science student when I was going through the material of [the missing semester](https://missing.csail.mit.edu/) CS course[^1]. When trying to install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux) to be able to use unix shell tools, I bricked my Windows version[^2] and then decided I might as well give Linux a try before I reinstall Windows.

Linux solved my issue with Windows, where I was disturbed to learn that Windows does not have shortcuts to move windows between screens. My computer science friends recommended I try a tiling window manager. They recommended I use [I3](https://i3wm.org/), so I tried that and have been hooked ever since. On Windows, I had essentially already been using all the window shortcuts, but the workflow was just so much smoother with i3.
I haven't been tempted to switch back ever since, except when I couldn't get Trackmania to work on my laptop (even though I had a friend with the exact same laptop and operating system who had it working on Steam).
I still use i3, but if not for switching costs, I would go with Xmonad instead, which is presumably easier to extend. I used to have all types of issues getting Bluetooth or audio to work when I was using i3, but essentially all of these issues were solved when I switched to using [Regolith](https://regolith-desktop.com/), which is an Ubuntu derivative that takes care of all the issues that come with using Gnome and i3 at the same time. 
One of my favourite features in i3 is the [Scratchpad](https://i3wm.org/docs/userguide.html#_scratchpad) (A small overlay window that you can make appear and disappear with 1 keyboard shortcut at any time). Pretty early after ChatGPT came out, I set up a scratch pad, so that I could have LLMs just 1 keyboard shortcut away:
![image](https://www.tassiloneubauer.com/images/scratchpad.png)
This probably tripled my LLM usage, which made me pretty competent at using them. Just like [googling](https://gwern.net/search), I think quick LLM queries to check things are underrated and yes, sycophancy is a problem, but leading queries can get you in trouble with Google or humans too and in practice, one of the main benefits other than better search I get from LLMs is them pointing out stupid errors I make.

In the early days, configuring [my dotfiles](https://github.com/sonofhypnos/dotfiles) for my operating system would take a lot of my time, but these days I rarely change things. By now, almost everything is configured just the way I like it :).

My editor of choice is Emacs, which I use in [Evil mode](https://github.com/emacs-evil/evil). I had started to use it after searching for a replacement for OneNote on Linux (OneNote didn't allow me to export my Notes!), and I was in search of software that had stood the test of time. I had always wanted to learn Lisp anyway, and Vim or Neovim weren't quite as configurable as I would have liked them to be. Learning to use all the shortcuts in Emacs and how to write Elisp to configure Emacs was a pretty steep learning curve in the beginning for the first 6 months, but now I feel comfortable and have no regrets. I have a separate [Scratchpad](https://i3wm.org/docs/userguide.html#_scratchpad) for Emacs as well, so that I can take notes on anything I am reading at any time.

I use Firefox for most of my daily browsing. The main reason I wouldn't want to switch to Chrome at this point is the browser extension [Tridactyl](https://github.com/tridactyl/tridactyl), which allows me to use [Vim shortcuts](https://www.youtube.com/watch?v=-txKSRn0qeA) not only for my window manager and my editor, but ALSO in my browser :). There's Vimium, but it is far inferior in its configurability and features.

For my shell I use Gnome Shell, which had more [latency]((https://danluu.com/term-latency/)) than I would like, when measured it, but all the other terminal I tried using had either issues with scrolling back in history or with text cutting off if I had the screen window in split-screen mode and even though I think there were ways to fix those issues I never really managed to properly configure them, so I am stuck with Gnome Shell for now.

[^1]: Highly recommended if you are a Computer Science student and you don't feel extremely comfortable with using the shell and shell tools, etc., yet.

[^2]: I learned that it was easier to install WSL when using the developer version of Windows, so I installed that. Once I had the developer version of Windows installed, I noticed that the entire UI in Windows is 10x slower on the developer version of Windows. The only way back to a fast version was to reinstall Windows.
