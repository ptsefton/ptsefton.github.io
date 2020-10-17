---
Title: "Use Styles"
Slug: use_styles
Date: 2005-03-02

---
If you're using a Word processor for anything other than one-off party
invitations or printing labels for the home-brew then you need to use
styles in your documents. You probably knew that already, but I have
been thinking about what that means.

I have been working on a couple of articles about styles in
OpenOffice.org. And last week I had to apply for a job, the one I'm
doing now, but which finishes for me in a few weeks unless, of course, I
get reappointed. The application got me thinking about what I used to
do, as I wrote about how wonderful I am. A lot of my wonderfulness has
to do with my tenacity in promoting the use of styles in word processors
year after year in job after job.

For the last ten-ish years I have been working with documents in content
management systems (you can read [what I think content management
is](blog/2004/12/08/what_is_content_management)), supporting knowledge
management systems. In all cases the first step for the back-end of the
system has been to figure out how to get from word processor documents
into
[SGML](http://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language)
or more recently [XML](http://en.wikipedia.org/wiki/XML). At the front
end it's been styles, styles and more styles, except that the useful set
of styles has not changed much, we just have to keep teaching it to new
converts.

What has happened in the last ten years is the word processors I work
with (Microsoft Word and now OpenOffice.org Writer) have made it easier
and easier to get XML out and back in again with no major innovations in
the way they work. Although Word is [clearly getting
worse](blog/2005/01/20/templates_atrpohy).

Using styles has been essential. Documents created in 1997 at Standards
Australia would slot straight into the work I've been doing on the [Word
Processor Interoperability
Project](http://del.icio.us/ptsefton/ptsefton+wpinterop) with a few
simple style-replacements.

The message here is that it is consistent styles that are the most help,
not 'doing XML' (yes, yes exporting to XML is an essential insurance
policy and a requirement for any system). Standards Australia's strategy
of keeping the Standards in Word format, using it to render them, then
'siphoning off' XML for web output has worked out well, but only because
of the styles.

When haranguing your company's management about the need to future-proof
their data by getting it into XML I think that the case for moving to a
'pure' or old-school XML system is pretty weak, unless you are in one of
the industries where text-processing will otherwise kill you, like
military hardware, legal publishing, the legislature and so on.

Using OpenOffice.org I can rescue Word documents and bring them into its
open-XML-based world as opposed to the Microsoft
proprietary-but-now-XML-based-world-if-you-upgrade. But while the
underlying XML in both camps is now considered essential, it doesn't
help much in re-processing documents either using XML tools or the word
processor unless you started with styles.

In my work at USQ we are experimenting with processing legacy FrameMaker
documents, initially to render as HTML, and there are plenty of pathways
between Frame, OpenOffice, XML, Word and so on all with their own
issues. But the big win is that these documents all used styles in a
consistent way, because they were maintained by a good well-trained
in-house publishing team. It looks like XML may not even figure in the
conversion from FrameMaker to Writer, as RTF seems to work just fine.
Score XML zero, styles 1.

And who really needs to do more than pump out content for print and
HTML. Yeah, you might be making a CD, but what will it have on it? HTML
and PDF, even if you have put a fancy flash reader in front of it.

What about an XML-backed Knowledge Base for all them advanced searches
you're gonna be running? Well, why not feed it XHTML, using class
attributes to carry semantics and then it will be easy to program
queries against since everyone who is anyone knows XHTML. In this way
you could build a system for searching both legislation and the manuals
for nasty guns with only a customization layer to worry about for the
advanced search interface - those applications need an (X)HTML output
anyway, so why not standardize and make life easier for systems
integrators and therefore cheaper all round?

It's the styles that matter.

Use styles.

\$LastChangedDate: 2005-03-02 01:28:44 -0600 (Wed, 02 Mar 2005) \$
