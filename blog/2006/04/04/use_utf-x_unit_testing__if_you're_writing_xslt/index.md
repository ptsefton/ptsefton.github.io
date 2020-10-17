---
Title: "Use UTF-X unit testing if you're writing XSLT"
Slug: use_utf-x_unit_testing__if_you're_writing_xslt
Date: 2006-04-04

---
<div>

While unit testing is a good idea when you're programming in any
language that supports it, it's a really really good idea in XSLT,
which, for most of us is an odd programming paradigm, with hard-to
follow code.

I wrote about unit testing for XSLT [last
year](http://ptsefton.com/blog/2005/08/16/unit_testing_for_xslt) and the
[year before](http://ptsefton.com/blog/2004/05/17/xslt_unit_testing).

(If you're a manager, get all your programmers to use unit tests
everywhere they can, or write you an essay explaining why not. I'll mark
the essay for you at standard rates for casual marking.)

At the [RUBRIC project](http://rubric.usq.edu.au/) we are dealing with a
lot of metadata and configuration files, mostly in XML. We expect to be
doing lots of transformations between XML formats as we begin to look at
interoperability for [Institutional
Repositories](http://en.wikipedia.org/wiki/Institutional_repository).

This week we had to transform a file containing the Australian Standard
Research Classification
([ASRC](http://www.abs.gov.au/AUSSTATS/abs@.nsf/66f306f503e529a5ca25697e0017661f/2d3b6b2b68a6834fca25697e0018fb2d!OpenDocument))
subject codes from one XML format into another. Even though this was a
probably a run-once bit of code, using Jacek Radajewski's
[UTF-X](http://utf-x.sourceforge.net/) unit-testing system helped a lot.

Technical officer Corey Wallis installed UTF-X, which is a minor
challenge 'cos it's Java and you have to fiddle around with paths and so
on, then we sat down with the other techie, Caroline Ayers and worked
through a process that involved five tests:

1.  Write the first trivial test – the root element gets mapped.

    -   Test fails, as expected because there is no XSLT yet.

    -   Write a trivial bit of XSLT to do the transform.

    -   Test it.

    -   It works!

        (I told the team we were supposed to shout w00t and do high
        fives and stuff, but they looked at me with the 'get back to
        work' look)

2.  Write test number two, to include more nodes inside the first one.

    -   Test fails. Write some code.

    -   Test passes!

    -   Oops – broke test number one.

    -   Fix it.

    -   Both pass

3.  And so on...

All up it took about an hour and a half of coding, which included a fair
bit of the long-suffering technical officers politely listening from to
my XSLT war stories and my test-first rantings.

The result is much more useful to us than a stand-alone bit of XSLT,
though because we have those five tests that will be there if we need to
change the system, or recycle it in some way. It's only five because the
input is a single fixed file – if you're looking at variable input you
would need a lot more to test for potential problems.

We'll publish the files and our work in due course.

There's another XSLT framework called [Juxy](http://juxy.tigris.org/)
about which I know nothing, but I do know that UTF-X is worth using if
you write any amount of XSLT. When I wrote the first cut of an
OpenOffice.org to XHTML transform which is now part of the [ICE
project](http://www.ice.usq.edu.au/) I simply couldn't have done it
without unit tests; the algorithm is too fiddly and XSLT too fragile to
work effectively without a tightly-woven net of tests, which you can see
[at the ICE
site](http://ice.usq.edu.au/browser/ice/trunk/apps/xhtml-export/test/).

So, use UTF-X and send your feedback to Jacek so he can keep making it
better.

</div>
