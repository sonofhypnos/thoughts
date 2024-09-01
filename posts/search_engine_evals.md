---
title: Search Engine Evaluations are Underexplored
tags: ["LLM"]
id: "search-engine-evaluation"
date: 2024-03-6
---

While there is currently a lot of attention on assessing language models, it puzzles me that no one seems to be independently assessing the quality of different search engines and recommender systems. Shouldn't this be easy to do? 
The only thing I could find related to this is this [Russian site](http://www.analyzethis.ru/?lang=en&location=ru) (It might be propaganda from Yandex, as it is listed as the top quality site?). Taking their [“overall search quality”](http://www.analyzethis.ru/?page=1&analyzer=summary&interval=alltime&lang=en&location=en&view=) rating at face value does seem to support [the popular hypothesis](https://danluu.com/seo-spam/) that search quality of Google has slightly deteriorated over the last 10 years (although compared to 2009-2012, quality has been basically the same according to this measure). 
![Overall search result quality.](https://i.imgur.com/bbrcXfF.png)

The gpt-4 translated version of their blog states that they gave up actively maintaining this project in 2014, because search engine quality had become reasonable according to them:  
> For the first time in the history of the project, we have decided to shut down one of the analyzers: SEO pressing as a phenomenon has essentially become a thing of the past, and the results of the analyzer have ceased to be interesting.

> Despite the fact that search engine optimization as an industry continues to thrive, search engine developers have made significant progress in combating the clutter of search results with specially promoted commercial results. The progress of search engines is evident to the naked eye, including in the graph of our analyzer over the entire history of measurements:

![commercial results](https://imgur.com/QrJi08D.png)

> SEO Pressing Analyzer Graph

> The result of the analyzer is the share of commercial sites in the search results for queries that do not have a clearly commercial meaning; when there are too many such sites in the search results, it is called susceptibility to SEO pressing. It is easy to see that a few years ago, more than half (sometimes significantly more than half) of the search results from all leading search engines consisted of sites offering specific goods or services. This is, of course, a lot: a query can have different meanings, and the search results should cater to as many of them as possible. At the same time, a level of 2-3 such sites seems decent, since a user who queries "Thailand" might easily be interested in tours to that country, and one who queries "power station" might be interested in power stations for a country home.

If we are worried that current recommender systems [are already doing damage](https://www.lesswrong.com/posts/rKmojEZ9qKwApjCfX/the-gears-to-ascenscion-s-shortform#asBREKKKgH3vXDs9p) and expect things to get worse in the future, it might be good to actively monitor this to not get frog boiled.
