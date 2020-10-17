---
Title: "How the ICE Python came to be"
Slug: how_the_ice_python_came_to_be
Date: 2006-03-09

---
<div>

I've been reading stuff on programming languages via Tim Bray's [ongoing
site](http://www.tbray.org/ongoing/When/200x/2006/03/05/Languages-Today).
I liked the pieces by Steve Yegge, who now chooses Ruby. What's more he
has a bike analogy:

> If languages are bicycles, then Awk is a pink kiddie bike with a white
> basket and streamers coming off the handlebars, Perl is a beach
> cruiser (remember how cool they were? Gosh.) and Ruby is a \$7,500
> titanium mountain bike. The leap from Perl to Ruby is as significant
> as the leap from C++ to Java, but without any of the downside, because
> Ruby's essentially a proper superset of Perl's functionality, whereas
> Java took some things away that people missed, and didn't offer real
> replacements for them.
>
> <http://www.cabochon.com/~stevey/blog-rants/tour-de-babel.html>

(I have never ridden a \$7,500 titanium mountain bike, but maybe I can
find out what it's like by writing some Ruby.)

I thought this might be a good time to talk about why we chose to write
the cross-platform publishing Integrated Content Environment (ICE) in
Python about a year ago.

1.  We needed to integrate with OpenOffice.org which ships with Python
    built-in, so there's likely to be lots of example of Python code to
    draw on.

2.  While we had a team well qualified and practiced with Java, none of
    us had any confidence that we could get a cross platform Java
    application to run correctly. I couldn't get simple applets written
    by the USQ team to run in Firefox at the time and I simply dreaded
    having to go to Sun's site to download Java! Which one do I need?
    JDK, JRE who knows? And how do I run a Java thing I've downloaded?
    Classpath? What?

3.  Python allows us to compile stand-alone applications for Windows and
    OS X.

4.  [Chandler](http://chandler.osafoundation.org/), the new über
    Personal Information Manager project is using Python. The OSAF team
    did their homework and bet on Python. And ICE was aimed at a similar
    community, starting with Higher Education just like Chandler. One
    day ICE, or part of it may even become a Chandler module.

5.  **Python is a good language**, mostly consistent and easy to test. I
    think that Python's whitespace makes for readable, more consistent
    code, It bypasses the need to document at least some aspects of a
    coding standard.

    We use [py.test](http://codespeak.net/py/current/doc/test.html) for
    our unit test framework, in addition to
    [UTF-X](https://utf-x.dev.java.net/) for testing XSLT.

Some things are less than ideal.

Python has pretty feeble native XML support, lacking the crucial XPath
and XSLT out of the box. We use [libxml2 and
libsxtl](http://xmlsoft.org/), which work in not very Pythonic way but
get the job done.

But why not Ruby, and possibly Rails?

Ruby's profile a year ago was nothing like it is now so we didn't really
consider it. I think if we were to start ICE now, it would be worth a
look. It **can** be [compiled into stand-alone
executables](http://www.erikveen.dds.nl/rubyscript2exe/index.html) just
like Python. There would be lots of work to do, though to find out about
subversion libraries and OpenOffice.org integration.

****

</div>
