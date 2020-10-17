---
Title: Supporting ProseMirror inline HTML editor
Date: 2015-09-01
Category: ScholarlyHTML
---

The world needs a good, sane in-browser editing component, one that
edits document structure (headings, lists, quotes etc) rather than
format (font, size etc). I've been thinking for a while that an
editing component based around Markdown (or [Commonmark]) would be
just the thing. Markdown/Commonmark is effectively a spec for the
minimal sensible markup set for documents, it's more than adequate for
articles, theses, reports etc. And it can be [extended] with document semantics.

Anyway, there's a [crowdfunding campaign] going on for an editor called
ProseMirror that does just that, and promises collaborative editing as
well. It's beta quality but looks promising, I chipped in 50
Euros to try to get it over the line to be released as open source.

The author says:

> ## Who I am
> 
> This campaign is being run by Marijn Haverbeke, author
> of CodeMirror, a widely used in-browser code editor, Eloquent
> JavaScript, a freely available JavaScript book, and Tern, which is
> an editor-assistance engine for JavaScript coding that I also
> crowd-funded here. I have a long history of releasing and
> maintaining solid open software. My work on CodeMirror (which you
> might know as the editor in Chrome and Firefox's dev tools) has
> given me lots of experience with writing a fast, solid, extendable
> editor. Many of the techniques that went into ProseMirror have
> already proven themselves in CodeMirror.

There's a lot to like with this editor - it has a nice floating
toolbar that pops up at the right of the paragraph, with a couple of
non-quite-standard behaviours that just might catch on. Mostly works,
but has some really obvious <strike>bugs</strike> usability issues ,
like when I try to make a nested list it makes commonmark like this:

    * List item
    * List item
    * * List item

And it even renders the two bullets side by side in the HTML view.
Even thought that is apparently supported by commonmark, for a prose
editor it's just wrong. Nobody *means* two bullets unless they're up
to no good, typographically speaking.

The editor should do the thing
you almost certainly mean. Something like:

    * List item
    * List item
      * List item

But, if that stuff gets cleaned up then this will be perfect for
producing [Scholarly Markdown], and [Scholarly HTML]. The $84 AUD
means I'll get priority on a reporting a bug, assuming it reaches its
funding goal.

[Commonmark]: http://commonmark.org/
[crowdfunding campaign]: (https://www.indiegogo.com/projects/1301159)
[Scholarly Markdown]: http://scholarlymarkdown.com/
[Scholarly HTML]: https://github.com/scholarlyhtml
[extended]: http://ptsefton.com/2014/06/26/we-are-not-dinosaurs.htm
