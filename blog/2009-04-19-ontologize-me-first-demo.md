---
Author: ptsefton
Comments: true
Date: 2009-04-19 06:07:21+00:00
Slug: ontologize-me-first-demo

Title: Ontologize me! First demo
Wordpress_id: 325
excerpt: Demo of an RDF triple encoded in a URL
---

<div>

<div class="page-toc">

</div>

<div>

While I was on leave after Easter, Duncan Dickinson [had a
go](http://blog.duncan.dickinson.name/2009/04/attempt-1-urls-with-semantics.html)
at implementing my idea for encoding RDF triples in a URL with a helper
site. He elaborates on that short post
[here](http://blog.duncan.dickinson.name/2009/04/easy-semantic-linking-for-authors.html).

I was also working on a little site. I have not gone very far with this,
but one thing I can do assert that I am the creator of this resource by
linking a variant of my name to the ontologize.me site: [Dr Peter M
Sefton](http://ontologize.me/meta/?r=http://purl.org/dc/terms/creator&o=http://ptsefton.com/about).
All it does so far is what you see there, it can decode a URL-encoded
RDF statement into English. In this case it will tell you that this page
has a creator identified by a URI.

So far I have not:

1.  Made a wizard/bookmarklet to create these links/

2.  Worked out how to get the same page to serve machine-readable RDF.

Another step will be to get [ICE](http://ice.usq.edu.au/) (or maybe use
jQuery) to encode the RDF as RDFa in the HTML that it produces and maybe
even to embed the same semantics in PDF, as per [Chris Rusbridge's
idea](http://digitalcuration.blogspot.com/2009/04/semantically-richer-pdf.html).

Note that we need different URLs to talk about metadata for a whole
resource, versus asserting that a term, such as Potter syndrome, is an
instance of a disease in an ontology, hence the `/meta/` in the URL I
have used above.

</div>

</div>
