---
id: "lazyblorg-templates"
---

[DONE]{.done .DONE} Templates [[lb\_templates]{.smallcaps}]{.tag tag-name="lb_templates"} [[blog]{.smallcaps}]{.tag tag-name="blog"} {#templates created="[2014-12-26 Fri 16:09]"}
====================================================================================================================================

General elements
----------------

### Sidebar

```{=html}
<a id="show-sidebar-text" href="#show-sidebar">Show Sidebar</a>
<div class="sidebar toggle-sidebar">
   <div class="search">
     <iframe id="search-big" src="//duckduckgo.com/search.html?width=140&site=#DOMAIN#&prefill=Search%20blog"></iframe>
     <iframe id="search-narrow" src="//duckduckgo.com/search.html?width=70&k1=-1&k2=s&site=#DOMAIN#&prefill=Search"></iframe>
     <br/>
   </div>
   <ul>
   <li><a href="#BASE-URL#">Recent articles</a></li>
   <li>[[id:#ABOUT-PAGE-ID#][About this blog]]</li>
   <li>[[id:#HOWTO-PAGE-ID#][How to use this blog efficiently]]</li>
   <li><img src="#BASE-URL#/images/feed-icon-14x14.png" alt="RSS icon" />&nbsp;Subscribe to one of my feeds:
       <ul>
       <li><span style="font-size:small"><a href="#BASE-URL#/feeds/lazyblorg-all.atom_1.0.links-only.xml">links only feed</a> (most reliable)</span></li>
       <li><span style="font-size:small"><a href="#BASE-URL#/feeds/lazyblorg-all.atom_1.0.links-and-teaser.xml">article teaser feed</a></span></li>
       <li><span style="font-size:small"><a href="#BASE-URL#/feeds/lazyblorg-all.atom_1.0.links-and-content.xml">full content feed</a></span></li>
       </ul></li>
   <li><span style="font-size:small"><a href="https://en.wiktionary.org/wiki/TBD">TBD</a>: Per Tag Feeds</span></li>
   <li><span style="font-size:small"><a href="https://en.wiktionary.org/wiki/TBD">TBD</a>: Archive</span></li>
   <li>Top <a href="#BASE-URL#/tags/">tags</a>:
       <ul class="top-tags-list">
            #TOP-TAG-LIST#
       </ul></li>
   </ul>
</div>

```
### Sections

-   \#SECTION-TITLE\#: title of the next heading/section
-   \#SECTION-LEVEL\#: relative level of the next heading/section

```{=html}
<header><h#SECTION-LEVEL# class="section-title">#SECTION-TITLE#</h#SECTION-LEVEL#></header>

```
### Paragraph

-   \#PAR-CONTENT\#

```{=html}
<p>

#PAR-CONTENT#

</p>

```
### Lists

```{=html}
<ul>
```
-   \#CONTENT\#: text of the list item

```{=html}
<li>#CONTENT#</li>
```
```{=html}
</ul>
```
### Pre-formatted text

Without name/label:

```{=html}
<div class="example_code">
<pre>
```
```{=html}
  </pre>
</div>

```
With name/label:

```{=html}
<p>

    #NAME#
      <div class="example_code">
      <pre>
```
```{=html}
      </pre>
    </div>

</p>
```
### SRC blocks (not HTML)

Without name/label:

```{=html}
<div class="example_code">
<pre>
```
```{=html}
  </pre>
</div>

```
With name/label:

```{=html}
<p>

    #NAME#
      <div class="example_code">
      <pre>
```
```{=html}
      </pre>
    </div>

</p>
```
### HTML blocks

-   \#NAME\#: Org-mode name of the block

```{=html}
<p>

    #NAME#
      <div class="example_code">
```
```{=html}
      </div>

</p>

```
### QUOTE blocks

```{=html}
<blockquote>
```
```{=html}
</blockquote>

```
### Back-references

```{=html}
<div class="back-references"><hr /><p>Related articles that link to this one:</p>
  <ul>

```
```{=html}
<div class="back-references"><hr /><p>Ähnliche Beiträge, die hierher zeigen:</p>
  <ul>

```
```{=html}
<li>#REFERENCE#</li>

```
```{=html}
  </ul>
</div>

```
### Reading time indicators

```{=html}
<aside class="reading-time-section">
    Reading time is one minute
</aside>
```
```{=html}
<aside class="reading-time-section">
    Lesezeit ist eine Minute
</aside>
```
```{=html}
<aside class="reading-time-section">
    Reading time is #READINGMINUTES# minutes
</aside>
```
```{=html}
<aside class="reading-time-section">
    Lesezeit ist #READINGMINUTES# Minuten
</aside>
```
### ignore me

```{=html}
```
```{=html}
```
Persistent
----------

### Entry Page

1.  Header

    -   \#BLOGNAME\#: short name of the blog
    -   \#COMMON-SIDEBAR\# : the sidebar content which is shared on all
        pages
    -   \#ARTICLE-ID\#: Org-mode ID property of the blog entry

    ```{=html}
      <!DOCTYPE html>
      <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
      <meta charset="UTF-8">
      <meta name="author" content="#AUTHOR-NAME#" />
      <meta name="generator" content="lazyblorg" />
      <link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
            href="#CSS-URL#" type="text/css" media="screen"  />

      <link rel="alternate" type="application/atom+xml"
            title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
      <link rel="alternate" type="application/atom+xml"
            title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
      <link rel="alternate" type="application/atom+xml"
            title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

      <!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

      <title>#BLOG-NAME# - Homepage of #AUTHOR-NAME#</title>
      </head>

      <body class="persistent-body">

      <header class="persistent-header">

          <nav class="entrypage-article-header-nav">
            <span class="breadcrumbs">
              <img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"><span style="padding-top:1em;">
            </span>
          </nav>

      </header>

      #COMMON-SIDEBAR#

      <div class="entry-page-greetings">
      <p>

        This is the home-page of #AUTHOR-NAME#.

      </p>

      <p>

        On this page you can see the latest blog updates. For further articles, please use the <b>search bar</b> or <b>navigate through <a href="tags/">the blue tags</a></b>.

      </p>

      <p>


      </p>

      <p>
          <aside class="tag-cloud">
            <ul>

    #TAGOVERVIEW-CLOUD#

                </ul>
              </aside>
      </p>

      <p>

        Most recent articles or updates:

      </p>
      </div>

    ```

2.  Article-Preview

    -   \#ARTICLE-TITLE\#: heading/title of the blog article
    -   \#ARTICLE-URL\#: URL of the blog article
    -   \#ARTICLE-YEAR\#: four digit year of the article (folder path)
    -   \#ARTICLE-MONTH\#: two digit month of the article (folder path)
    -   \#ARTICLE-DAY\#: two digit day of the article (folder path)
    -   \#ARTICLE-PUBLISHED-HTML-DATETIME\#: time-stamp of publishing in
        HTML date-time format (e.g., `2011-10-30T15:00+02:00`)
    -   \#ARTICLE-PUBLISHED-HUMAN-READABLE\#: time-stamp of publishing
        in human readable format (e.g., `2011-10-30T15:00`)
    -   \#ARTICLE-TEASER\#: First lines up to the first heading or
        \<hr\>-element

    ```{=html}

    <article class="entry-page-article">
    ```
    ```{=html}
    <aside>
      <ul class="entry-page-article-tags">
    ```
    -   \#TAGNAME\#: string of a tag

    ```{=html}
    <li><a class="usertag" href="#BASE-URL#/tags/#TAGNAME#/">#TAGNAME#</a></li>

    ```
    ```{=html}
      </ul>
    </aside>
    ```
    ```{=html}
    <h1><a href="#ARTICLE-URL#">#ARTICLE-YEAR#-#ARTICLE-MONTH#-#ARTICLE-DAY#: #ARTICLE-TITLE#</a></h1>

    #ARTICLE-TEASER#

    ```
    ```{=html}
    <p>
    <a href="#ARTICLE-URL#" class="article-preview-more">Read the whole article&nbsp;...</a>
    </p>
    ```
    ```{=html}

    </article>


    ```

3.  Footer

    -   \#BLOGNAME\#: short name of the blog

    ```{=html}

        <footer>
          <p><i>[[id:#ABOUT-PAGE-ID#][#BLOG-NAME#]]</i> is authored in <a href="//orgmode.org">Org mode</a> and generated by <a href="https://github.com/novoid/lazyblorg">lazyblorg</a>

            &nbsp;&bull;&nbsp; <a href="//validator.w3.org/check/referer">HTML5</a>

            &nbsp;&bull;&nbsp; <a href="//jigsaw.w3.org/css-validator/">CSS3</a>

            &nbsp;&bull;&nbsp; <a href="https://web.archive.org/web/*/#DOMAIN#/">Archive</a>

            &nbsp;&bull;&nbsp; <a href="https://jeffhuang.com/designed_to_last/">Designed to Last</a>
          </p>
        </footer>

      </body>
    </html>
    ```

### Other Persistent Pages

1.  Header

    -   \#ARTICLE-TITLE\#: heading/title of the blog article
    -   \#ARTICLE-ID\#: Org-mode ID property of the blog entry

    ```{=html}
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta charset="UTF-8">
    <meta name="author" content="#AUTHOR-NAME#" />
    <meta name="generator" content="lazyblorg" />
    <meta name="orgmode-id" content="#ARTICLE-ID#" />
    <link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
          href="#CSS-URL#" type="text/css" media="screen"  />

    <link rel="alternate" type="application/atom+xml"
          title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
    <link rel="alternate" type="application/atom+xml"
          title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
    <link rel="alternate" type="application/atom+xml"
          title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

    <!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

        <title>#ARTICLE-TITLE#</title>

    </head>

    ```

2.  Top of Article

    -   \#BLOGNAME\#: short name of the blog
    -   \#ARTICLE-YEAR\#: four digit year of the article (folder path)
    -   \#ARTICLE-MONTH\#: two digit month of the article (folder path)
    -   \#ARTICLE-DAY\#: two digit day of the article (folder path)
    -   \#ARTICLE-PUBLISHED-HTML-DATETIME\#: time-stamp of publishing in
        HTML date-time format (e.g., 2011-10-30T15:00+02:00)
    -   \#ARTICLE-PUBLISHED-HUMAN-READABLE\#: time-stamp of publishing
        in human readable format (e.g., 2011-10-30T15:00)
    -   \#COMMON-SIDEBAR\# : the sidebar content which is shared on all
        pages

    ```{=html}
    <body>

      <div class="common-orgsource"><a href="source.org.txt">&#960;</a></div>

      <header>

        <nav class="persistent-article-header-nav">
          <span class="breadcrumbs">
            <a href="../"><img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"></a>
          </span>
        </nav>

    ```
    ```{=html}
      <h1 class="common-article-header-title">#ARTICLE-TITLE#</h1>

    #READING-MINUTES-SECTION#

    </header>

    #COMMON-SIDEBAR#

    <article class="common-article">

    ```
    ```{=html}
    </article>

    ```

3.  Footer

    ```{=html}
          <aside class="published-on">
            Published on <time datetime="#ARTICLE-PUBLISHED-HTML-DATETIME#">#ARTICLE-PUBLISHED-HUMAN-READABLE#</time>
          </aside>

       <p class="email-comment">
          <a href="mailto:#COMMENT-EMAIL-ADDRESS#?subject=#ARTICLE-ID#%20comment:%20&body=Please%20do%20not%20remove%20'#ARTICLE-ID#%20comment:'%20in%20subject%20and%20please%20tell%20me%20whether%20or%20not%20it%20is%20OK%20to%20add%20your%20comment%20and%2For%20your%20name%20and%2For%20your%20email%20address%20to%20the%20blog%20entry!">Comment via email</a> or via <a href="//disqus.com">Disqus</a> comments below:
       </p>

        <div id="disqus_thread"></div>
        <div id="disqus_loader" style="text-align: center">
          <!-- stolen from http://blog.yjl.im/2012/04/let-your-readers-decide-when-to-load.html -->
          <button onclick="load_disqus()">Load Disqus Comments</button>
          <script>
            function load_disqus()
            {
              var dsq = document.createElement('script');
              dsq.type = 'text/javascript';
              dsq.async = true;
              dsq.src = "//#DISQUS-NAME#.disqus.com/embed.js";
              var disqus_identifier = '#ARTICLE-ID#';
              (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
              var ldr = document.getElementById('disqus_loader');
              ldr.parentNode.removeChild(ldr);
            }
          </script>
        </div>
        <noscript>Please enable JavaScript to view the <a href="//disqus.com/?ref_noscript">Disqus comments.</a></noscript>

        <footer>
          <p><i>[[id:#ABOUT-PAGE-ID#][#BLOG-NAME#]]</i> is authored in <a href="//orgmode.org">Org mode</a> and generated by <a href="https://github.com/novoid/lazyblorg">lazyblorg</a>

            &nbsp;&bull;&nbsp; <a href="//validator.w3.org/check/referer">HTML5</a>

            &nbsp;&bull;&nbsp; <a href="//jigsaw.w3.org/css-validator/">CSS3</a>

            &nbsp;&bull;&nbsp; <a href="https://web.archive.org/web/*/#DOMAIN#/">Archive</a>

            &nbsp;&bull;&nbsp; <a href="https://jeffhuang.com/designed_to_last/">Designed to Last</a>
          </p>
        </footer>

      </body>
    </html>
    ```

Article
-------

### Header {#header-2}

-   \#ARTICLE-TITLE\#: heading/title of the blog article
-   \#ARTICLE-ID\#: Org-mode ID property of the blog entry

```{=html}
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">

<meta name="author" content="#AUTHOR-NAME#" />
<meta name="generator" content="lazyblorg" />
<meta name="description" content="#ARTICLE-TITLE#" />
<meta name="orgmode-id" content="#ARTICLE-ID#" />

<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@#TWITTER-HANDLE#" />
<meta name="twitter:creator" content="@#TWITTER-HANDLE#" />
<meta name="twitter:title" content="#ARTICLE-TITLE#" />
<meta name="twitter:description" content="#ARTICLE-TITLE#" />
<meta name="twitter:image" content="#TWITTER-IMAGE#" />

<meta property="og:type" content="article" />
<meta property="og:title" content="#ARTICLE-TITLE#" />
<meta property="og:description" content="#ARTICLE-TITLE#" />
<meta property="og:image" content="#TWITTER-IMAGE#" />
<meta property="og:site_name" content="#BLOG-NAME# - Web-page of #AUTHOR-NAME#">
<meta property="article:published_time" content="#ARTICLE-PUBLISHED-HTML-DATETIME#" />
<meta property="article:author" content="#AUTHOR-NAME#" />

<link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
      href="#CSS-URL#" type="text/css" media="screen"  />

<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

<!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

    <!-- link rel="stylesheet" type="text/css" href="../../../../style.css" / -->
    <title>#ARTICLE-TITLE#</title>

</head>
```
### Top of Article {#top-of-article-1}

-   \#BLOGNAME\#: short name of the blog
-   \#ARTICLE-YEAR\#: four digit year of the article (folder path)
-   \#ARTICLE-MONTH\#: two digit month of the article (folder path)
-   \#ARTICLE-DAY\#: two digit day of the article (folder path)
-   \#ARTICLE-PUBLISHED-HTML-DATETIME\#: time-stamp of publishing in
    HTML date-time format (e.g., 2011-10-30T15:00+02:00)
-   \#ARTICLE-PUBLISHED-HUMAN-READABLE\#: time-stamp of publishing in
    human readable format (e.g., 2011-10-30T15:00)
-   \#COMMON-SIDEBAR\# : the sidebar content which is shared on all
    pages

```{=html}
<body>

  <div class="common-orgsource"><a href="source.org.txt">&#960;</a></div>


  <header>

    <nav class="temporal-article-header-nav">
      <span class="breadcrumbs">
        <a href="../../../../"><img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"></a><span style="padding-top:1em;">&nbsp;&nbsp;&nbsp;&nbsp;&raquo;
        <a href="../../../">#ARTICLE-YEAR#</a>&nbsp;&ndash;&nbsp;<a href="../../">#ARTICLE-MONTH#</a>&nbsp;&ndash;&nbsp;<a href="../">#ARTICLE-DAY#</a></span>
      </span>
    </nav>

```
```{=html}
<aside class="common-tags">
  <ul>

```
-   \#TAGNAME\#: string of a tag

```{=html}
<li><a class="usertag" href="#BASE-URL#/tags/#TAGNAME#/">#TAGNAME#</a></li>

```
```{=html}
<li><a class="autotag" href="#BASE-URL#/tags/#TAGNAME#/">#TAGNAME#</a></li>

```
```{=html}
<li>#AUTOTAGLANGUAGELINK</li>

```
```{=html}
  </ul>
</aside>

```
```{=html}
    <h1 class="common-article-header-title">#ARTICLE-TITLE#</h1>

#READING-MINUTES-SECTION#

  </header>

#COMMON-SIDEBAR#

<article class="common-article">

```
```{=html}

</article>

```
### Footer {#footer-2}

```{=html}
      <aside class="published-on">
        Published on <time datetime="#ARTICLE-PUBLISHED-HTML-DATETIME#">#ARTICLE-PUBLISHED-HUMAN-READABLE#</time>
      </aside>

   <p class="email-comment">
      <a href="mailto:#COMMENT-EMAIL-ADDRESS#?subject=#ARTICLE-ID#%20comment:%20&body=Please%20do%20not%20remove%20'#ARTICLE-ID#%20comment:'%20in%20subject%20and%20please%20tell%20me%20whether%20or%20not%20it%20is%20OK%20to%20add%20your%20comment%20and%2For%20your%20name%20and%2For%20your%20email%20address%20to%20the%20blog%20entry!">Comment via email</a> or via <a href="//disqus.com">Disqus</a> comments below:
   </p>

    <div id="disqus_thread"></div>
    <div id="disqus_loader" style="text-align: center">
      <!-- stolen from http://blog.yjl.im/2012/04/let-your-readers-decide-when-to-load.html -->
      <button onclick="load_disqus()">Load Disqus Comments</button>
      <script>
        function load_disqus()
        {
          var dsq = document.createElement('script');
          dsq.type = 'text/javascript';
          dsq.async = true;
          dsq.src = "//#DISQUS-NAME#.disqus.com/embed.js";
          var disqus_identifier = '#ARTICLE-ID#';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
          var ldr = document.getElementById('disqus_loader');
          ldr.parentNode.removeChild(ldr);
        }
      </script>
    </div>
    <noscript>Please enable JavaScript to view the <a href="//disqus.com/?ref_noscript">Disqus comments.</a></noscript>

    <footer>
      <p><i>[[id:#ABOUT-PAGE-ID#][#BLOG-NAME#]]</i> is authored in <a href="//orgmode.org">Org mode</a> and generated by <a href="https://github.com/novoid/lazyblorg">lazyblorg</a>

        &nbsp;&bull;&nbsp; <a href="//validator.w3.org/check/referer">HTML5</a>

        &nbsp;&bull;&nbsp; <a href="//jigsaw.w3.org/css-validator/">CSS3</a>

        &nbsp;&bull;&nbsp; <a href="https://web.archive.org/web/*/#DOMAIN#/#ARTICLE-URL#/">Archive</a>

        &nbsp;&bull;&nbsp; <a href="https://jeffhuang.com/designed_to_last/">Designed to Last</a>
      </p>
    </footer>

  </body>
</html>
```
Tag Overview Page
-----------------

A single page which is used as template for
`example.com/tags/index.html`.

### Header {#header-3}

-   \#ARTICLE-TITLE\#: heading/title of the blog article
-   \#ARTICLE-ID\#: Org-mode ID property of the blog entry

```{=html}
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">

<meta name="author" content="#AUTHOR-NAME#" />
<meta name="generator" content="lazyblorg" />
<meta name="description" content="Tag overview page" />

<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@#TWITTER-HANDLE#" />
<meta name="twitter:creator" content="@#TWITTER-HANDLE#" />
<meta name="twitter:title" content="#BLOG-NAME# - tag overview page" />
<meta name="twitter:description" content="Tag overview page" />
<meta name="twitter:image" content="#TWITTER-IMAGE#" />

<meta property="og:type" content="article" />
<meta property="og:title" content="#BLOG-NAME# - tag overview page" />
<meta property="og:description" content="Tag overview page" />
<meta property="og:image" content="#TWITTER-IMAGE#" />
<meta property="og:site_name" content="#BLOG-NAME# - Web-page of #AUTHOR-NAME#">
<meta property="article:published_time" content="#ARTICLE-PUBLISHED-HTML-DATETIME#" />
<meta property="article:author" content="#AUTHOR-NAME#" />

<link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
      href="#CSS-URL#" type="text/css" media="screen"  />

<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

<!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

    <title>Tags of #BLOG-NAME#</title>

</head>
```
### Article Body

```{=html}
  <body>

    <header>

      <nav class="temporal-article-header-nav">
        <span class="breadcrumbs">
          <a href="../"><img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"></a><span style="padding-top:1em;">&nbsp;&nbsp;&nbsp;&nbsp;&raquo;Tags</span>
        </span>
      </nav>

    </header>

  #COMMON-SIDEBAR#

  <article class="common-article">

    <p>

    Tag cloud of all tags except «<a href="hardware">hardware</a>» and «<a href="software">software</a>» which are my most general tags.
    The bigger the tag, the more articles are tagged with it.
    <!-- Tag Cloud: FIXXME: legend explaining size and colour -->

    </p>

      <aside class="tag-cloud">
        <ul>

#TAGOVERVIEW-CLOUD#

            </ul>
          </aside>

  </article>

```
### Footer {#footer-3}

```{=html}
    <footer>
      <p><i>[[id:#ABOUT-PAGE-ID#][#BLOG-NAME#]]</i> is authored in <a href="//orgmode.org">Org mode</a> and generated by <a href="https://github.com/novoid/lazyblorg">lazyblorg</a>

        &nbsp;&bull;&nbsp; <a href="//validator.w3.org/check/referer">HTML5</a>

        &nbsp;&bull;&nbsp; <a href="//jigsaw.w3.org/css-validator/">CSS3</a>

        &nbsp;&bull;&nbsp; <a href="https://web.archive.org/web/*/#DOMAIN#/#ARTICLE-URL#/">Archive</a>

        &nbsp;&bull;&nbsp; <a href="https://jeffhuang.com/designed_to_last/">Designed to Last</a>
      </p>
    </footer>

  </body>
</html>
```
Tag Pages
---------

Pages that describe a tag. Corresponding Org-mode entries must have:

-   heading is a single word: the tag itself
-   tags `blog` and `lb_tag` set
-   `ID` set in properties
-   marked as `DONE`

### Header {#header-4}

-   \#ARTICLE-TITLE\#: heading/title of the blog article
-   \#ARTICLE-ID\#: Org-mode ID property of the blog entry

```{=html}
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">

<meta name="author" content="#AUTHOR-NAME#" />
<meta name="generator" content="lazyblorg" />
<meta name="description" content="Tag page for tag #ARTICLE-TITLE#" />
<meta name="orgmode-id" content="#ARTICLE-ID#" />

<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@#TWITTER-HANDLE#" />
<meta name="twitter:creator" content="@#TWITTER-HANDLE#" />
<meta name="twitter:title" content="#ARTICLE-TITLE#" />
<meta name="twitter:description" content="Tag page for tag #ARTICLE-TITLE#" />
<meta name="twitter:image" content="#TWITTER-IMAGE#" />

<meta property="og:type" content="article" />
<meta property="og:title" content="#ARTICLE-TITLE#" />
<meta property="og:description" content="Tag page for tag #ARTICLE-TITLE#" />
<meta property="og:image" content="#TWITTER-IMAGE#" />
<meta property="og:site_name" content="#BLOG-NAME# - Web-page of #AUTHOR-NAME#">
<meta property="article:published_time" content="#ARTICLE-PUBLISHED-HTML-DATETIME#" />
<meta property="article:author" content="#AUTHOR-NAME#" />

<link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
      href="#CSS-URL#" type="text/css" media="screen"  />

<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

<!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

    <!-- link rel="stylesheet" type="text/css" href="../../../../style.css" / -->
    <title>The Tag &laquo;#ARTICLE-TITLE#&raquo;</title>

</head>
```
### Top of Article {#top-of-article-2}

-   \#BLOGNAME\#: short name of the blog
-   \#ARTICLE-YEAR\#: four digit year of the article (folder path)
-   \#ARTICLE-MONTH\#: two digit month of the article (folder path)
-   \#ARTICLE-DAY\#: two digit day of the article (folder path)
-   \#ARTICLE-PUBLISHED-HTML-DATETIME\#: time-stamp of publishing in
    HTML date-time format (e.g., 2011-10-30T15:00+02:00)
-   \#ARTICLE-PUBLISHED-HUMAN-READABLE\#: time-stamp of publishing in
    human readable format (e.g., 2011-10-30T15:00)
-   \#COMMON-SIDEBAR\# : the sidebar content which is shared on all
    pages

```{=html}
<body>

  <div class="common-orgsource"><a href="source.org.txt">&#960;</a></div>


  <header>

    <nav class="temporal-article-header-nav">
      <span class="breadcrumbs">
        <a href="../../../../"><img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"></a><span style="padding-top:1em;">&nbsp;&nbsp;&nbsp;&nbsp;&raquo;<a href="../">Tags</a>&nbsp;&nbsp;&nbsp;&nbsp;&raquo;#ARTICLE-TITLE#</span>
      </span>
    </nav>

```
```{=html}
<aside class="common-tags">
  <ul>

```
-   \#TAGNAME\#: string of a tag

```{=html}
<li><a class="usertag" href="#BASE-URL#/tags/#TAGNAME#/">#ARTICLE_TITLE#</a></li>

```
```{=html}
<li><a class="autotag" href="#BASE-URL#/tags/#TAGNAME#/">#TAGNAME#</a></li>

```
```{=html}
  </ul>
</aside>

```
```{=html}
    <h1 class="common-article-header-title">Tag Page for the Tag "#ARTICLE-TITLE#"</h1>

  #READING-MINUTES-SECTION#

  </header>

#COMMON-SIDEBAR#

<article class="common-article">

```
```{=html}
<hr />

<p>
All articles tagged with #ARTICLE-TITLE# <span class="minor-contrast">(sorted by last update, oldest on top)</span>:
</p>

<p>
#TAG-PAGE-LIST#
</p>

</article>

```
### Footer {#footer-4}

I\'m re-using article-footer.

Day Overview
------------

FIXXME

Month Overview
--------------

### Header {#header-5}

-   \#BLOGNAME\#: short name of the blog
-   \#YEAR\#: four digit year
-   \#MONTH-LONGNAME\#: name of the month like \"January\" or
    \"February\"
-   \#MONTH-SHORTNAME\#: three letter name of the month like \"Jan\" or
    \"Feb\"
-   \#MONTH-TWODIGITNUMBER\#: number of the month like \"01\" or \"02\"

```{=html}
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">
<meta name="author" content="#AUTHOR-NAME#" />
<meta name="generator" content="lazyblorg" />
<link rel="stylesheet" title="#BLOG-NAME# Standard CSS Style"
      href="#CSS-URL#" type="text/css" media="screen"  />

<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (links only)" href="#FEEDURL_LINKS#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (article teasers)" href="#FEEDURL_TEASER#" />
<link rel="alternate" type="application/atom+xml"
      title="#BLOG-NAME# (full content)" href="#FEEDURL_CONTENT#" />

<!-- WARNING: This page is written in HTML5 and might not be displayed correctly in old browsers. -->

<title>#BLOGNAME#: #YEAR#-#MONTH-TWODIGITNUMBER#</title>
</head>

<body>

<article class="month-overview">

  <header>

    <nav class="month-overview-header-nav">
      <span class="breadcrumbs">
        <a href="../../"><img src="#BLOG-LOGO#" alt="#BLOG-NAME# logo" width="350" style="vertical-align:middle;"></a><span style="padding-top:1em;">&nbsp;&nbsp;&nbsp;&nbsp;&raquo;
        #YEAR#&nbsp;&ndash;&nbsp;#MONTH-TWODIGITNUMBER#</span>
      </span>
    </nav>

    <h1 class="article-title">#YEAR#-#MONTH-TWODIGITNUMBER#</h1>

  </header>

<p><ul class="month-body">

```
### Article-Link

-   \#ARTICLE-TITLE\#: heading/title of the blog article
-   \#ARTICLE-URL\#: URL of the blog article
-   \#ARTICLE-YEAR\#: four digit year of the article (folder path)
-   \#ARTICLE-MONTH\#: two digit month of the article (folder path)
-   \#ARTICLE-DAY\#: two digit day of the article (folder path)
-   \#ARTICLE-PUBLISHED-HTML-DATETIME\#: time-stamp of publishing in
    HTML date-time format (e.g., 2011-10-30T15:00+02:00)
-   \#ARTICLE-PUBLISHED-HUMAN-READABLE\#: time-stamp of publishing in
    human readable format (e.g., 2011-10-30T15:00)

```{=html}
<li><a href="#ARTICLE-URL#">#ARTICLE-YEAR#-#ARTICLE-MONTH#-#ARTICLE-DAY#: #ARTICLE-TITLE#</a></li>
```
### Footer {#footer-5}

-   \#BLOGNAME\#: short name of the blog
-   \#YEAR\#: four digit year
-   \#MONTH-LONGNAME\#: name of the month like \"January\" or
    \"February\"
-   \#MONTH-SHORTNAME\#: three letter name of the month like \"Jan\" or
    \"Feb\"
-   \#MONTH-TWODIGITNUMBER\#: number of the month like \"01\" or \"02\"

```{=html}
    </ul></p>
    </article>

    <footer>
      <p><i>[[id:#ABOUT-PAGE-ID#][#BLOG-NAME#]]</i> is authored in <a href="//orgmode.org">Org mode</a> and generated by <a href="https://github.com/novoid/lazyblorg">lazyblorg</a>

        &nbsp;&bull;&nbsp; <a href="//validator.w3.org/check/referer">HTML5</a>

        &nbsp;&bull;&nbsp; <a href="//jigsaw.w3.org/css-validator/">CSS3</a>

        &nbsp;&bull;&nbsp; <a href="https://jeffhuang.com/designed_to_last/">Designed to Last</a>
      </p>
    </footer>

  </body>
</html>
```
Year Overview {#year-overview created="[2016-11-16 Wed 21:33]"}
-------------

FIXXME
