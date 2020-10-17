---
Title: "Workflow 2.0"
Slug: workflow_2_0
Date: 2006-10-24

---
<div>

Two projects I've been working on are about to collide.
[RUBRIC](http://rubric.edu.au/) has been looking at institutional
repositories for storing finished documents and ICE looks at the process
of creating documents. RUBRIC is considering long term storage of
documents with stable metadata (ie fairly fixed context) and
[ICE](http://ice.usq.edu.au/) is looking at short-term storage of works
in progress where context changes all the time.

As these projects meet workflow becomes very important. It is a hot
topic for the [RUBRIC](http://rubric.edu.au/) project and we have been
also asked about workflow in [ICE](http://ice.usq.edu.au/).

I want to think about Workflow for Web 2.0

Web 2.0 is all about open systems and people  interacting. (I was not a
fan of the term, but I've given up resisting and started using it.)

Wikipedia [currently
says](http://en.wikipedia.org/wiki/Web_2.0#Introduction):

> In the opening talk of the first Web 2.0 conference, Tim O'Reilly and
> John Battelle summarized key principles they believed characterized
> Web 2.0 applications:
>
> -   the Web as a platform
>
> -   **data as the driving force**
>
> -   **network effects** created by an architecture of participation
>
> -   innovation in assembly of systems and sites composed by **pulling
>     together features** from distributed, independent developers (a
>     kind of "open source" development)
>
> -   lightweight business models enabled by **content and service
>     syndication**
>
> -   the end of the software adoption cycle ("the perpetual beta")
>
> -   software above the level of a single device, leveraging the power
>     of The Long Tail.
>
The highlighting is mine – these are the bits I want to talk about in
this post.

I think that some of the characteristics of  'Web 2.0' are important to
workflow. I'm thinking that workflow should emerge out of the
interaction between people using multiple different, mainly web-based
systems, and that building too much workflow into any one system is
likely to be unsatisfying.  Web 2.0 is about relinquishing centralised
control over process, while maintaining the integrity of individual
systems.

The idea is to work out what you are trying to achieve. For an
institutional repository the criteria for inclusion might be something
like the following.

An item must:

1.  Be a **peer reviewed scholarly work or thesis** for which a
    higher-degree has been awarded.

2.  Be available for **Open Access**.

3.  Have associated **archival-quality metadata that has been
    certified** by the library.

So any item that meets these criteria can and should go in as
automatically as possible. It shouldn't matter in what order these
things happen, just that they can be shown to have happened. If the
metadata for a thesis can be finalized during the examination period and
locked-down then why not allow that even if the workflow designer didn't
foresee that happening?

Cameron Loudon and I like to call this approach 'emergent workflow' but
I'm thinking of calling it 'Workflow 2.0' .

# <span id="id1981886"></span>Workflow 2.0: what would it look like?

Currently it is *de-rigeur* for institutional repositories (IRs) to have
a web-ingest mechanism. That is, there is a form you can fill out on the
web to upload a document.

But in a Workflow 2.0 system the IR might not need to have a web ingest.
Instead there could be an **ingest rule** that would fire when a certain
context was detected, such as a document attaining a certain state of
development, which would be reflected in it's metadata. That's the
'**data as the driving force**' that's quoted above. In this case it's
metadata that's doing the driving.

So if your institution uses Microsoft Sharepoint, for all content
management, then you might add your paper to Sharepoint, and collect
metadata about it there. Sharepoint could have an ATOM feed for
'Conference papers that have been accepted into peer-reviewed
conferences'. The IR would subscribe to the feed and grab new content
automatically. That's **content and service syndication**.

Or there might be a marvelous metadata collection application that is
independent of the IR – why not use that? I know some libraries use
their existing metadata tools rather than the ones that come with the
repository; the examples I've seen have been a bit clunky, but in a Web
2.0 / Workflow 2.0 world integration could be quite seamless.

We're going to try this with ICE in the new [ICE-RS
project](http://ice.usq.edu.au/introduction/ice_rs.htm).

Here's a fictional scenario. We don't have all these features yet:

1.  I decide to write a paper for a conference. Let's say it's
    [AusWeb](http://ausweb.scu.edu.au/).

2.  I go to my drafts folder in ICE and add a new document, choosing
    'conference paper' as a template.

3.  ICE brings up a form with a few key details.

    1.  name of the conference

    2.  date the full paper is due

    3.  dates the conference will be held

    4.  working title for the paper

    5.  what referencing style does the conference require?

        (If ICE doesn't already know some of the above entered by
        another user)

4.  ICE creates a document and I start working on an abstract.

5.  I forget all about it.

6.  A month before the deadline, my calendar reminds me that the paper
    is due in a month.

    How?

    Well, when I added the draft, ICE added the dates to its iCal
    calendar, including reminders at strategic points. My calendar is
    subscribed to ICE, so the reminders will pop up at the right time.
    That's workflow 2.0; there's no overarching 'flowchart' in ICE
    that's mapping out steps, more a polite integration with my other
    tools. That's  **pulling together features.**

7.  I finish the paper and use ICE to format it to AusWeb's style guide.

8.  Here it would be great to click the 'submit to AusWeb' button, and I
    have spoken to the organizers about making this happen, but maybe I
    have to do the submission myself and just tick the 'I have
    Submitted' button.

9.  My paper is accepted subject to some fix-ups, so back to step 7
    until...

10. ... the paper is unconditionally accepted so  I can tick the box
    that says 'Accepted'.

11. The USQ [e-Prints site](http://eprints.usq.edu.au/) notices that my
    paper has been accepted, via an ATOM feed that watches ICE, and
    grabs a copy for the repository, where is sits in a holding pen
    awaiting review.

12. A librarian **grooms the metadata** I added to my document and when
    it's spiffy, uses the IR's internal workflow to ingest the document.
    Optionally, the librarian could do this in ICE some time during the
    authoring process, and we can cut out the approval process at the
    end.

13.  ICE reminds me, via my calendar that I have three weeks to sort out
    my travel.

There's other potential here as well. There might be a **dashboard in
the travel office** that works out that there are three people planning
to attend the same conference, so maybe we should share transport.
That's a kind of workflow I can't see you getting any other way. Imagine
trying to put in a new university-wide system that tried to track all
the conference submissions happening everywhere so the bureaucrats could
save a few dollars. But if authors are induced to input the data because
it's of use to them, then we might see a '**network effect** created by
an architecture of participation'.

Hey, ICE might even be able to help in filling out the travel forms or
interfacing with the travel API for the University, assuming it's a
'2.0' kinda system.

</div>
