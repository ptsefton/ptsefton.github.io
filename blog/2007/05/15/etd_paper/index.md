---
Title: "Submitting a paper to a conference using ICE"
Slug: etd_paper
Date: 2007-05-15

---
<div>

It's been quiet here because I have been busy writing up my paper for
the [ETD conference](http://epc.ub.uu.se/etd2007/) in Uppsala Sweden.
For the unitiated, ETD means 'Electronic Theses and Dissertations'. My
paper is on Thursday 14<span class="T1">th</span> June 2007 in the
session on [Realising the vision of
ETDs](http://epc.ub.uu.se/etd2007/sessions/1.html?keepThis=true&TB_iframe=true&height=480&width=640).
Seems like a good session for our work on the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project, which
is mid way through. We have some progress to report and a vision to
share.

As usual, I used the ICE template to write the paper, 'cos that's by far
the fastest way for me to work, and I can use the paper itself as a
demonstration of the extraordinary powers of the Integrated Content
Environment, ICE.

Like most journals and conferences the ETD conference has a template
that you're supposed to use to submit the paper. They accept Word or
OpenOffice.org Writer formats which is nice. The template's pretty
straightforward. I wrote to the organizers to find out whether they
minded wanted me to use their style names or whether it was the look
that mattered. Turns out in this case that it is the look that's
important into the style names.

This was an opportunity to make a contribution to the ICE-RS project
where one of the goals is to show how ICE might be used to contribute to
various conferences and journals. So I worked out how to get a document
that looked right for the ETD conference, but used ICE styles.

For those of you who know your way around the more technical side of
your word processor this may be of interest. I'm putting this stuff up
here so I don't forget. We'll come back to this on the ICE-RS project as
this is one of our deliverables.

The process for OpenOffice.org or Word is as shown in this picture. I
expand on it below with more words specific to OpenOffice.org. (I'm
leaving out the issue of toolbars and macros here as we're working on
making the ICE template into an OpenOffice.org extension).

![Object1](/blog/2007/05/15/etd_paper/1.gif)

Here are my notes on how to create conference template that uses ICE
styles:

1.  Open the conference template using OOo Writer.

2.  Rename all the obvious styles to ICE equivalents:

    -   Heading-2 -\> h2

    -   Standard -\> p

3.  For less obvious styles create new ICE styles that are subclasses.

    For example we have not finalised our metadata styles in ICE yet, so
    I mapped as follows:

    -   Abstract heading -\> h-abstract

    -   Abstract -\> p-abstract

    -   Author -\> p-author

4.  Save the new document as an OpenOffice.org template <span
    class="spCh spChx2013">–</span> leave any sample text in there as
    this will be your new conference template.

5.  Open a blank ICE document using the default ICE template.

6.  `Load Styles...` from the new conference template.

    The `Load Styles...` dialog is hidden in the Styles and Formating
    widget:

    ![graphics1](/blog/2007/05/15/etd_paper/2.jpg)

    1.  Set the checkboxes as shown

        ![graphics2](/blog/2007/05/15/etd_paper/3.jpg)

    2.  Click From File... and select your new conference template.

    You now have an ICE document where some of the styles are formatted
    in correctly for the new template, and others may be a bit off
    depending on how well the style inheritance stuff is working in the
    ICE template. (I say this because I think we can improve it).

7.  Fix the ICE styles so they're consistent with the conference styles.

    In my case that meant fixing all the list and blockquote styles to
    have the correct spacing before and after. This should have been
    easier than it was; we need to repair the ICE template so
    inheritance works better, it really should be a matter of fixing one
    style, say the basic list bullet and having all the others fall into
    line.

    To fix the styles I resorted to saving my document, unzipping the
    parts inside and doing search and replace on the formatting.

8.  Save the ICE document.

    This has all the styles you need with the right look, but won't have
    the right margins and headers and footers etc.

9.  Reopen the conference template, which has some, but not all ICE
    style.

10. Load the styles from the ICE document.

Voila! A document that looks like it belongs at the conference, but
which actually uses ICE style naming conventions.

For the other case where the conference organizers want the document
with their styles we'll need a variant of the above process. I'm
thinking along the lines of a style-mapping table that can be run to
change the style names back to their styles on submission.

</div>
