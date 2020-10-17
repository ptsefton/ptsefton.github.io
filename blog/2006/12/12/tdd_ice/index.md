---
Title: "Tests on ICE"
Slug: tdd_ice
Date: 2006-12-12

---
<div>

Test-driven development. Test-first programming. A **Good Thing**.

The first part of the [ICE system](http://ice.usq.edu.au/) to be written
was an XSLT stylesheet that transformed open office XML into HTML,
started before I joined USQ. Once we agreed on the GPL license I gave
the copyright to USQ to look after when we kicked off the ICE project in
mid 2005. The stylesheet was **really complicated** to write even though
I based it on a GPL stylesheet that did some of the heavy lifting. I
would never have got it working without the UTF-X test framework; I was
able to work out the tricksy techniques I needed with a **bank of tests
in place**.

When we switched to OpenOffice.org version 2 and the OpenDocument
format, others in the ICE team added tests to deal with tables and so
on.

Later on, Dr Ian Barnes of ANU, who's a computer scientist wrote a
similar XSLT stylesheet to go from **Open Document format to DocBook
XML**. He [got his working
too](http://www.apsr.edu.au/publications/preservation_of_word_processing_documents.html)
(can't remember if he wrote tests) but even he said it was hard to
figure out.

Anyway, more than a year into ICE's development cracks started to appear
in the original stylesheet. **Profiling shows** that it's one of the
slowest parts of the application, it breaks on some **long documents**
and **nobody wants to touch** it tests or not. While XSLT can do the job
it's not comfortable.

So, we decided to rewrite the XSLT in Python – using only native Python
XML libraries, instead of the libxslt2 used elsewhere in ICE. This ism
partly so we can look at turning our exporter into an OpenOffice plugin
later on.

Enter Ron Ward. He worked out a state machine in Python that could
**output nested HTML** from an essentially flat stream of paragraphs,
shifting state based on ICE styles. As he worked, Ron converted UTF-X
unit tests into a new test framework, working first on simple lists,
then adding other structures.

Ron **worked entirely from the tests**, in amongst ICE maintenance jobs,
and got all but a few things working, some of which he thought might be
wrong anyway. I asked “have you tried rendering entire documents and
looking at them”. No, he said, he didn't expect that to work. At my
insistence hooked up the new renderer and we converted a site with a
dozen documents or so using the new code. The result? **Nearly
flawless**. There are a few odd things to investigate, but on the whole
the thing just worked.

Instead of working the way a lot of us used to, by writing bits of code
and eyeballing the output, writing code that broke other code, and
**hoping** that everything was coming together, the automated unit-test
suite made the focus on small, manageable units, and guarded against
regression as the work proceeded. And while Ron was pretty sure that the
test coverage wasn't good enough to cover everything it turned out to be
**bloody close**.

So here's to test-driven development and one particular test-driven
developer, Mr Ronald Ward.  And here's to Jacek Radajewski who brought
[UTF-X](http://utf-x.sourceforge.net/) into the world and continues to
maintain it.

And by the way, I have just undertaken a minor document conversion task
for a colleague, joining up a bunch of HTML documents and turning them
into a single Word document. It was pretty simple, and I started to
think I'd **just do it without tests**, but I quickly got tangled up.
When I came to my senses it took less than a minute to set up a UTF-X
test file, and only a few more to add tests for the bits and pieces of
my file.

</div>
