---
Author: ptsefton
Comments: true
Date: 2008-12-01 20:07:07+00:00
Slug: embargoes-on-bits-of-theses-skating-on-thin-ice

Title: 'Embargoes on bits of theses: skating on thin ICE?'
Wordpress_id: 256
---

<div>

<div class="page-toc">

</div>

<div>

I gave myself a [task](http://ice.usq.edu.au/trac/ticket/6280)[<span
style="vertical-align: super;"><span
class="footnote">\*</span></span>](#ftn1) after the last
[TheOREM-ICE](http://development.jisc.ac.uk/whatwedo/programmes/digitalrepositories2007/theoremice.aspx)
teleconference to look into how ICE might be used for fine-grained
thesis embargoes.

I have not seen a full spec but I gather from the conversation that
sometimes you want to make a thesis available but place some of the
data, or maybe a chapter or two under embargo. Jim Downing proposed that
a repository would still advertise the
[ORE](http://www.openarchives.org/ore/) resource map of the thesis on
the web but some parts would be unfetchable by anonymous access until
the embargo period is expired. Could we use ICE to do that?

Maybe not such a good idea.

I'll talk here about *why* not, and outline some other possibilities. Of
course you should be cautious when I start talking like this 'cos based
on prior form I'm probably really just trying to get money to start a
new software development or integration project.

For a start embargoes are really quite different from the sorts of
access you want in an authoring system, being time based for a start and
they have to work on the wide web rather than the intranet and this
stuff happens when the thesis finished, so it really should be out of
the document authoring system at that point.

ICE is designed for document authoring and collaboration and only has
fairly broad-brush access control. In the courseware we work with access
is by a whole team to a whole course. For a thesis it is similarly
simple, you have the ability to add stuff and your supervisor can
comment. I'm not at all sure that it would make sense to add complex
document-level access features to ICE, instead why not concentrate on
the ICE templates and conversation system? That is the bit we do better
than anyone else that I know of. We could integrate the templates into
other systems and leave the business of writing content or document
management systems to all the other contenders. (One reason why not is
that many CMSs are pretty hopeless at managing multiple renditions of
the same content and don't have plug-in convertors but there must be at
least some we could work with.)

I'm not at all sure that ICE itself should be pushed too much further
into thesis management past the authoring stage. It certainly looks like
it would be good for drafting a thesis and getting your supervisor to
comment, and it's definitely on the cutting edge of being able to mashup
document content with data visualization, but we don't have all the
elaborate approval and review steps that you'd need for the internal and
external processes that follow. One promising lead springs from the way
that the Maths & Computing department here at USQ use the [Open Journal
Systems](http://pkp.sfu.ca/?q=ojs) (OJS) to manage theses. We're
[exploring the idea of an ICE/OJS
mashup](http://ice.usq.edu.au/trac/query?status=new&status=assigned&status=reopened&status=closed&component=PKP&order=priority).
Stay tuned for a report from the [APSR Open Access Publishing
Workshop](http://www.apsr.edu.au/open_access_publishing/) later this
week where I will put this idea and many others to the technical stream.

For delivery I think [The
Fascinator](http://ice.usq.edu.au/projects/fascinator/trac) might be a
good way to manage the kind of embargoed access that the TheOREM team
have identified as a requirement. ICE could manage the authoring, with
examination via something like OJS and then use an ORE resource map to
pass the thesis to a departmental or institutional repository running
The Fascinator, which IS designed to do access control. It could then re
publish the resource map to the world-wide repository grid and manage
the embargoes. Either at the examination stage, or at the repository
deposit stage the candidate would set up the embargoes, which would need
to be kept as metadata against the components of the thesis.

Thinking about this led me to the idea of putting something like The
Fascinator on the desktop, letting it find all your stuff, giving you a
simple way to organize it into projects, embargo bits of it and so on,
and then automate the process of disseminating it to the institutional
and other places you'd like it go. I'm thinking of something like Picasa
(which finds all your pictures on your hard drive no matter how
embarrassing or not safe for work they are) and iTunes which [although
in my opinion potentially
evil](http://ptsefton.com/2008/04/24/some-thoughts-on-vendor-lock-in-from-the-domestic-to-the-institutional-is-apple-mac-os-x-evil.htm)
has some nice ways of browsing and organizing content, but with a
connection to the world wide repository grid. More on this idea soon.

------------------------------------------------------------------------

<div style="font-size: .9em;">

<span class="footnote"></span>
[\*](#ftn1-text) We're doing this project more or less in the open so
you can poke around and see what we're up to.

</span>

</div>

</div>

</div>
