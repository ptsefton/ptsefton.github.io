---
Title: "Trac, RSS, Subversion, OpenOffice.org getting stuff done"
Slug: trac,_rss,_subversion,_openoffice.org_getting_stuff_done
Date: 2005-05-24

---
Had a nice getting stuff done moment this afternoon where the software
tools I'm using came together in really nice way. We had finished some
more work on the [application we're
building](http://www.usq.edu.au/dec/staff/ice.htm) and I sat back down
at my desk. Nearly time to knock off, so I decided to scan the updates
in [NetNewsWire](http://ranchero.com/netnewswire/), nothing too much
there grabbed me, until I came to an item that looked like this:

> \#848: Revise licensing policy and send to Alan for approval

That's a job ticket from the [Trac](http://www.edgewall.com/trac/)
software we're using showing up in amongst all the distractions out
there on the web. I looked at Chris who's my lift home (Chris is the one
who proclaimed that [Trac is the answer to all our
problems](blog/2005/03/07/trac)), and decided there was time to get some
actual work done rather than doing 'research'.

Shifted into the terminal, updated the document directory for ICE. "svn
up". This got me the latest versions of the documentation for ICE.

Opened the policy in OpenOffice and edited it, saved and exported a PDF.

Back to the terminal and I committed it to the repository.

> svn commit -m "Fixes \#848. Updated with GPL instead of Sleepycat
> licence - to be followed up with an email to Alan"

This sent a new version of the document off to the repository, where it
will be kept with all the previous versions and it closed the ticket.
Then I sent the PDF off to the boss.

And yes, it would have been better if I had mailed the document before I
did the commit.

This is great example of the right tools coming together in the right
way. The typing part would put some people off, but there are other ways
to use Subversion, notably via the wonderful
[TortoiseSVN](http://tortoisesvn.tigris.org/) application for windows
that integrates version control into the file Explorer.

If you are behind the USQ firewall you can see this stuff - drop me a
line to find out how you can browse our repository not only of code, but
of documents, presentations and the informal Trac
[wiki](http://en.wikipedia.org/wiki/Wiki) that we use to tie it all
together and keep quick notes.
