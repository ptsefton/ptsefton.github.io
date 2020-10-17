---
Author: ptsefton
Comments: true
Date: 2012-08-31 08:54:15+00:00
Slug: how-to-write-and-format-a-technical-procedure
Category: How to
Title: How to write and format a technical procedure
Wordpress_id: 1438
---

<article itemscope="itemscope" itemtype="http://schema.org/ScholarlyArticle">
<section>
## About this document

<section>
### Background

The first job I had after doing a PhD in linguistics, back in 1995 was
as a technical writer for TAFE NSW, working exciting stuff like how to
set up networking in the MicroVax servers they had running the networks
in the computing labs (TAFE does vocational education). The tech-writing
team leader was called David Drinkwater, and he taught me some simple
rules that have proven to be very reliable[^1].

The most important rule is to use the imperative voice. That is, tell
the reader exactly what to do in each and every step without ‘you
should’ or ‘the following needs to be done’.  Every job I’ve had since I
have written up some kind of variant of this quick primer for my team,
so this time I’m putting in on my own site so I don’t have to rewrite it
every five or so years. Suggestions are welcome, via the comments.

</section>
<section>
### Scope

This is about reproducible procedures that need to be unambiguous. Think
*training* rather than *education*. If something can be expressed as a
kind of recipe then these guidelines will help to make it unambiguous
and easy to digest. This approach is not what you want for discussing
the history of food or reviewing a restaurant.

There is a bit of a bias in this document towards command-line
installation guides for server software because that’s what I have been
working with lately, any suggestions of tips and tricks for other kinds
of procedures will be gratefully received and incorporated.

