---
Title: "Deep structure vs word processing"
Slug: editing_structured_documents
Date: 2005-01-29

---
Jon Udell has been thinking and writing about ways to edit the essence
of a computer program rather than the textual view, in the [*Deep
structure of
code*](http://weblog.infoworld.com/udell/2005/01/19.html#a1154), and has
posted a
[follow-up](http://weblog.infoworld.com/udell/2005/01/20.html#a1155)
with some reactions. He's still wondering if the text editor emacs "will
ever be pried from my [Jon's](jon's) cold dead fingers". I have some
thoughts on how this discussion relates to editing text, rather than
programs.

This [reaction](http://bannister.us/weblog/?p=192) from Preston L.
Bannister struck a chord with me, not so much for editing code, but for
its relevance to editing structured *text*.

> Back in college, after we had all played with structure editors for a
> time, one member of our group identified the source of our discomfort
> by noting that many simple common operations in a text editor were
> much more complicated in a structure editor.

This is relates to the task I have at USQ; to help people use the XML
publishing system. I've played with the chosen (XML) structure editor
and particularly didn't like the experience of trying to rework a
document by splitting a section into two parts, which would have been a
matter of applying one heading style in an word processing environment,
but was a complex set of steps in the validating XML editor. Nor would I
like to try the same thing in emacs for the first time, although I do
use it for writing code. Both approaches, the text-based and the
tree-based compare very unfavorably to Microsoft Word's outline feature
where reorganizing a word document using the outliner and well designed
styles is a joy. In some sense Word is a structural editor but it's not
all that fussy. What makes this part of it nice to use?

-   No constraints, your document is never broken, according to Word (of
    course, this is a problem too).

<!-- -->

-   Structure is *implied* by the application of styles (and I can't
    resist pointing out that natural language does this a lot, look at
    the way chains of reference are interleaved through text with no
    trees in sight) - there are no inherent structures to get in the
    way.

<!-- -->

-   The structures that do exist are not in a single tree, you can look
    a the outline structure in one tree view but there are other
    structures that can cut across it, for example tables. (So why can't
    we do this with XML namespaces - why do all the elements have to be
    in one tree. 'Cos it's easier to parse I suppose.)

This niceness comes at a cost, at least if you're an XML structure
Naz\^H\^H\^H type of person, because there's no way of enforcing all
those XML rules, but the Word Processor has evolved to serve people who
didn't worry about that, and along with all the stupid 'features' and
[regressive tendencies in Word](blog/2005/01/20/templates_atrpohy) are
some very well designed writing tools for general-purpose writers.

I am fascinated by this space - what will evolve to allow more
structure, while keeping the fluidity of a word processing environment?

By the way, the metaphorical 'depth' in this discussion bothers me a
bit. I was trained, or persuaded (mainly by one [Christian
Matthiessen](http://minerva.ling.mq.edu.au/xian/CM_Resume.html)) to
think about language in spatial terms too but the 'surface' realization
of language was usually drawn down low, with syntax and semantics and
context of culture *up* and *out* and *around*, giving you a sense that
utterances are embedded (deep, if you like) in the surrounding language
and culture, the opposite of the idea that the representation in text is
*above* something deeper, presumably reflecting a more biological
starting point with the surface at your mouth and the 'deep' bit
somewhere inside your brain.

\$LastChangedDate: 2005-02-04 16:36:55 -0600 (Fri, 04 Feb 2005) \$
