---
Title: "Does a text citation make a good persistent identifier?"
Slug: identify_me
Date: 2006-11-01

---
<div>

We've been talking about persistent identifiers at RUBRIC: how are
people going to name the things in their repository so they can be cited
and located in the future? We're looking to the  PILIN project (read a
presentation in
[PDF](http://www.arrow.edu.au/docs/files/PILIN-IDEA-20061010.pdf) or
[text](http://www.arrow.edu.au/docs/files/PILIN-IDEA-20061010.txt)) for
some advice. Expect to see more on this topic here over the next few
months.

Lots of repositories use [Handles](http://www.handle.net/) to name
things and the handle infrastructure for naming things and storing
metadata about them is pretty impressive; but others, like USQ have yet
to buy-in and [some
people](http://norman.walsh.name/2006/07/25/namesAndAddresses) think
that URIs are perfectly good names. Me, I'm still confused.

Anyway, a practical problem: how do you refer to an item in the [USQ
ePrints repository](http://eprints.usq.edu.au/)?

How about a plain-text citation? This identifies something; it's a
perfectly good name.

> "Sefton, Peter (2006) The integrated content environment. In:
> AusWeb06: The 12th Australasian World Wide Web Conference, 1-5 July
> 2006, Noosa, Australia."

My theory was that I could use Google as a resolver to find versions of
the paper by doing a phrase search but that doesn't work. The full
citation with the quotes yields nothing. Without the quotes Google takes
me to the ePrints [page](http://eprints.usq.edu.au/archive/00000697/).
But
[Yahoo](http://search.yahoo.com/search?ei=UTF-8&fr=sfp&p=Sefton%2C+Peter+(2006)+The+integrated+content+environment.+In%3A+AusWeb06%3A+The+12th+Australasian+World+W)
finds it using a phrase search. So does
[MSN](http://search.ninemsn.com.au/results.aspx?q=%22Sefton%2C+Peter+(2006)+The+integrated+content+environment.+In%3A+AusWeb06%3A+The+12th+Australasian+World+Wide+Web+Conference%2C+1-5+July+2006%2C+Noosa%2C+Australia.%22&geovar=70&FORM=REDIR).

USQ ePrints has a version of the paper in PDF format but the actual
paper is available from the conference web site in HTML format. As I
write this there's no link from ePrints to the version at the
conference; I'll see if I can get that added.

You can find the version of the paper at the conference web site by
searching  for AusWeb06, then clicking through the[days of the
program](http://ausweb.scu.edu.au/aw06/papers/refereed/sefton/index.html)
(I was on Tuesday).

There is a also a paper version of the proceedings – so of course you
can [find that](http://nla.gov.au/anbd.bib-an000040588911) via  the
National Library of Australia. (I searched to ausweb06). That finds the
proceedings of the conference: *AusWeb06 : Making a Difference with Web
Technologies / Treloar, Andrew(ed), Ellis, Allan(ed).* Maybe we could
update the ePrints repository to use this as part of the citation but if
we do that then the links in this post will eventually break – the
citation I used  in this post will no longer be there.

At this stage its looking like the plain text citation is not a
particularly good persistent name if you want automated resolution, but
on the other hand a human being can use it find the paper, and it should
work in a post-Internet world.

My understanding of handles is that you should be able to link all the
different versions of the paper by storing URLs as metadata against a
single name, the handle resolver service could be used to point to any
one of those versions, or you could make a service that threw up a page
where people could choose.

The handle could, in theory be like this (where n would be a number):
`1959.n/"Sefton, Peter (2006) The integrated content environment. In: AusWeb06: The 12th Australasian World Wide Web Conference, 1-5 July 2006, Noosa, Australia."`

Except that I have heard some people say that this kind of  local name
(that's the bit after the /) is a bad idea and names should be
meaningless. I don't understand that bit yet – maybe it's because of the
issue I noted above with the wording of the citation.

We're working through lots of practical issues to do with naming, citing
and locating things on the [RUBRIC](http://rubric.edu.au/) and
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm)projects – more
soon.

</div>
