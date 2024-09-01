---
title: "An Example Blog Post"
tags: ["lazyblorg", "software"]
id: "2017-07-17-example-posting"
---

Documentation:
==============

What is the name of the Directory of my blog?
---------------------------------------------

How to write new blog entry:
----------------------------

Example workflow for creating a blog entry

write a blog entry anywhere in your Org-mode files With lazyblorg, you
can, e.g., write a blog article about an event as a sub-heading of the
event itself! tag your entry with :blog: add an unique ID in the
PROPERTIES drawer You might want to use a package that automatically
generates unique IDs to your headings (I don't). You might want to take
a look at this solution using file or directory variables. set the state
of your entry to DONE make sure that a :LOGBOOK: drawer entry will be
created that contains the time-stamp

An example blog entry looks like this:

[DONE]{.done .DONE} An Example Blog Post [[blog]{.smallcaps}]{.tag tag-name="blog"} [[lazyblorg]{.smallcaps}]{.tag tag-name="lazyblorg"} [[software]{.smallcaps}]{.tag tag-name="software"} {#an-example-blog-post id="2017-07-17-example-posting" created="[2017-06-17 Sat 23:45]"}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\[...\] Today, I found out that I still don\'t know how to create a
valid Blogpost with lazyblorg

That's it. lazyblorg does the rest. It feels like magic, doesn't it? :-)
