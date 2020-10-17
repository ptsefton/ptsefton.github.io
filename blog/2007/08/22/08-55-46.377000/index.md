---
Title: "URIs as tags"
Slug: 08-55-46.377000
Date: 2007-08-22

---
<div>

[View this page as PDF](/blog/2007/08/22/08-55-46.377000/100.pdf)

# <span id="id1"></span>RDF

[RDF](http://www.w3.org/RDF/) is a Good Thing, I gather, for metadata
but I have been slow to get started with it.

Here's part of the current Wikipedia summary:

> The RDF metadata model is based upon the idea of making statements
> about resources in the form of subject-predicate-object expressions,
> called triples in RDF terminology. The subject denotes the resource,
> and the predicate denotes traits or aspects of the resource and
> expresses a relationship between the subject and the object. For
> example, one way to represent the notion "The sky has the color blue"
> in RDF is as a triple of specially formatted strings: a subject
> denoting "the sky", a predicate denoting "has the color", and an
> object denoting "blue".
>
> (Wikipedia contributors 2007)

# <span id="id3"></span>Neil's Godfrey's idea

In an email this morning [Neil
Godfrey](http://metalogger.wordpress.com/) of the RUBRIC project asked
if we should assign a del.icio.us tag for each item in an institutional
repository. That's a very very interesting idea. You could provide a
virtual repository that way.

Bbut the immediate issue is how would you express the metadata?

If we're describing an item in a 'normal' repository they you can can
say the author is Peter Sefton (or PT Sefton, or Petie Sefton, or Dr
Peter Sefton, Petey Sefton, or Daddy). So that's predicate:author with
object <span class="spCh spChx201c">“</span>Peter Sefton<span
class="spCh spChx201d">”</span>.

So how would I do this in del.icio.us?

Use separate accounts for different predicates
:   I could make a del.icio.us account for describing authors say
    `usq_repos_predicat`e`_dc_creator`, and tag all the authors using
    that account. So you could decide on a canonical representation for
    each author in tag form and use the special account. A tag for me
    might be Peter\_Malcolm\_Sefton\_1979-08-09 (if I wasn't lying about
    my age :-).

Conflate the predicate and the object
:   You could make up tags that had both the predicate and the object in
    them. So the tag might be
    ` dc_creator:Peter_Malcolm_Sefton_1979-08-09`.

Use a URI
:   The semantic web dream, as I understand it is to be able to use URIs
    wherever possible for in RDF descriptions. I tried this morning, and
    guess what? Del.icio.us seems to be accept URLs as tags (but they
    don't actually work properly so you can't use them to see things
    only tag things).
:   Returning to [the issue of how to identify a
    person](http://ptsefton.com/blog/2006/06/06/the_affiliation_issue_in_institutional_repository_software),
    what we'd really like to be able to do is to find a unique
    identifier for each bit of metadata that might appear in more than
    one place. So, rather than having strings all over the place, like
    different versions of my name, I would have a way to use a unique
    identifier.
:   If Wikipedia let you add entries for anyone at all, then that would
    be easy <span class="spCh spChx2013">–</span> you'd either find or
    create a record for the person. So I could use this is a URI/tag for
    myself. Note that I've added a predicate to the URL to show that
    we're talking about my role as an author and a ;manifestation' of my
    name which is the string that's used to refer to me in this
    instance.
:   <http://en.wikipedia.org/wiki/ptsefton?predicate=dc:creator&manifestation=Peter%20Sefton>
:   (Might be better to use three tags <span
    class="spCh spChx2013">–</span> one with just my name with not
    relation one with a predicate and one with a manifestation to allow
    better querying.)
:   But (a) It's wrong to make a page for myself and (b) it would be
    removed anyway, although I suppose one could just use the URI.
:   This scheme would let you find all the things I've authored across
    the whole of del.icio.us, if it worked. One could conceivably build
    harvesting technology to automate this. The problem remains, thought
    hat there's no single authoritative source for author names.

# <span id="id5"></span>What I did

To test this out, I have made a new tag that means something was
authored by me. It's a URI that points to a page about me on my website.

<http://ptsefton.com/pt?predicate=dc:creator>

I have used del.icio.us tag management to tag everything on my website
as being written by me. And I've been off to a couple of other places on
the web that have things I wrote and used that tag.

But sadly, while del.icio.us lets you **make** the tag, it doesn't work
to **view** the tag. So you can see the tags here amongst the other tags
on my account:

[http://del.icio.us/ptsefton/](http://del.icio.us/ptsefton/http://ptsefton.com/pt%3Fpredicate%3Ddc:creator)

But if you click on the tag it doesn't work (as of today):

<http://del.icio.us/ptsefton/http://ptsefton.com/pt%3Fpredicate%3Ddc:creator>

# <span id="id6"></span>Conclusion

I think Neil Godfrey might be onto something here, with his idea of
tagging stuff in repositories, but I'm not sure what it is.

The tags I've created seem to me to be able to bundle together a
predicate (is-author) with a object (an author), but we still have the
problem that there is no common way to identify authors with a URI.

# <span id="id7"></span>References

Wikipedia contributors. 2007. Resource Description Framework.
*Wikipedia, The Free Encyclopedia*, August 15.
http://en.wikipedia.org/w/index.php?title=Resource*Description*Framework&oldid=151387368
(accessed August 20, 2007).

</div>