I pay some attention to document structure and formatting here. I’m
assuming most documentation these days is destined for the web. If it’s
going to be housed on a project site then it probably makes sense to
draft and manage it in the project site. For many projects this will
mean using a wiki format in GitHub, Google Code Jira, Trac or the like.
If there’s interest I could do a Markdown template or similar. Me, I
happen to use Word, because it’s a comfortable writing environment and I
happen to have [a tool for creating clean HTML from Word
docs](http://ptsefton.com/2011/10/18/worddown-word-to-html5-conversion-tool.htm).

This document is intended to be an example of the procedural style it is
expounding, even though it’s not strictly a procedural document.

</section>
<section>
### Audience

This document is for people writing technical procedures, particularly
to do with software, such as installation or user guides. No special
technical skills are required apart from the ability to format a
document using headings and numbered lists.

</section>
</section>
<section>
## The process

<section>
### Provide background

1.  Make sure that it is clear who the document is for by putting a
    heading near the top like “Audience” or “Who is this for”. Then, as
    I repeat below, write for the identified audience all the way
    through.

2.  As with a recipe, at the top of the document, list all the
    ingredients and any special tools, software, permissions, licenses
    or URLs for name authority services as well as where to find them
    (if you don’t know what that is then you understand that’s why it
    needs to be up the top of the document).

    Your reader doesn’t want to find out they need a second computer, an
    account on iTunes, two litres of ethanol, a sorbetière with the
    frozen bit already chilled, a special proprietary wrench and an 8”
    floppy disc half way through.

</section>
<section>
### Document the steps

1.  Use imperative statements formatted as numbered lists.

    That is, command-sentences like the one above. Yes this is the way
    we talk to dogs. Think “Sit”, “Stay” and “Shake”. Yes, it might be a
    bit rude, but it is unambiguously something the reader is to do.

2.  If context is required, then add it to the beginning of the command,
    as I did in this sentence, which is a still a command (the verb is
    “add”).

3.  Write for your identified audience.

    For example a Linux systems administrator can be told to “Edit the
    file” while if you find yourself explaining this to a non-expert
    then a lot more detail will be needed about how to get in and out of
    the editor and how to make the change.

4.  Never, ever, use the passive voice in the actual procedural part of
    procedures.

    > For example:
    >
    > > The file is now loaded into the database.
    > >
    > > The machine is shut down.

    Both of these are ambiguous because the agency is missing. Who
    loaded the file? Who shut down or is about to shut down the machine?
    (This is not general advice for all documents, the passive is useful
    and appropriate in many genres, just not in the server room).

5.  Remembering to issue commands, in context, use forms like this:

    > To shut down the machine:
    >
    > 1.  Push the big blue button for ten seconds.
    >
    >     The machine will emit an audible sigh and the lights will go
    >     out. When the lights are out that means it is shut down.
    >
    > 2.  If the machine did not sigh and shut down, repeat (i).
    >
    > 3.  If the machine is still not shut down after three tries, hit
    >     it with the hammer you prepared earlier.
    >
6.  Don’t be relentlessly positive, even if they taught you that in
    business school. If there’s something that the reader shouldn’t do,
    warn them explicitly.

</section>
</section>
<section>
## Factor the procedure into blocks

Yes, sometimes you need some non-procedural background to your
procedure. Put it below a heading like this text. This kind of
background is where you can put options such as variations people might
like to try, but if it’s a technical procedure you’re writing don’t be
tempted to turn it into a training manual about all the configuration
options that might be possible or some kind of narrative. Pick one
unambiguous pathway and tell the reader how to follow it. Most of us
need to learn a few scales before we improvise.

1.  Don’t ask the reader to perform a lot of computational thinking such
    as adding alternatives such as “If you’re on a Mac”.

2.  If more than a few decisions need to be made along the way, make one
    or more separate procedures.

    Yes that might be a maintenance problem. Solve that problem yourself
    and spare the user.

3.  Avoid the use of variables like
    \<\$wherever-you-decided-to-install-this\> and pick one
    best-practice way to do things. For example, on a Linux system tell
    people to install code in /opt/ or in the desktop world tell people
    to drag a mac application into Applications. If they disagree they
    can do it differently.

4.  Break procedures up into manageable blocks of, say, no more than
    seven steps which perform some logical sub task, use a particular
    user account or take place in a particular part of an application.
    There a couple of ways to do this:

    1.  Start a new list of steps with a paragraph like “To shut down
        the machine”.

    2.  Use an imperative heading. That is, a command.

NOTE: when I was drafting this document the above “Break procedures up
into manageable blocks of, say, no more than seven steps” was step 8,
that was funny, but it was also wrong, so I re-organized the document.
No, seven is not a magic number.

<section>
#### Test it!

When you have finished:

1.  Get someone who fits the profile for the identified audience to test
    your procedure.

2.  Before they start, get the tester to read these or any other
    guidelines you have so they can check the procedure for compliance
    as well as tell you if it works.

3.  Fix any problems and retest.

NOTE: If you’re working on a development project, and the documentation
isn’t working then there’s probably a problem with the process, which
might mean the software has been built badly or the system isn’t
working.

If it’s hard to document it’s likely impossible to use.

Tell someone!

</section>
<section>
### Avoid writing documentation

No, “Avoid writing documentation” does not mean “don’t document things
that need to be documented”. It means, try to minimise the need for
documentation.

1.  For example, work towards turning multi-step installation procedures
    into installation packages or scripts.

2.  Go back to the business analysts, programmers, managers or whoever
    invented the process you’re documenting and work with them to
    automate or eliminate everything you can.

</section>
</section>
<section>
## Tips and tricks

<section>
### For command line documentation

1.  Format  command-line commands in \<pre\> blocks for the web or in
    monospace fonts for print.

2.  Make it easy to copy and paste commands, and not just one at a time:

    1.  Do not include the prompt unless you can let the user copy and
        paste commands without having to edit it out.

    2.  Don’t let line-breaks creep into commands in a way that makes
        them hard to test (this is a problem with PDF).

    3.  If you really wanted the prompt because it showed the working
        directory or username then make that explicit with commands. For
        example:

            #Become the user this app will run assu dc21cd ~ 

    4.  Use comments, as seen in the previous example as you would in
        code.

</section>
<section>
### For desktop or web software

1.  Use screenshots where they’re genuinely better than using text, at
    least the first time you refer to that particular visual interface
    device.

2.  Even if you have used a screenshot refer to things in text, such as
    “From the File menu choose Close”, this will help readers to find
    things via searching in the documents and in search engines.

3.  If there are a lot of configuration items, summarise them in a table
    in text so they can be searched; even if there are screenshots as
    well.

4.  Format menu items and using \<code\> in HTML or a monospace font in
    print.

Copyright<span class="apple-converted-space">  </span>Peter Sefton,
2012. Licensed under<span class="apple-converted-space"> </span>Creative
Commons Attribution-Share Alike 2.5<span
class="apple-converted-space"> </span>Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>




</section>
</section>
</article>

[^1]:   The only thing I’ve changed from David’s original advice on
    writing about software is to recommend formatting mentions of menu
    items using \<code\> in HTML or a monospace font in print, but as
    David said, it is sufficient to use the exact capitalisation and
    punctuation of the menu: “From the File menu choose Save as…” Also
    we didn’t have to deal with stuff like the Microsoft Word Ribbon in
    those days, so fewer screenshots were required.
