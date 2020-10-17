---
Author: ptsefton
Comments: true
Date: 2009-02-12 10:36:10+00:00
Slug: the-path-to-developer-happiness-unit-testing-in-python-xslt

Title: 'The path to developer happiness: Unit testing in Python & XSLT'
Wordpress_id: 284
---

<div>

<div class="page-toc">

</div>

<div>

When David Flanders asked me what I'd like to talk about at the
Developer Happiness Days, I thought I could do something on XSLT <span
class="spCh spChx2013">–</span> which turns out to be not that much of a
hot topic <span class="spCh spChx2013">–</span> I ended up giving a
short talk on XSLT and where to use it and where to not use it, and
contributing to the Python day. In both cases I pushed the idea that
beginners should start with test-first unit testing.

In the Python day we had a discussion about Integrated Development
Environments and concluded that there is no one way, but Eclipse does
seem to be popular (Ron Ward and I loathe it but others in our team use
it happily). Someone pointed out to me that Eclipse is really good for
multi-language development.

I did a quick demo of
[Doctest](http://docs.python.org/library/doctest.html) which is a way of
embedding unit tests in documentation.

What's a unit test?

> In [computer
> programming](http://en.wikipedia.org/wiki/Computer_programming),
> **unit testing** is a software design and development method where the
> programmer verifies that individual units of [source
> code](http://en.wikipedia.org/wiki/Source_code) are working properly.
> A unit is the smallest testable part of an application. In [procedural
> programming](http://en.wikipedia.org/wiki/Procedural_programming) a
> unit may be an individual program, function, procedure, etc., while in
> [object-oriented
> programming](http://en.wikipedia.org/wiki/Object-oriented_programming),
> the smallest unit is a
> [method](http://en.wikipedia.org/wiki/Method_%28computer_science%29),
> which may belong to a base/super class, abstract class or
> derived/child class.
>
> <http://en.wikipedia.org/wiki/Unit_testing>

My contribution was a hello world program where the testable bit was a
'hi' function.

(And we didn't really say this but everyone I spoke to was in favour of
developing with Unix based OS, meaning OS X or Linux (Ubuntu is the
default now). If you're stuck with Windows then get some virtualization
going.)

And here are my notes for the lighting talk on XSLT:

<div class="slide">

# XSLT? What is it? Why would you use it?

In this talk I'd like to cover the basics of:

-   What it is?

-   When to use it and when not.

-   If you are going to use it, how to do so without losing your mind.

</div>

<div class="slide">

# What is XSLT?

1.  A way of transforming XML into (almost always) another kind of XML.

2.  XSLT is a plot by the computer science intelligentsia to sneak Lisp
    into your life.

3.  XSLT is aggressively 'functionally' oriented (ie it's Lisp with an
    even scarier syntax).

4.  XSLT is a standard widely available, simple way to transform data
    from one format to another.

5.  XSLT 2 is an improvement but there is a severe shortage of
    implementations

</div>

Places I have used XSLT follow.

<div class="slide">

# The all-encompassing XSLT CMS

An entire web framework for content management. Site structure was
defined by a 'site map' which was compiled into a big XSLT stylesheet
used to process every request.

Do it again?

Emphatically no.

</div>

<div class="slide">

# Rendering word processing documents into HTML

Gets very complicated when trying to create hierarchical structure from
flat input.

Modern word processing formats have too much indirection and too much
application baggage to process with XSLT.

Do it again? Not until XSLT 3 :-)

</div>

<div class="slide">

# Simple data transforms

Simple data transforms for mapping data from one relatively flat form to
another <span class="spCh spChx2013">–</span> eg EndNote references to
Dublin Core metdata.

Works well enough.

Will do it again.

</div>

# <span id="id1"></span><!--id1--></a>

<div class="slide">

# If you're going to do it

Test first!

XSLT can really mess with your mind. Start with test cases. We use
UTF-X.

<http://utf-x.sourceforge.net/>

And here's a quick [how to get
started](http://ice.usq.edu.au/trac/wiki/InstallUtfx) on Ubuntu that I
worked out in my prep for dev8d.

</div>

Summary:

1.  Don't overdo it.

2.  Use it where the overall structure of you input and output is either
    very congruent or very simple.

3.  Write tests first.

</div>

</div>
