---
Title: "Trac is the answer to all our problems"
Slug: trac
Date: 2005-03-07

---
It's official. Chris Mills, who is on our team at USQ ([see our communal
bookmarks here](http://del.icio.us/tag/usqsdt)) has declared
[Trac](http://www.edgewall.com/trac) to be the answer to all our
problems.

What is Trac? It's a project management tool that ties together
Subversion for version control, an issue/bug/feature/ticket-tracking
system and a [wiki](http://en.wikipedia.org/wiki/Wiki). There are some
gaps, to be sure, but it's a pretty useful tool out of the box.

You can set up milestones for the ends of engineering cycles and
releases, build whatever web of 'stories' you like to represent
user-requested features and add development and maintenance tasks as
tickets. The nice bit is the integration; a wee bit of scripting (thanks
Sally MacFarlane) completes the already impressive web of links between
tickets and the wiki, between commits to the repository and tickets. You
can say, like:

    svn commit -m "Added a yellow background. Fixes #978"

And it will close ticket number 978.

I found Trac as part of my relentless web-surfing, but the rest of the
team did the hard work to test it out and install it as part of a
general overhaul of our development toolset. This included slurping up
all the bugs out of [Bugzilla](http://en.wikipedia.org/wiki/Bugzilla)
and moving all the code from
[CVS](http://en.wikipedia.org/wiki/Concurrent_Versions_System) to
Subversion.

I have a trac system of my own which I will use to get serious about the
[Word processor interoperability project (WP
Interop)](http://del.icio.us/ptsefton/ptsefton+wpinterop) any day now.

But Chris, it's not going to solve some of our other problems, such as
finding just one more old Sun Microsystems disk-enclosure to prop up my
desk so we can replace those unsightly bricks, or working out how some
of us are going to get to work (if there is any) when petrol hits \$8.50
a litre.
