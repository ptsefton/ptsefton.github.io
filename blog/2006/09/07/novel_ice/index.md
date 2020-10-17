---
Title: "ICE for lady novelists"
Slug: novel_ice
Date: 2006-09-07

---
<div>

[Updated 2006-10-06: fixed spelling of Westerfeld]

This week Justine Larbalestier [tells you how to write a
novel](http://justinelarbalestier.com/blog/?p=398). That's not how I
wrote my 2.4 novels – but then mine were not publishable.

(“Competently written but lacking the excitement our readers expect”
said Mills & Boon. “You have not been successful” from the nice helpful
people at the Vogel prize, who were all about encouraging young writers
by giving them useful feedback.)

Obviously I'm in no position to comment on  Justine's advice, so I'd
like to comment on the technology.

Justine says:

> On that computer you need a word processing program. If you want to be
> compatible with the publishing industry it should be microsoft word.
> If you want a program that doesn’t make you froth with rage it should
> be anything other than microsoft word. (Sadly, I have gone with the
> rage-frothing option.) You’ll also need some kind of spreadsheet
> program which needn’t be compatible with anything else—it is for your
> eyes only.

Word aint so bad if you can get it set up right. The [ICE
project](http://ice.usq.edu.au/) is all about that; we started with
optimizing Word and OpenOffice.org Writer for courseware writing, and
the ICE-RS project will look at optimizing it for research. I reckon I
could use it for writing a novel without too much pain. But it was
helpfully explained to me at age 28 that I  am “not successful” as a
novelist so what would I know? Also I am unable to generate excitement.

Justine goes on to write about her husband Scott's method for managing a
book in a spreadsheet.

> At a glance I can see which pov was telling what chapter, what day it
> was, where they were, and who was getting the lion share of the novel.
> You can also have a content column that lets you know whether it’s a
> sitting-around-talking chapter (”) or a sitting-around-and-thinking
> (’) or an action-packed chapter (!) or somewhere in between (\^) or
> one with sex (\*).

This is a Good Idea.

What they do in the Westerfeld / Larbalestier household is keep metadata
about the parts of their books in a spreadsheet and use that metadata to
manage and plan the production process. I started wondering how this
could work with ICE. Instead of putting the metatada in a spreadsheet
why not attach the data to the documents themselves? Then you would go
to your ICE web-view of your novel and see an annotated table of
contents that showed which chapters are '“' and which are '!'.

(And why not add this information to the published version so people can
find the '\*'?)

I'm imagining that one would keep each chapter in a separate document
and use ICE to put the chapters in order using the `organize` feature
(making it trivially easy to change the order later). ICE watches what
you're doing and turns everything into HTML, which you may or may not
need. But ICE is good a presenting things in nice ways. How about little
icons for the protagonists so you can see who's point of view is where
in the novel?

While we're at it, how about:

1.  Automatically generated word counts.

2.  Dialogue to description ratio worked out by the computer.

3.  Ratings from first-readers – give them a form so they can enter
    comments but also simple star-ratings.

I'm imagining a dashboard view of the novel, with green and red lights
to show where the work is needed and suitable icons for Justine's
categories of  talking, thinking, doing and rooting.

Cameron Loudon and I have talked about this for research workflows. We
want to allow you to attach stuff to your documents about what journal
or conference you are targeting, deadlines etc and then let a management
system report to you about what you have due when. Or one could report
on the progress of a group in aggregate. Imagine how that would look at
Justine's place with two writers working on multiple fronts. Who's
novel's going better? Who has the most words per chapter?

Or for a thesis, you could look at metrics like how many quotations and
citations you have in each part, and ratings and comments from your
supervisor.

[ICE](http://ice.usq.edu.au/)also takes care of a couple of other things
for a writer, the main one being backups and version control. Here on
this blog for example I write on any one of a few computers, on a
'working copy' of all my stuff. When I hit the sync button it all gets
sent to a virtual server I rent somewhere in the USA. That server keeps
track of every version of everything I write.

(Justine – you do back stuff up, **don't you**?)

If I want to roll back to the state of my work on a particular day I
can. This gives great freedom to completely refactor a whole chapter to
see how it comes out and revert or roll back if it comes out wrong.

(There's a caveat here. ICE does not yet have features to do this, you
have to resort to using the Subversion system directly, or get someone
to set up a  web server application such as Trac that lets you browse
your old versions via the web. There is a nice Windows interface called
the [Tortoise](http://tortoisesvn.tigris.org/) for Subversion. And the
commandline works even better).

If you want to share a work in progress then your collaborators can hit
'sync' to get the latest snapshot. We're adding annotation and rating
services over the next year that should allow us do what Justine is
doing with her spreadsheet.

Using ICE you'd also get an HTML version of your book with all the
required navigation. Some novelists like to put their stuff up on the
web for anyone to read. ICE would make that really, really simple to do.

</div>
