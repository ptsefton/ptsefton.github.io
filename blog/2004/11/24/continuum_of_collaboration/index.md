---
Title: "A continuum of collaboration"
Slug: continuum_of_collaboration
Date: 2004-11-24

---
Tim Bray [wrote about how blogs and wikis are
different](http://tbray.org/ongoing/When/200x/2004/11/05/BlogWikiHuh):

> A wiki is a collaborative construction engine, with refactoring and
> edit-in-place being the dominant forms of activity, and many equal
> voices singing in a chorus. A blog is more like a content faucet, a
> source with one voice, always growing at one end; while updates to
> existing content are OK, the dominant activity is pouring new text and
> pictures and whatever in.

And James Tauber is [belatedly
continuing](http://jtauber.com/blog/2004/11/15/belated_thoughts_on_blogs_and_wikis).

James points out there are a number of dimensions of wikiness, and I
agree with him.

I'd like to talk about just one dimension: collaborativeness (James'
"Spirit of collaboration").

At one end we have a wiki, which is can be changed by anyone. That's
collaboration.

At the other end we have a blog like this one, which is mine all mine,
even though it uses wikiesque markup and which has no comments. You can
converse with me via email, your own web site, or a tag in del.icio.us
but you can't collaborate except by quoting me elsewhere. Ha!

(Can I *have* 'ends' to a dimension? James would know.)

Here I talk about another kind of collaboration that is not wiki-like
which I have implemented before, and which We are exploring here at USQ,
for a potential content-seeded learning system, either as an extension
to or a replacement for a 'traditional' Learning Management System.

In between there are blogs with comments, and blogs with discussion
forums, and wikis with closed authorship.

I have worked a lot with another approach which is to use inline
commenting or annotation. The Continuous Publishing System that we built
at NextEd (now available from Sourceforge in [kit
form](http://sourceforge.net/projects/cps-skite/) only - know how to use
CVS and NANT?) allows annotations in-line on published content.
Published means locked, and once content is locked it can magically
sprout little discussion links on every paragraph, based on a unique id,
like Tim Bray's [purple
pilcrows](http://www.tbray.org/ongoing/When/200x/2004/05/31/PurpleAgain).
This lets people make a small bit of content that adds to the main one
but is stored separately. They can point out a typo, or ask a question,
or see the original content without all the annotations all over it. At
previous jobs we used this technology for:

-   Indicating that you had read something. "Annotate here to show me
    you read this". Very handy for proving to one's self that management
    either (a) don't read the stuff you send them, or (b) have nothing
    to prove to you.

<!-- -->

-   Tracking tasks in projects. Project cycle notes would be written in
    a Word document, then rendered as HTML with tasks showing as list
    items. People would come in and write down (using words) that they
    had done stuff, and how long it took. We made a prototype of a
    system that could track task estimates and effort across engineering
    cycles. Adding an estimate to an item on any page would create a
    task, which you could then annotate with progress. Didn't get the
    cycles to build it, though.

<!-- -->

-   In house auctions. Stick up a page with descriptions of things for
    sale and let people add bids using the inline annotation system.

<!-- -->

-   Voting on entries in an awards process.

Right now, in my new job we are putting together a demo of how this kind
of annotation can be used in a learning system for:

-   Inline discussion in course materials - ask a question in the
    content itself.

<!-- -->

-   Completion indicators, tick off that you have done an activity such
    as a set reading, or flag that you want to come back.

<!-- -->

-   Disposition indicators, show how you feel about a course module.
    This is untested, but you should be able to mark that you are
    'unhappy' with a module, have the lecturer and peers notice, help
    you, and have you change your tag to 'happy'.

At the end of the course the teacher should be able to roll the feedback
into the module for next time and publish a new, improved version.

This is all collaboration, provided you have a *live* teacher in the
feedback loop responding to class input, but without the ability to
change the content that you have with a wiki. But a course or
meta-course wiki may be worth adding to the Learning Management System
as well, possibly one that persists across course offerings.

You can read about the vision behind this in the [paper I'm writing with
Cameron Loudon](biblio), a lot of these ideas come from his interaction
with online educators.

This approach lies somewhere between a wiki and a blog on the scale of
collaborativeness. The content is arguable, but the integrity of the
published material is assured and it is always visible behind the
annotation. In an online education environment this could be very
important — you probably shouldn't just go changing content even with
tracking of the change, and in a replicated environment where people go
on and offline, re-synchronising when they can, each item needs to be
kept as a separate transaction so you do not have merge problems.

But it is collaborative, and it is not a wiki.

[Updated with a spell check. Remember coffee first, post
later.](updated_with_a_spell_check._remember_coffee_first,_post_later.)

\$LastChangedDate: 2004-11-24 01:32:51 -0600 (Wed, 24 Nov 2004) \$
\$Rev: 85 \$
