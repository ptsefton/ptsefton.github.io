---
Title: "Balanced review of word processors? I don't think so."
Slug: wp_review
Date: 2007-02-19

---
<div>

I had seen this
[review](http://www.donationcoder.com/Reviews/Archive/WordProcs/) of
word processing software.

I skimmed this thing looking for:

1.  Evidence that it's credible.

2.  Something that might be news to us at the ICE project.

Found neither, so decided to ignore it.

But now that Simon Phipps, of Sun has [called
it](http://blogs.sun.com/webmink/) <span
class="spCh spChx201c">“</span>Excellent and balanced reviews of the top
three word-processors.<span class="spCh spChx201d">”</span> I thought
I'd go back and take another look.

First time through I missed this bit:

> Let us be clear: the choice is not between being able to interoperate
> with Microsoft <span class="spCh spChx2014">—</span> thanks to Novell
> and Corel doing interoperability work for them <span
> class="spCh spChx2014">—</span> or being stuck in some ODF ghetto,
> unable to read Microsoft documents. Everyone wants to interoperate.
> The question is how. The problem is Microsoft. The solution lies with
> Microsoft. It's 2007, and it's time that Microsoft followed the same
> standards everyone else, instead of insisting the world bend to their
> ways. Microsoft's OXML doesn't disrupt this propensity. It's not only
> unacceptable, but quite strange that even now we can't all freely
> share documents with one another, no matter what operating system we
> like to use. We can send each other email, read each others' blogs and
> websites, even if you are on Windows, I'm on Linux, and Uncle Fester
> is using OS X. Why isn't that the norm for everything? It ought to be.
> The bottleneck is Microsoft. FOSS software is happy to interoperate
> with any other software. Why won't Microsoft? That is the \$64,000
> question in 2007. All this only matters if you intend to use Microsoft
> Word. The good news is that there are many good alternatives.

This is not what I'd call balanced., or even self-consistent. The
paragraph starts out talking about interoperability being a problem
which of course it is, and ends with <span
class="spCh spChx201c">“</span>All this only matters if you intend to
use Microsoft Word. The good news is that there are many good
alternatives.<span class="spCh spChx201d">”</span> Well, no, as long as
there are significant numbers of people using Word then interoperability
matters. And while there are alternatives, this review doesn't convince
me that the author would know a good alternative when he saw one.

There's no advice here about how to get interoperability to work: [Use
styles](http://del.icio.us/ptsefton/usestyles)? Stick to a subset of
functionality? Save in a particular format? (If you want that advice [go
to the ICE website](http://ice.usq.edu.au/instructions/user_guide.htm).
You can use Word or Writer and share documents between them).

This 'review' has nothing much to offer. It doesn't look at simple
use-cases across all three. Like how do the various word processors
perform at saving HTML? For example, there are some real, obvious
problems with the way Writer exports HTML. It doesn't even resize
images. And there are well-known issues with Word and its
round-trappable HTML format which includes a lot of non-standard stuff.
Are they fixed in Word 2007?

I'd think a review, even a brief one should be able to address these
issues.

Instead, it makes different points about the different word processors
without giving any sense of how they compare for given tasks.

They think Writer would be good for academic writing. Don't like Word's
citation support, make passing reference to
[EndNote](http://www.endnote.com/) without even getting its name right.
Nothing about citations for Word Perfect.

Anyone who set out to write a quick academic paper using OpenOffice.org
rather than Word + EndNote on the basis of this review would likely be
quite disappointed. (In the time it takes to get a PhD done we should be
able to supply better tools via the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project and the
OpenOffice bibliography project will likely have made some progress).
I'm not sure you you'd go with Word 2007 <span
class="spCh spChx2013">–</span> it would probably depend on whether the
referencing style you wanted was available. But I'm betting that you'd
have more chance of getting help than with OpenOffice.org.

But wait, there's more! The review says as a negative point about
Writer:

> Styles and Formatting dialog cannot be docked. Word processing is all
> about styles and while OpenOffice.org makes styles very easy, c'mon!

OpenOffice.org does NOT make styles easy. The default is to apply styles
using a non-dockable dialog. There are at least 3 other usability
problems with this dialog.

1.  It **doesn't let you use the keyboard** to navigate through long
    lists of styles. Hitting 'h' should take you to the headings.

2.  By default it **does not show you the styles** in the template
    you're actually using. My trick is to switch from showing paragraph
    styles to list styles and then back to paragraph styles.

3.  **List styles.** I hate to bring this up again, but OpenOffice.org
    has both list and paragraph styles which are sort-of linked
    together. I keep asking for someone to explain to me how it's all
    meant to work, but so far the best approach I've been able to find
    is the one we use in our ICE templates. We provide a custom menu
    that bypasses the non-dockable dialog. It calls macros to apply
    redundant paragraph and list style information, which aids
    enormously in document interoperability.

(And if word processing is about styles then why is there so little
about them in the review?)

Normally I'd ignore something like this, and I'm not going to spend any
more time on it, but can we please elevate the debate about file formats
and word processing from this level? Is anyone interested in solutions
or do you all just want to score points in the ODF vs OOXML pissing
competition.

</div>
