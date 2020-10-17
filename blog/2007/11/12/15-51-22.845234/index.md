---
Title: "Crossing curation mountain"
Slug: 15-51-22.845234
Date: 2007-11-12

---
<div>

[View this page as PDF](/blog/2007/11/12/15-51-22.845234/100.pdf)

<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">I'm looking forward to seeing Peter Murray Rust
</span></span>[<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">eat my dog
food</span></span>](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=806)<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">. He's lucky cos at our place the hounds eat relatively
benign dry food. Oh, and raw chicken wings and mouldy bread and diverse
leftovers deemed to foul for </span></span>[<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">the
fowl</span></span>](http://ptsefton.com/blog/2007/02/08/chooks)<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">. Not to mention compost, fertilizer of all kinds of origin,
grass and lizards and parrots when they can get them. Maybe not so
lucky, but I'll buy him a beer to wash it down.</span></span>

I'm going to follow up on using ICE for blogging to WordPress soon which
is what that dog food stuff is about, but Peter has just pointed out
some issues with getting papers into institutional repositories and I
wanted to discuss some of his points here.

<span
style="background-color:transparent; country:US; language:en; "><span
class="T2">In summary I think that his message is that the
</span></span>[**<span>curation
boundary</span>**](http://ptsefton.com/blog/2007/02/07/curation-boundary)**<span>
is too high</span>**<span
style="background-color:transparent; country:US; language:en; "><span
class="T2"> to cross for authoring teams. Or is it that it is
</span></span>**<span>too far away</span>**<span
style="background-color:transparent; country:US; language:en; "><span
class="T2"> from the authoring process?</span></span>

Here's his summary:

> [<span
> style="background-color:transparent; country:US; language:en; "><span
> class="T2">Using our own
> repository</span></span>](http://wwmm.ch.cam.ac.uk/blogs/murrayrust/?p=811)
>
> ...
>
> Here are some basic problems about reposting:
>
> -   the process from starting a manuscript to final publication can
>     take months or years
>
> -   there are likely to be multiple authors
>
> -   authors will appear and disappear during the process
>
> -   manuscripts may fission or fuse.
>
> -   authors may come from different institutions
>
PMR then goes on to talk about the solution they're trying. They have
set up an authoring repository when collaborators use Subversion (SVN):

> Well, we are starting to write our papers using our own repository.
> Not an IR, but an SVN repository. So Nick, Joe and I will share
> versions of our manuscripts in the WWMM SVN repository. Joe wrote his
> thesis with SVN/TeX and I think Nick<span
> class="spCh spChx2019">’</span>s doing the same. Joe thought it was a
> great way to do things.

([ICE](http://ice.usq.edu.au/) uses Subversion too and it works well for
us, but we have had to put quite a complex layer in front of it so
ordinary non-technical people can deal with it. We have been asked to
support LaTeX; I'll let you all know if that comes off.)

> The advantage of SVN is that you have a complete version history. The
> disadvantage is only that it<span class="spCh spChx2019">’</span>s not
> easy to run between institutions. I am not a supporter of
> certificates. And remember that not all our authors are part of the
> higher education system. In fact Google documents starts to look
> attractive (though the versioning is not as nice as SVN.)
>
> Will it work? I don<span class="spCh spChx2019">’</span>t know.
> Probably not 100% - we often get bitten by access permissions,
> forgetting where things are, etc. But it<span
> class="spCh spChx2019">’</span>s worth a try.

Two things here:

1.  <span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">Working between institutions is definitely a problem,
    particularly when not everyone is in higher-ed. I'm not sure what
    kind of certificates PMR's talking about but I will say this:
    </span></span>[<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">Shibboleth</span></span>](http://shibboleth.internet2.edu/)<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2"> isn't going to solve the problem when there are groups
    coming from all over the place any time soon, but
    </span></span>[<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">OpenID</span></span>](http://openid.net/)<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2"> might help. Using OpenID the owner of a working
    repository should be able to tell SVN who to trust, using their
    OpenID <span class="spCh spChx2013">–</span> and if you come from an
    institution that doesn't use it then you can always get one from
    elsewhere.</span></span>

    <span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">Should work for web application, but it could be a
    challenge to get the commandline version of SVN working with OpenID
    because some OpenID providers might require you to use a web-GUI to
    authenticate, but </span></span>[<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">people</span></span>](http://bloritsch.d-haven.net/articles/2007/07/27/openid-as-authentication-wrapper)
    have [<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">thought about
    it</span></span>](http://brad.livejournal.com/2206769.html)<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">.</span></span>

2.  <span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">Google docs? Well as discussed here before Stijn Dekeyser
    and Richard Watson of USQ found that</span></span>[<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2"> it makes a good online text editor with supernatural
    collaborative
    powers</span></span>](http://ptsefton.com/blog/2006/12/06/goog_docs)<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">. If you want to edit in raw LaTeX that is. They made a
    demo system that lets you render Google docs, even. But as a word
    processor? </span></span>[<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">No</span></span>](http://ptsefton.com/blog/2007/07/05/the_web_with_google_docs)<span
    style="background-color:transparent; country:US; language:en; "><span
    class="T2">. You'd be stopped by the lack of support for stuff like
    bibliographies and Maths before you got too far and don't get me
    restarted on the HTML it makes.</span></span>

I liked the last bit, so I added some emphasis:

> And **if I were funding repositories I would certainly put resource
> into communal authoring environments**. If you do that, then it really
> is a one-click reposition instead of the half-day mess of trying to
> find the lost documents.

I'll be sure to mention this to our friends at DEST.

</div>
