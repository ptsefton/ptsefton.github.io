---
Title: "Update on lists"
Slug: update_on_lists
Date: 2004-09-07

---
I have been making slow progress on the Word Processing Interoperability
project. Over the last couple of weeks I have worked on OpenOffice.org.
It's not perfect, and lags behind Word in some areas but it really is
open in some important ways. There are two small technical triumphs I
would like to report on as I work towards an actual downloadable
template. It's technical stuff.

First of all, the OO.o file format is a zip file, containing a
fragmented version of a document with all the textual content and
metadata in XML. I am interested in the word processing component for
this project, and I was able to take the default 'blank' document that
is built in to the product, save it as a template, and add the new
[styles and lists for the WP Interop project](wp-interop-styles). It was
trivially easy to take the default 'style.xml' file which, weirdly,
contains the style definitions, and add new definitions to it using an
XSLT stylesheet to automatically create both a paragraph style and a
list style (if required) for a representative sample of the styles we
will need.

This is a great job for a computer, building styles that are easily
parameterized. The same is presumably possible in Word using an XML-ized
version of a document, but it is easy to do in Word's macro language,
and there is an existing macro from my past we can adapt.

The bad news about OO.o is that the macro language is a horror, worse by
far the Word's VBA and recording a macro to generate lists generates a
tiny bit of usable code, some commented-out code (!) and some big gaps
where it records nothing. Lucky the file format is easy to hack. And
another thing about OO.o; while it has an 'export as XHTML' with a
hackable stylesheet, it only works properly for images if you run the
stylesheet on a saved document that you have unzipped.

The second trick was also easy but it took two weeks of very part-time
mucking around to figure it out, during which time I explored all sorts
of dead-end solutions that weren't.

The problem was how to take a flat list of lists as spat-out by OO.o
(leaving out the items in the lists):

    <text:unordered-list text:style-name="l1">
    ...
    </text:unordered-list>
    <text:unordered-list text:style-name="l2">
    ...
    </text:unordered-list>
    <text:unordered-list text:style-name="l1">
    ...
    </text:unordered-list>

And get the middle list to embed in the first and the third to become
part of the first.

    <ul class="l1"> 
    ... 
    <li> …<ul class="l2*"> ... </ul></li>
    </ul>

I worked out early on that the solution was going to involve processing
item by item using the 'following-sibling' axis. So you start with the
first list, and it will call the next one, which may become embedded in
the first. The trick is to take two runs at it. One in 'embed' mode,
where you let things nest in each other, the second in
'find-more-at-the-same-level' mode, where you ignore anything that is
embeddable and look for the continuation of the list you are already in,
both of them called recursively.

Code for both of the above is coming as part of a first-release OO.o
Writer template, as soon as I have enough to be usable. Maybe later this
week.
