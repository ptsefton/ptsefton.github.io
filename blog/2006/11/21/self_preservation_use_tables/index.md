---
Title: "Adventures in self preservation: Use tables!"
Slug: self_preservation_use_tables
Date: 2006-11-21

---
<div>

I regulary remind youse all to [use
styles](http://del.icio.us/ptsefton/ptsefton+usestyles) here. Styles
make your life easier and improve document longevity by making it much
easier to update old documents like I'm doing in my [Adventures in self
preservation
series](http://del.icio.us/ptsefton/ptsefton+selfpreservation).

And here's another bit of advice. Use tables for any tabular
information. NOT TABS.

Got that? Don't use tabs or spaces in a word processor to line stuff up.
(It's a different matter if you're working with plain-old text).

1.  It's a hassle to use tabs for any but the most trivial tasks.

2.  Slight changes to your text, or to margins can blow up your
    formatting.

3.  Future versions of your word processing software may not reproduce
    things exactly as you intended – maybe the font you used is not
    available and one with slightly different character spacing gets
    used.

4.  There are no tabs on the web, so there is no way to publish tabbed
    data in HTML without converting it to tables (which may take some
    human intervention) or using PDF.

Tables on the other hand describe the structural relationships in the
data, and things don't get out of alignment when you add and subtract
characters. Sometimes all you need is a two by two table with no
borders. There are ways to add lots of semantic information your table
to show which bits are headers and so on, but even without that tables
are waaaaay better than tabs.

Here's an example from my honours thesis, that I'm [converting into an
ICE document](http://del.icio.us/ptsefton/ptsefton+selfpreservation) as
part of the [ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm)
project. It's a bit of linguistic analysis, using [Systemic Functional
 linguistics](http://en.wikipedia.org/wiki/Systemic_linguistics).

As it appeared in the original document, I used a table for the
analysis, and a monospaced font for the text . My 16-years-ago self was
pretty smart, but not surprisingly was not smart enough to anticipate
that in the year 2006 and I would want to put the thing on the web. I
think that the tables in that version of Word for the Mac (maybe 4?)
were pretty basic, they certainly had no cell merging, and maybe even
had to have all the columns the same width, so maybe I was unable to
find a nice way to format using tables all the way.

Even opening the Word file in a more modern version of  Word stuffs-up
the formatting. True, some things are messed-up within tables but they
are very easy to fix by re-sizing cells. Much easier than repairing
hand-spaced stuff with tabs or spaces.

So here's one of my examples, with spaces for formatting, using ICE.
(ICE uses OpenOffice.org writer to convert documents, and its behaviour
when exporting is that if you use more than one space it make
non-breaking spaces for you – we should probably change that).

This             is a cat              isn’t      it

<div class="Table48" align="left">

+--------------+--------------+--------------+--------------+--------------+--------------+
| Mood         |              | Residue      |              | Moodtag      |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Subject      | Finite       |              |              | Tagfinite    | Tagsubj.     |
+--------------+--------------+--------------+--------------+--------------+--------------+

</div>

What I really meant was:                 

<div class="Table49" align="left">

+--------------+--------------+--------------+--------------+--------------+--------------+
| This         | is           | a cat        |              | isn’t        | it           |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Mood         |              | Residue      |              | Moodtag      |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Subject      | Finite       |              |              | Tagfinite    | Tagsubj.     |
+--------------+--------------+--------------+--------------+--------------+--------------+

</div>

</div>
