---
Title: "Administration overheads for repository maintainers: remapping old names"
Slug: repository-maintenance
Date: 2006-11-01

---
<div>

Taking on a repository requires responsible maintainers prepared to look
after it for a long time. It's not just for Christmas.

Lets consider the case where an organization decides to migrate their
content to a new bit of repository software, such as
[Fez.](http://dev-fez.library.uq.edu.au/)

Lets take three universities: call then a, b, and c. Actually they're
USQ, Swinburne and Monash. As far as I know none of these institutions
are thinking about migrating their repositories to Fez it's just an
example, OK?

University a has a repository: at the moment it's based on the [GNU
EPrints](http://www.eprints.org/software/) software. A URI for a paper
looks like this: <http://eprints.usq.edu.au/archive/00000697/> . In a
Fez repository the a URI looks like this:
<http://espace.library.uq.edu.au/view.php?pid=UQ:542> so, to migrate USQ
staff will have to set up some web server configuration to map incoming
requests for EPrints-style URIs to the correct form for Fez; a fairly
straightforward bit of web server admin.

University b uses handles, and currently has a repository running on
version 2 of the VTLS Vital software. A record in that repository will
tell you to use a link to the handle.net resolver:

> Please use this identifier to cite or link to this item:
> <http://hdl.handle.net/1959.3/2394>

Click on the link and you find yourself looking at this resource:
[http://researchbank.swinburne.edu.au:8000/access/detail.php?pid=swin:2394&datastream=](http://researchbank.swinburne.edu.au:8000/access/detail.php?pid=swin:2394&datastream)
That's a VITAL URI. Now, while the page clearly states to use the
handle-style URI, I bet that plenty of people will have cited things in
the repository using whatever they can copy out of the address bar on
their browser, so the Swinburne people may choose to do (1) the same
kind of web server configuration as USQ to remap vital links to Fez
links, and (2) additionally update their handle server so that the local
name *2394* is mapped to the correct service.

Now, consider university c. Their links look like this:
<http://arrow.monash.edu.au/hdl/1959.1/2658> They've got their own
handle resolver at arrow.monash.edu.au. To move to Fez they'd have
exactly the same amount of work to do as Swinburne. But if they decide
to change their handle infrastructure then they will have to do
something about requests coming to that domain. And its not unreasonable
to expect that handle infrastructure might change, there is talk on the
PILIN project (read a presentation in
[PDF](http://www.arrow.edu.au/docs/files/PILIN-IDEA-20061010.pdf) or
[text](http://www.arrow.edu.au/docs/files/PILIN-IDEA-20061010.txt))
about considering national infrastructure in Australia for handles.

(National infrastructure would be a big plus for government, where
departments appear and disappear regularly. One day we might even do
away with state governments here in Australia. And like it or not, some
universities may be subsumed into others or even dismembered and shared
out. In these cases it would be difficult to keep up a culture of
rewriting URLs for long-forgotten systems on obsolete domains.)

Of course, the managers of the handle-enabled repositories could just
decide to not support the application-specific linking – but I think
that would be a bad idea – lots of citations will go missing unless URIs
are remapped.

Here's a thought. Could the VITAL team and the Fez team settle on a
common way of displaying an item record with nice clean paths, EPrints
style? Anything wrong with `/archive/ `? At least lose the `.php`!

That would make migration easier, particularly in the case of the
university of Queensland where old URLS to the GNU ePrints software
would *just work* when migrated. We could take out the step where you
have to reconfigure your web server to migrate between repositories.
(Note to self: must check with VTLS what they plan to do about this for
Version 3 of VITAL which has a new architecture).

I'm sure VTLS would like to make it easier for Fez users to upgrade to
VITAL and the Fez team are always looking for new community members.

</div>
