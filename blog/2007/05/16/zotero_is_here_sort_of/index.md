---
Title: "Zotero provides cross-platform bibliography solution for authors. Sort of."
Slug: zotero_is_here_sort_of
Date: 2007-05-16

---
<div>

If you are regular reader, and you read posts here all the way to the
bottom, then you will have seen the [previous
post](http://ptsefton.com/blog/2007/05/16/handles_curation_boundary), in
which there was an **actual bibliography**. This means that we now have
a working if shaky and tentative way to do bibliographies in Microsoft
Word and OpenOffice.org, as part of the
[ICE-RS](http://ice.usq.edu.au/introduction/ice_rs.htm) project.

I can now use the magnificent Firefox plugin known as
[Zotero](http://www.zotero.org/) to build a library of references. I
find that it works pretty well to auto import for things found via
Google scholar. But it's sobering to be subscribed to the forums in
Google Reader and to see all the posts like the scary <span
class="spCh spChx201c">“</span>[Library gone
missing](http://forums.zotero.org/discussion/825/library-gone-missing/#Item_0)<span
class="spCh spChx201d">”</span> (which turned out to have a reasonably
happy ending except that I worry about Cate having all her references
for her thesis in Zotero <span class="spCh spChx2013">–</span> how
should she back it all up?).

And thanks to [Ian Laurenson](http://forums.zotero.org/account/752/) who
has been doing some work for the ICE project, we now have an
OpenOffice.org version of the original Zotero word plugin which solves
the issue I noted in my [previous
post](http://ptsefton.com/blog/2007/03/05/zotero_word_processor). You
can read about
[progress](http://forums.zotero.org/discussion/804/word-plugin-status-update/)
on the forums. Ian has done a great job with the plugin. He worked out
how to use the same codebase for both Writer and Word which both use a
kind of Basic, using compiler directives to put platform specific code
in where it is needed. Other stuff Ian's been helping with will appear
soon.

We have some early prototype Zotero plugin code that works in Word for
Windows and Mac and various flavours of OpenOffice.org and NeoOffice
[sitting in the ICE Subversion
repository](http://ice.usq.edu.au/trac/browser/ice/trunk/templates/zotero)
but I can't recommend that you use any of this yet unless you are very
brave and capable of solving your own issues, for one thing you have to
use the bleeding-edge developer version of
[Zotero](http://www.zotero.org/).

There are some serious issues to be resolved before we can call this a
good solution, the main one being the issue of stable IDs for
references. At the moment there's no way to share references and have
multiple people contribute to formatting a document because as in
EndNote the Ids are arbitrary and temporary. We've been discussing
options on the Zotero list but no idea yet how long this will take to
sort out but I am confident that we'll get there in the end.

More minor issues include working out how to add more citation styles to
the plugin and ironing out some the bugs and usability issues.

So thanks to Ian Laurenson (if you need OpenOffice.org customization
done he's your man) and to the Zotero team for letting us play with
their code!

</div>
