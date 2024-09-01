---
title: Vyvanse Metabolism
tags: ["medication", "biology"]
id: "vyvanse-half-life"
date: 2024-08-21
---

Things I learned that surprised me from a deep dive into how the medication I've been taking for years (Vyvanse) actually gets metabolized:

*   It says in the instructions that it works for 13 hours, and my psychiatrist informed me that it has a slow onset of about an hour. What that actually means is that after ~1h you reach 1/2 the peak concentration and after 13 hours you are at 1/2 the peak concentration again, because the half-life is 12h (and someone decided at some point 1/2 is where we decide the exponential starts and ends?). Importantly, this means 1/4 of the medication is still present the next day! ![Simple model](https://i.imgur.com/0aW9ktd.png)

Here is some [real data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4823324/), which fit the simple exponential decay rather well (It's from children though, which metabolize dextroamphetamine faster, which is why the half-life is only ~10h) ![real data](https://i.imgur.com/JGxS46s.jpeg)

*   If you eat ~1-3 grams of baking soda, you can make the amount of medication you lose through urine (usually ~50%) go to 0[^1] (don't do this! Your body probably keeps its urine pH at the level it does for a reason! You could get [kidney stones](https://en.wikipedia.org/wiki/Kidney_stone_disease)). 
*   I thought the opposite effect (acidic urine gets rid of the medication quickly) explained why my ADHD psychologist had told me that the medication works less well combined with citric fruit, but no! [Citric fruit actually increase your urine pH (or mostly don't affect it much)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428529/)? Probably because of the [citric acid cycle](https://en.wikipedia.org/wiki/Citric_acid_cycle) which means there's more acid leaving as co2 through your lungs? (I have this from gpt4 and a rough gloss over details checked out when checking Wikipedia, but this could be wrong, I barely remember my chemistry from school)
*   Instead, Grapefruit has some ingredients known to inhibit enzymes for several drugs, including dextroamphetamine (I don't understand if this inhibitory effect is actually large enough to be a problem yet though)
*   This brings me to another observation: apparently each of these enzymes is used in >10-20% of drugs: ([CYP3A4/5](https://en.wikipedia.org/wiki/CYP3A4), [CYP2D6](https://en.wikipedia.org/wiki/CYP2D6), [CYP2C9](https://en.wikipedia.org/wiki/CYP2C9)). Wow! Seems worth learning more about them! CYP2D6 gets actually used twice in the metabolism of dextroamphetamine, [once for producing and once for degrading an active metabolite](https://en.wikipedia.org/wiki/Dextroamphetamine#Pharmacokinetics). 
![Amphetamine](https://i.imgur.com/GUEXWbM.png)

Currently still learning more about basics about neurotransmitters from a textbook, and I might write another update once/if at the point where I feel comfortable writing about the effects of dextroamphetamine on signal transmission.

[^1]: [Urinary excretion of methylamphetamine in man](https://sci-hub.st/https://www.nature.com/articles/2061260a0) (scihub is your friend)
