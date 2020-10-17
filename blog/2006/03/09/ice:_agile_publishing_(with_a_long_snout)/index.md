---
Title: "ICE: Agile Publishing (with a long snout)"
Slug: ice:_agile_publishing_(with_a_long_snout)
Date: 2006-03-09

---
<div>

There's a piece over at XML.com called [The Emerging Art of Agile
Publishing](http://www.xml.com/pub/a/2006/03/08/agile-publishing.html).
(I [have articles](http://www.xml.com/pub/au/245) there too, you know.)

This resonates really well with the work we are doing on ICE.

Under the heading **Interleaving** we get
[this](http://www.xml.com/pub/a/2006/03/08/agile-publishing.html), which
could almost be advertising copy for ICE:

> Interleaving is a style of work where tasks are integrated with other
> tasks and among groups, not just held by individuals in missile silos
> until launch time. For example, I normally write in my cave, an
> 11-by-17 office above our garage, for weeks or months before an editor
> sees my work. Why? Because my chapter or article is stored exclusively
> on my hard drive.
>
> If our work were interleaved, it could be stored in an online
> Subversion repository that could be accessed by <span
> class="ACRONYM">HTTP</span>. Then the editor could read the message
> logs or "check out" what was going on anytime. Intrusive
> micromanagement? No, because we communicate with and trust each other.
> We help each other instead of yelp at each other. It keeps us clear,
> accountable, and unstuck.

Yep. ICE uses Subversion repositories. If you download ICE the first
thing it does is check-out some sample content from a Subversion
repository, and you can set up your own local repository in seconds
(hint, in the current version look in the config.xml file, in future
versions there will be a web interface).

You can look at the Subversion repository for ICE's documentation [via
our Trac
software](http://ice.usq.edu.au/browser/ice/downloads/latest/documentation/packages/ice-guide/).
That shows you the source files which are OpenDocument documents. If you
want to see what ICE produces, download the [zipped
documents](http://ice.usq.edu.au/file/ice/downloads/latest/documentation/packages/ice-guide/ice-guide_template.zip?rev=2633&format=raw),
you'll see an HTML version, and PDF for the whole book, and for each
part of the book.

I'm at home tonight typing this on a Windows machine running OpenOffice,
when I'm finished I will send it via Subversion to my \$25 Linux server,
check it out on another Windows machine a metre away and format it using
ICE before sending it up to my blog in the USA (don't try this at home,
kids). When I get to work tomorrow ICE will use Subversion to get
tonight's changes onto the Mac.

In a less onanistic context we use ICE to share documents at work. Cam
writes a newsletter and syncs-up using ICE, the rest of us sync it to
our ICE servers running on our computers and check his work 'cos he has
a habit of misspelling our names. For some reason he spells Dr Sefton
“Dr Sloppy”.

There's more from Michael Fitzgerald at xml.com:

> Another way of interleaving work is to share tools. If I were a
> production editor, I might be working in the [Adobe
> FrameMaker](http://www.adobe.com/products/framemaker/main.html) editor
> to produce camera-ready copy for the printer. As a writer, I've worked
> in FrameMaker as well. Why not share the same tool? It would cut out a
> lot of time if we both used the same tool. Too much time is eaten up
> converting and munging files from one format to the other, to say
> nothing of the cleanup required. Uncommon? Yes. Impossible? No.

Right, we use the same tool in the production department as the authors
use. Well, sort of. See, we use the [ICE
template](http://ice.usq.edu.au/browser/ice/downloads/latest/templates/)
which is allows some people to work in Word and some in OpenOffice.org.
Behind the scenes ICE uses OpenOffice.org to make PDF books, and HTML
pages all linked up into nice little web sites. We could add FrameMaker
to the mix pretty easily, but looks like OpenOffice.org is good enough
for what we need. Maybe [Adobe
InDesign](http://www.adobe.com/products/indesign/main.html) one day?

And I could have quoted Michael Fitzgerald in a post I wrote tonight
about ['spinning' in project
management](http://ptsefton.com/blog/2006/03/09/project_management_is_like_pedalling_a_bike):

> Writing and editing, in my view, are better experienced in bite-sized
> portions. So divide the work in pieces with short cycles. In other
> words, write short chapters, or divide longer chapters into smaller
> sections, and then turn the chapter or section over to your editor.
> She will likely turn it around quickly, because it is no longer a
> daunting task, hovering in her inbox.
>
> When the writing and editing happen in short cycles, there is more of
> a flow to the stream, rather than breaching log jams. See what I mean?
> If the work flows more smoothly, there is less opportunity for
> contention among teammates, and more opportunity for frequent, rapid
> exchanges of work among them. When the work starts to flow, momentum
> builds, and the momentum itself helps the
> flow.['](http://ptsefton.com/blog/2006/03/09/project_management_is_like_pedalling_a_bike)

Again, this is what ICE is doing for us in the RUBRIC team; we have all
our stuff there on everyone's desktop. Very easy it is to take a peek at
a colleague's work, add a bit, and sync-up.

In the future we'll add annotation features to ICE so you can comment on
other people's stuff without actually changing it.

As usual, I point out that ICE is an early-release bit of software.
Still on parole as it were.

We are getting good results at USQ with a number of courses being
published using the system, and it's helping us a lot on the
[RUBRIC](http://www.rubric.edu.au/) project, but you can expect bugs at
this stage, mainly in the area of Subversion interaction. We have not
found and dealt with all the issues that come about when people and
too-helpful software create and delete files and confuse poor Subversion
which is trying to keep track of everything, under ICE's command. But if
you're game, [download it](http://ice.usq.edu.au/)and [drop me a
line](mailto:pt@ptsefton.com) if you have problems.

****

</div>
