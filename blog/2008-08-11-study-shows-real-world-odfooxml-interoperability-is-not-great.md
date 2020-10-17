---
Author: ptsefton
Comments: true
Date: 2008-08-11 00:31:24+00:00
Slug: study-shows-real-world-odfooxml-interoperability-is-not-great

Title: Study shows real-world  ODF/OOXML interoperability is not great
Wordpress_id: 179
---

<div>

<div class="page-toc">

</div>

<div>

Via [Doug
Mahugh](http://blogs.msdn.com/dmahugh/archive/2008/08/09/links-for-08-09-2008.aspx)
at Microsoft comes [this
study](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1201708) (Shah
& Kesan 2008)<span class="spCh spChx2060">⁠</span> on interoperability
of word processing applications using the Open Document Format and
Office Open XML.

After outlining some possible approaches to testing conformance of
applications against the standards and pointing out what a gargantuan
task that would be, they settle on a pragmatic approach: **test
interoperability with the dominant application for each format**.

> This research tested the interoperability for ODF and OOXML document
> formats based on a reference implementation approach. For ODF, the
> test documents are developed in OpenOffice, which is currently the
> dominant implementation for ODF. For OOXML, the test documents are
> developed in Microsoft Office 2007 for Windows. These are not
> reference implementations in a true sense, because they do not
> perfectly implement the standard. However, they act as de facto
> reference implementations, because they are the dominant
> implementations that all developers seek compatibility with.

This makes perfect sense for real-world testing. The results are
interesting and unsurprising ([to me, at
least](http://ptsefton.com/2008/05/13/claims-about-odf-support-are-typically-meaningless.htm)).
Basically the best interoperability is between Microsoft Office Word and
OpenOffice.org Writer <span class="spCh spChx2013">–</span> even when
they are reading each other's formats. I reckon that would be because
the OOo team have invested person-decades of effort in reverse
engineering the Word document model, and Writer is more or less able to
deal with Word docs. The document serialization format is not that
relevant. It's the document models that count. And some of the
applications they test are not really even word processors.

This paper makes a great case that it is interop that counts and the
goes on to show how poor interop really is.

Unfortunately, this study didn't get as far as looking at styles
compatibility as that's one area where there are some frustrating
problems but also great opportunities to help in interoperability. If
you [use styles](http://delicious.com/ptsefton/ptsefton+usestyles) then
at least the semantics and structure of documents can be preserved even
if page fidelity is not.

And there's a way to **improve interoperability**. You don't have to
leave users to their own devices, you can advise them of which features
of which applications to use for particular tasks. This is what we try
to do on the [ICE project](http://ice.usq.edu.au/). We provide
[templates](http://ice.usq.edu.au/instructions/templates/toolbars_and_templates.htm)
and [advice](http://ice.usq.edu.au/packages/user_guide/default.htm) to
help people create interoperable documents.

Inspired by this paper, I'm off to start work on a paper looking at
**proactive interoperability**, by helping users to pick features that
**will** interoperate. As noted in this study there's not much out there
to choose from apart from Writer and Word. That's why we will continue
to work with Writer and Word looking for practical solutions.

Shah, R.C. & Kesan, J.P., 2008. Lost in Translation: Interoperability
Issues for Open Standards - ODF and OOXML as Examples by Rajiv Shah, Jay
Kesan. In *The proceedings of the 36th Research Conference on
Communication, Information and Internet Policy (TPRC), Arlington, VA
Sept. 26-28, 2008*. Available at: http://ssrn.com/abstract=1201708
[Accessed August 10, 2008].

</div>

</div>
