---
Title: "Matt Zumwalt showed some great work on XForms and Fedora at OR07"
Slug: xforms_revistied
Date: 2007-01-25

---
<div>

I'm at [Open Repositories 2007](http://openrepositories.org/). <span
class="spCh spCh0xa0"> </span>

Getting over my jetlag now, one day's not too bad. <span
class="spCh spCh0xa0"> </span>(I demanded advice from an expert, but she
only said travel 1<span class="T1">st</span> class or stay at home.
Thanks [Justine](http://justinelarbalestier.com/blog/?p=521).)

I [wrote recently](http://ptsefton.com/blog/2007/01/10/xforms_mods)
about unfinished explorations I did with XForms as a metadata editing
system.

Yesterday I was most impressed with a presentation on XForms and the
[Fedora repository](http://www.fedora.info/) by Matt Zumwalt,
*Simplifying Fedora Frontends with XForms and Fedora*. Matt talked about
how he added an interface to allow editing of XML metadata streams in a
Fedora repository using XForms. What this means is that a bit of
standards-based configuration code can be used to build a portable
interface for editing structured XML.

(Technically, XForms has <span
class="spCh spCh0xa0"> </span>Model-view-controller (MVC) pattern, where
the model can be an instance document, and the view is an XForms
description of how to edit it. The controller is an XForms application,
so you don't have to write that.)

Matt's work **should work with**
[**MODS**](http://www.loc.gov/standards/mods/) **metadata**, which seems
to be a strong prospect for RUBRIC and ARROW repositories in 2007. I
hope to have more to report on this soon.

It could be used for **repositories other than Fedora**, like, say
[DSpace](http://www.dspace.org/). Scott Yeadon of ANU gave a demo of
moving objects between Fedora and DSpace; and talked about a package
profile from the National Library of Australia for interchange. Seems
like there is hope that Australian repositories might be able to agree
on interchangeable content models.

Matt told be me wants to take the time to document his XForms code and
he will put in on the web when he's done that.

Christiaan Kortekaas of UQ tels me that he looked at XForms a few years
ago, before starting Fez, and the technology wasn't ready. Fair enough.
I think it is just about ready to use now, and I'd love to see this idea
taken further. I've already started talking to our friends from
[APSR](http://www.apsr.edu.au/) and [ARROW](http://arrow.edu.au/)about
collaborating to achieve this.

I know a couple of VTLS people were in the audience, and I hope they're
able to do something with XForms too, for their VALET/VITAL product,
which badly needs a way to edit metadata without invoking a
general-purpose XML editor (I think they might).

</div>
