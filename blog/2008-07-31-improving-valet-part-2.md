---
Author: ptsefton
Comments: true
Date: 2008-07-31 01:14:02+00:00
Slug: improving-valet-part-2

Title: Improving VALET - part 2
Wordpress_id: 165
---

<div>

<div class="page-toc">

</div>

<div>

This is my second post on the VALET repository deposit tool. Again, if
you're not a repository aficionado you can probably move on[<span
style="vertical-align: super;"><span
class="footnote">1</span></span>](#ftn0).

Still here?

One of the issues we confronted with VALET was to rewrite in Java or not
to rewrite in Java? VALET is written in Perl and quite nicely written in
my opinion, apart from the HTML forms which are a big mess of non-valid
HTML. There's nothing wrong with that as such, but it does have a couple
of downsides relative to Java:

1.  VALET requires a web server to be installed. VITAL used to ship with
    Apache but it no longer does, so to run VALET you can end up having
    to compile and install Apache, and obtain some other dependencies.
    If it were a Java application then you could just drop it in to the
    same servlet container as you use for VITAL and Fedora.

2.  We have heard from some of the, um, younger techies in the ARROW
    community that Perl is a complete mystery. Others report
    difficulties in hiring Perl programmers, whereas everyone does Java
    at uni these days.

On the other hand, there are some reasons not to want to do a port:

1.  Some of the ARROW contingent have been using Perl since 1934 and can
    at least tolerate it. I'd count myself in that group. Fortran
    anyone?

2.  Hacking a Java program is not as simple as using a text editor to
    change a Perl file, because you need to compile (and worry about
    stuff like CLASSPATH, ugh).

3.  A port will create a huge fork.

All these points count for something, but Prashant from University of
South Australia has pointed out that using JSP (to which I'm allergic,
like PHP and ASP) gives a much easier entry point for 'casual'
developers and even if it does fork VALET is actually a fairly small
application so the investment is not huge and the gain for sites where
they want to just consume the software should be worth it.

In the end the group here at the VALET camp decided that there was
enough interest in a Java version that they were going to go for it.
Nobody would own up to being a Java expert but four or five confessed to
having written production Java code.

They're creating an application as I write this. While they do that
Harry, Duncan and David are integrating all the changes that ARROW sites
made to VALET and submitted to the Google group. So the Java team will
have a moving target as they re-implement the Perl code.

The Perl version won't be going away <span
class="spCh spChx2013">–</span> but it looks like at least some sites
will move straight over to the Java version once it's done.

So what are the Java team (Tim, Guy, Prashant and Cyrus) doing?

They're starting a VALET compatible clone. The idea is that you should
be able to take an existing VALET workflow and data entry forms and with
minimal effort, port it to run in the new application. Best case would
be no work at all required; the new application will be a drop-in
replacement for VALET. We'll see if that can be achieved.

The new app rejoices in the working title of *Squire*, which is not an
acronym; it shows that the developers know how to use a thesaurus. Or is
it named for the [fish](http://www2.dpi.qld.gov.au/fishweb/2532.html)? I
reckon they should call it
[Alfred](http://en.wikipedia.org/wiki/Alfred_Pennyworth) or
Pennyworth[<span style="vertical-align: super;"><span
class="footnote">2</span></span>](#ftn1). Either way, it's better than
the original working title of *Black Hole*. which would be like calling
your deposit interface [Roach
Motel](http://digital.library.wisc.edu/1793/22088). Although at least if
you had a repository deposit called Black Hole you could claim very high
rates of compression for data. Just don't mention decompression.

The new JAVA platform will make it easier to do some of the other
changes that the community are asking for (we're discussion this on the
ARROW Google group for those of you in the inner-circle), in some cases
because there are more repository-oriented libraries for Java than for
Perl but also just because as a community we have more competent Java
programmers than Perl programmers these days.

Here are some enhancements that we will probably do at USQ at some stage
<span class="spCh spChx2013">–</span> there are lots of other
requirements too which we are not going to forget these are just the
ones that I can speak for at this stage:

1.  A
    [SWORD](http://sourceforge.net/projects/sword-app/#item3rd-1)deposit
    so the application can push content to repositories other than
    Fedora. We're going to look at deposit of complex objects over SWORD
    in the TheOREM-ICE project very soon so this will be a quick add-on.

2.  The inevitable ICE interface so that if you submit a styled word
    processing document to Squire if will generate good quality HTML and
    PDF renditions automatically. We're working with Ian Barnes at ANU
    and [talking to the PKP
    people](http://ptsefton.com/2008/06/26/a-few-words-on-magic.htm)
    about how we might be able to do a better job of inferring document
    structure than the standard, breathtakingly abysmal <span
    class="spCh spChx201c">“</span>Save as HTML<span
    class="spCh spChx201d">”</span> feature in word processors. Another
    step in my campaign to stamp out PDF-only Web 0.5 repositories, at
    least in Queensland.

3.  Automatic embedding of metadata and license in the PDF file in XMP
    format, based on some work which is apparently going on in
    collaboration between QUT and an Australian Government agency.

4.  A lightweight complete open source repository package with Squire
    for deposit plus [Sun Of
    Fedora](http://ptsefton.com/2008/06/27/tim-mccallum-shows-off-sun-of-fedora.htm)
    as a portal. Not a lot of features, or complexity, just the basics.

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote"></span>
[1](#ftn0-text) If you don't want to read about repositories, I
recommend Bike Snob NYC. Which prominent fast but not fast enough
Australian cyclist was he talking about last week?

> Firstly, there was Saunier Duval's impressive one-two finish, proving
> once again that there is no "I" in "team." (Though there is a "moi" in
> "chamois.") Secondly, \_\_\_ \_\_\_\_ (whose collarbones are only
> intact after yesterday's crash because they have both been replaced by
> titanium) proved he is in fact a great stage racer by taking the
> Maillot Jaune by one second. (Anybody can blast his way up a
> mountainside in a distateful display of power, but it takes a certain
> dignified restraint to sidle up behind people and pilfer seconds the
> way \_\_\_ does, like an uninvited party guest nabbing cocktail
> weiners.)
>
> <http://bikesnobnyc.blogspot.com/2008/07/rest-day-roundup-stealing-seconds-and.html>

</span>

</div>

<div style="font-size: .9em;">

<span class="footnote">[2](#ftn1-text) Bron Chandler points out that
there is some potential for [recursive
naming](http://en.wikipedia.org/wiki/Recursive_acronym) in the tradition
of GNU and HURD. Alfred Pennyworth is sometime know as Batman's batman.
What would VALET's nemesis be called? Do valets have nemeses? Do nemeses
have valets?</span>

</div>

</div>

</div>
