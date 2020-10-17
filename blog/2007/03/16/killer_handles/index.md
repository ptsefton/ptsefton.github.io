---
Title: "A killer app for handles"
Slug: killer_handles
Date: 2007-03-16

---
<div>

I've touched on **persistent identifiers** in general and **handles** in
particular here a couple of times[. One
time](http://ptsefton.com/blog/2006/11/01/identify_me) I wrote about
plain text citations. [Another time
I](http://ptsefton.com/blog/2006/11/01/repository-maintenance) looked at
migration issues. I've been what you might call a bit of a handle
sceptic, 'cos I didn't really see how they fitted with real-life web
based repositories, but for the first time this week I think I can see
new services built to exploit handles could really make life easier.
I'll go through a bit of background on the issues first, then look at
what I think may be a killer app for handles. Killer enough to consider
using them sooner rather than later, anyway.

# <span id="id31"></span>About handles

I [speculated](http://ptsefton.com/blog/2006/11/01/identify_me) a while
ago about whether a full-text citation, makes a good persistent
identifier for a conference paper. The answer was sort of no, as far as
automated lookup goes, although the clues offered by a text citation
mean you can do some detective work to find something.

Another approach to naming things is to use a **handle**. A handle is a
name with some special properties, and is backed some computer
infrastructure designed to help you find the digital object that the
handle names.

Lets look at a real example.

Here's a handle: `1959.1/2635`

This is a name that's guaranteed to be unique within the handle
infrastructure. It might also be a part number for a low cost
cutting-edge high-performance fibre-composite prosthetic chicken foot,
made by a small company in Gatton, but that's irrelevant.

The handle website
[explains:](http://handle.net/overviews/handle-syntax.html)

> Within the handle namespace, every identifier consists of two parts:
> its handle prefix, also known as a "naming authority", and a suffix or
> unique "local name" under the prefix. The prefix and suffix are
> separated by the ASCII character "/". An identifier may thus be
> defined as
>
> **\<Handle\> ::= \<Handle Prefix\> "/"\<Handle Suffix\>**
>
> For example, "10.1045/april2006-paskin" is an identifier (also known
> as a Digital Object Identifier (DOI), an implementation of the Handle
> System) for an article published in D-Lib Magazine. It is defined
> under the prefix (naming authority) "10.1045", and its suffix (local
> name) is "april2006-paskin".
>
> http://handle.net/overviews/handle-syntax.html

What can you do with the handle known as `1959.1/2635?`

You can go to a handle resolver and ask it to take you to the object.

1.  Go to <http://hdl.handle.net/>

2.  Put the handle, `1959.1/2635` in the handle box.

3.  Leave the checkboxes alone, I won't discuss those.

4.  Hit Submit.

Within a second or two you'll be looking at something like this:
<http://arrowprod.lib.monash.edu.au:8000/access/detail.php?pid=monash:2635&datastream=>

Of course when you read this post the URL that the handle resolver takes
you to might be different. But the idea is that if you use the resolver
then you'll always get the metadata summary page for a paper in the
Monash University institutional repository even if they change the
software.

Now, that page says:

> Please use this identifier to cite or link to this
> item:http://arrow.monash.edu.au/hdl/1959.1/2635

So if I were to mail you a link, that's the one I'm supposed to use. I
could just mail you the handle and assume that you'd know what to do
with it but I'm not that mean.

So, there are quite a few ways to refer to this thing:

1.  <http://arrow.monash.edu.au/hdl/1959.1/2635>

2.  hdl:1959.1/2635

3.  <http://hdl.handle.net/1959.1/2635>

4.  <http://arrowprod.lib.monash.edu.au:8000/access/detail.php?pid=monash:2635&datastream=>

5.  <http://arrowprod.lib.monash.edu.au:8000/access/detail.php?pid=monash:2635&datastream>

The Monash folks would like you to use the first option, so lets call
that the *canonical URL*. This would mean that in future they could get
rid of the redirect step when you end up looking at a messy looking URL,
lets call that the *messy URL*, instead of the the canonical URL.

The last example is a problem. That's the messy URL minus the last '='.
Unfortunately that works. This is unfortunate because it's an easy error
to make, and it will work, but that link is highly likely to be
non-persistent.

I bet lots of people will just copy the messy URL from the address bar.
Some might even think that there's something odd going on when they use
the URL they are requested to use but the browser changes it on them.

> http://arrowprod.lib.monash.edu.au:8000/access/detail.php?pid=monash:2635&datastream=

Which means a maintenance headache for the Monash repository minders. If
they upgrade their repository software in a way that will change the URL
for an item, which I happen to know they are planning to do, then they
will need to think about **redirecting** all requests for those old
fashioned messy URLs that used to work but no longer do.

This is easy enough to do: they need to tell the web server how to
recognize requests directed at old versions of the repository, yank out
the local identifier, `monash:2635`, cut it up, stick it together with
the handle prefix `1959.1` to make the complete handle `1959.1/2635` and
then redirect the request to a handle resolver. That's one line of
redirect code. (And there's a problem if the handles are not related to
the local identifiers, that simply won't work <span
class="spCh spChx2013">–</span> you'd need a lookup table)

There also needs to be an **ongoing commitment** from the institution
that as long as there's DNS (the bit that resolves the name
arrow.monash.edu.au to a particular Internet address) and HTTP (the
protocol your web browser uses to talk to the repository software) that
they will keep the redirect in place. Ongoing commitment is a policy and
governance thing. It's about putting processes in place to ensure that
future systems don't break things that used to work. So the simpler the
thing you commit to, the more chance there is that future generations
will be able to keep it up.

I used to think that because you had to do this redirect stuff anyway
that buying in to handles was just another thing to worry about. Another
mouth to feed. Handles are not just for Christmas.

But what if the handles stuff actually helped?

# <span id="id32"></span>A killer app (or two) for handles?

Lyle Winton from the [PILIN](http://www.arrow.edu.au/PILIN) project has
**proposed a really nice sounding service**, *findurl*. Instead of
having to work out a bit of complicated redirect-code that parses a
request and works out where to redirect it for each and every bit of web
software you ever install, why not ask a new handles service to find it
for you? Send it the old URL and it will look for the handle record that
lists the URL in question, then redirect you to the new home for the
object.

This means that for any handle-enabled site you only need to commit to
maintaining one teensy bit of redirect code. It would be saying <span
class="spCh spChx201c">“</span>Looks like this request is for something
I can no longer serve. Lets send this request on to the `findurl`
service<span class="spCh spChx201d">”</span>.

(If the software has had multiple ways of viewing the same record with
different URLs then a smarter redirect than a simple findurl might be
appropriate. But for migrating from a well-behaved system findurl looks
to me like a really simple solution)

A second killer app would be **handle resolver which can act as a
proxy** rather than a redirector. That is you'd go to the canonical URL
for an item at Monash, and instead of it redirecting you it would fetch
the page itself and display it in the browser so you'd request this:

> http://arrow.monash.edu.au/hdl/1959.1/2635

And without any redirect shenanigans you'd be looking at the metadata
page for the item. (This is already on the wish list for the software
vendor to provide in future.)

This handle-proxy service may also be useful at a cross-institution
level. Take the Australian Government. Departments change their names,
appear, disappear, merge and split all the time. A government-wide
handle-proxy for things that should have a long life and a stable name
would be really useful.

There's lots more to think about with handles that I have covered here,
obviously. But if you take the Monash approach of hosting your own
handles services then I think you are probably pretty safe.

</div>
