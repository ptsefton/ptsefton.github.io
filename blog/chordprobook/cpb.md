---
title: 'Scratching an itch: my software for formating song-sheets into, *gasp* PDF!'
date: 2015-11-10

---
[update:  2015-11-11 minor edits]

Summary: I made a [new open source program](https://github.com/ptsefton/chordprobook) to format song sheets in [chordpro](http://www.vromans.org/johan/projects/Chordii/chordpro/) format in a variety of ways. It's a command line thing. Not everyone understands; when I talk about it to my friends in [the band I sort of accidentally seem to have nearly joined](https://www.facebook.com/U4riaBand) we have IM exchanges like:

Me:

> I have it set up now with a cloud server watching the dropbox, so if you put in a text file with a .cho extension it will auto-generate a PDF for the song

Other band member:

> The what with the what now?

So, I decided to tell you all here on the Interwebs where you will 100% get what I'm talking about.

The problem was this: I had several years worth of song-sheets downloaded from various places on the internets or typed out by hand, for my own and other people's songs, in a variety of formats, including Word docs, RTF and PDF but mostly text files. Then I started playing music with other people again for the first time in years, and we'd be trading bits of paper and files and mailing song files to each other, and so on, always searching for a fourth-generation photocopy of something someone had in their folder. Anyway, I got to looking at ways to manage this and create consistently formatted song sheets.

Turns out there's a handy format for marking-up songs called chordpro. This involves putting chord names in square brackets, inline, in amongst the lyrics. Like [C] this. Or [G#maj7] or this, with a {title: } at the top, and a few other simple commands. Here's one I prepared earlier.

```
{title: Universe}
{st: Peter Sefton}
{key: C} 
{transpose: -3} 

[C] This is a song about [E7] everything
[F] It's really div[C]erse
[Caug9]Got something for [E7] everyone
[Am] But only [G] has one [F] verse
[F] Get it? Uni [D] Verse

{c: Pre chorus}
[D7] Here comes the chorus:

{soc}
{c: Chorus}
[C] Uni [E7] verse Uni [F] verse
[F] Uni [Fm] verse Uni [C] verse
{eoc}

{sob}
{c: Bridge}
[C] That's [G] it
{eob}

{c: Coda}
[F] Sorry the song's [C] so terse

```

There are lots of software packages for managing chordpro songs, printing them out, showing them on your church projector, organising them on your iPad, transposing them between keys and so on, but none of the software did quite what I wanted in the way I wanted. For example, most of the packages are designed to put chords above the lyrics, but I prefer leaving the chords inline, the way Rob Weule did it in the [Ukulele Club Songbook] and [Richard G](http://www.scorpexuke.com/ukulele-songs.html) does it in his Ukulele songs, it's more compact for one thing not to mention easier to copy and paste. Here's an example of some free software online which is really well done, but not what I wanted at all:

![A nice online chordpro converter at ukegeeks.com][geeks]

I've been keeping my songs in text files in Dropbox for years and that suits me. I don't want to have to suck all the files in to the maw of some slightly dodgy open source Java application on my laptop, or upload them somewhere, or install a web application, and it hurts me to say this after all the work I put into scholarly publishing in HTML but PDF is perfect for songs which are page-based, good for printing and good for displaying on tablets.

And I like to keep my hand in with coding and, well, I have a few hours on the train every day which I don't always use for work stuff and, you can probably see where this is heading. I got to wondering what would happen if I ran a few songs through [Pandoc], the magnificent omniverous document conversion tool to make PDF and HTML versions, and one thing led to another. It started innocently enough with a simple script to process chordpro declarations into [markdown](http://www.infoq.com/news/2014/09/markdown-commonmark). But then I asked myself; how would this look as an epub ebook made up of multiple songs? And then how do I make a word doc with a table of contents and start each song on a new page? And how might I get the script to make the songs scale (pun intended) so they fill up the page, for maximum readability? Which led to experiments with [LaTeX](https://en.wikipedia.org/wiki/LaTeX), the taste of which I still don't have out of my mouth entirely, and a brief flirtation with the Open Document Format and the LibreOffice presentation software (we've dated before but it has never worked out long-term). I finally got friendly with an amazing bit of command line software called [wkhtmltopdf] which can turn HTML web pages into PDF *including* running any javascript they contain before doing so. This way I was able to write a script that automatically scaled up text to fit an A4 page.

I told myself "I'm not going to do chord grids", you know, little images with fret-dots etc, cos me and my music buddies are all awesome players who know every chord ever, and if not can like totally work them out in our heads, but then I wondered if there was an existing open source library that did chords for multiple instruments I could just, like, drop in to my Python program so I could re-learn the banjo chords I've forgotten, and learn a bit more mandolin, and it turned out that there isn't really, but a I used a few train trips and a hot saturday arvo to write a chord-grid-drawer. Turns this chord definition I got from the open source software at [Uke Geeks] (thanks Buz!):

```{define: Aaug frets 2 1 1 4 fingers 2 1 1 4 add: string 1 fret 1 finger 1 add: string 4 fret 1 finger 1}```

Into this:

<div style="text-align: center">

**Aaug**

<img width='80' height='100' alt='Aaug' src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABkCAIAAACemCBBAAAB+0lEQVR4nO2a3ZKDIAyFyc6+t+6TZy/YMi4gJIpt/r6rTntQjwRMGgERkye+Pn0B7yYMWycMWycMWycMW+ebO+AH4InruMPGShaRyc4cIk3vLqTDsHXCsHXCsHXcGQYkpynwP8eaDpSm/xtF0cF5OtkdLk1/ZB7Sx6Pn7Gx8bmn6CmrxQI98mfrCZIbLDQOAs5t3/F6avsXdLs2uh7twi+Sn9QMmu3R3629jphxEmr7lyqZ1dhrJ+sL8OTw9EPfB8GZ9hbtNa254fMPaX6XpK9zl0oyQrv4lVKfPxBq2DiPTKmtmB0g30vfPQjLcffSBTtu8epj7q0AYIX2W0OqCWg8f81VuricK6gzrcjVgTXm4r74sFtvC/nCr5B5kV9ofxtfc5mGMOyqMiWFsJnmqEY67TWt9PSwc0gxjb3NWZzXzYD0sE3flYRi2Thi2Thi2Thi2DqPVkokXxJXp3YV0GLZOGLZOGLaOO8NrXj38CNca9CoN32nQ6wvpmw16fYYrcoZM1yszTGkGmH1BHBEvdLyU1cP76wMe2reJ1QZiFZMX6s+1+sFlE02pfCylk7dtKChbw0hYgGON1hkucPctZTOcbjfoVc5wd91Soj1pnOFCtasTRyk2fI0wbJ0wbJ0wbJ0wbB1lfwB02TgW2Ia14y6kw7B1wrB13Bn+BUpG28tPtaJCAAAAAElFTkSuQmCC' />
</div>

Unlike most chord drawing software I found which has built-in limitations, It will also cheerfully render a really silly chord  like this, which would require twelve strings, and 33 playable frets, not to mention 11 fingers, like that the dude in [one fish two fish red fish blue fish](http://trove.nla.gov.au/work/6838507) by Dr Seuss:

> Say!
>
> Look at his fingers!
>
> One, two, three…
>
> How many fingers
>
> Do I see?
>
>
> One, two, three, four,
>
> Five, six, seven,
>
> Eight, nine, ten.
>
> He has eleven!
>
> Eleven!
>
> This is something new.
>
> I wish I had
>
> Eleven, too! 


```{define: F#stupid base-fret 22 frets 1 2 3 x 4 5 6 7 8 9 10 11 fingers 11 10 9 8 0 7 6 5 4 3 2 1}```

<div style="text-align: center">
**F#stupid**

<img width='240' height='220' alt='F#stupid' src='data:image/png;base64,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' />
</div>

So, I had the technology to render chords (even at grand piano scale) but then it turned I couldn't find chord definition files for more instruments. There are lots of chord charts in image formats, of course, but no data that I can find, which led to working out how to compile [this old C code](http://sniff.numachi.com/~rickheit/chord/ch/) and modify it a bit to produce chord-data files (my update to that code is not done enough to release).

Anyway, the above song looks like this when run through *my* software. Now, after a couple of months of part-time tinkering in I can type ```./chordprobook.py -o --instrument Uke uni-verse.cho``` and this appears!

![Uni-verse rendered for printing](/blog/chordprobook/uni-verse.cho_key_C_uke.png)

Better yet, *I have it set up now with a cloud server watching the dropbox, so if you put in a text file with a .cho extension it will auto-generate a PDF for the song*. That is, in our shared band folder in Dropbox, if anyone creates a new song file, a new PDF appears automagically about a second later. Drop me a line if you'd like to try it - all you have to do is share a Dropbox folder with an account of mine. This is one of my favourite deployment patterns for software, almost like a no-interface user-interface. I'll write more about this matter soon.

Along the way I learned:

*  How to make [books], by feeding in a [list of files].
*  How to make a [setlist book] for a performance complete with additional performance notes, from a [markdown file].
*  That even when we had a setlist book my bandmates typed up setlists in big writing to put on the floor, so I added a feature to write out set-per-page at the start of the book.
*  That we really need the ability to do per-performance annotations, such as who goes first and whether we have a count-in or all-in approach to the song, so notes from the setlist such as *go slow* get put at the top of each song.
*  How to keep two page songs on facing pages in said books so you don't have to turn pages.
*  How to generate chord-definitions for arbitrary instruments (still working on that bit).
*  How to transpose chord definitions from one instrument to another if they have the same *relative* tuning between strings - eg soprano uke chords into baritone uke, or open-G  banjo tuning into the C tuning used by my baby banjo, the Goldtone Plucky.
*  How to make stand-alone one page versions of songs ...
*  .. automatically, whenever I drop a new on in my Dropbox, or change one.

Now, I realise that a command line thing that's a hassle to install and will almost certainly break the moment someone other than me tries to run it has limited appeal, but I'm [releasing it to the world anyway](https://github.com/ptsefton/chordprobook/). Even if the software is not to your taste, I think some of the things I've done will be useful to others. For example I:

* Liberated Buz Carter's chord definitions for Soprano uke which were encoded in a [javascript program] into a [stand alone file], observing the license conditions of the software of course.
* Likewise liberated the [guitar chords] from the venerable [chordii] software.
* Generated chord definitions for 5 string [banjo] G-tuning and [mandolin]; these may not be the best voicings or fingerings as they were auto-generated - let me know if you can help improve them.

# The future
Here are some other things I am Never Ever Going To Do With This Software. Ever. Never. Absolutely promise.

*  It will never have a Graphical User Interface.

*  It will never be a web application.

*  It will never be a dot-com startup.

* It will never be an iOS app.


# Help?

If anyone wants to help we could:

* Build a decent library of chord shapes defined in chordpro format

* Improve the look of the generated books a lot, if anyone knows some modern HTML and CSS.

* Make it better.


[Pandoc]: http://pandoc.org

[list of files]: https://github.com/ptsefton/chordprobook/blob/master/samples/sample-book.txt
[books]: https://github.com/ptsefton/chordprobook/blob/master/example_output/sample-book.pdf
[setlist book]: https://github.com/ptsefton/chordprobook/blob/master/example_output/setlist.pdf
[markdown file]: https://raw.githubusercontent.com/ptsefton/chordprobook/master/samples/setlist.md
[wkhtmltopdf]: http://wkhtmltopdf.org/

[Uke Geeks]: http://ukegeeks.com/

[geeks]: /blog/chordprobook/geeks.png

[Ukulele Club Songbook]: http://katoombamusic.com.au/product/ukulele-club-songbook/

[javascript program]: https://github.com/buzcarter/UkeGeeks/blob/7bca97b47dd149fab892f8b81c29c3fa782eec09/src/js/scriptasaurus/ukeGeeks.definitions.sopranoUkuleleGcea.js

[stand alone file]: https://github.com/ptsefton/chordprobook/blob/master/chord_data/soprano_ukulele_chords.cho

[guitar chords]: https://github.com/ptsefton/chordprobook/blob/master/chord_data/guitar_chords.cho

[chordii]: http://sourceforge.net/projects/chordii/

[mandolin]: https://github.com/ptsefton/chordprobook/blob/master/chord_data/mandolin_chords.cho

[banjo]: https://github.com/ptsefton/chordprobook/blob/master/chord_data/5_string_banjo_g_chords.cho
