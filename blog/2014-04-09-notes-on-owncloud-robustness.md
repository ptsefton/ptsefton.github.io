---
Author: ptsefton
Comments: false
Date: 2014-04-09 22:58:49+00:00
Slug: notes-on-owncloud-robustness
Category: File Data Capture
Title: Notes on ownCloud robustness
Wordpress_id: 1963
---

<article>
I'm on my way to a meeting at Intersect about the next phase of the
[Cr8it data packaging and publishing
project](http://uws.edu.au/eresearch/home/projects/cr8it). Cr8it is an
ownCloud plugin, and ownCloud is widely regarded as THE open source
dropbox-like service, but it is not without its problems.

Dropbox has been a huge hit, a killer app with what I call powers to
"Share, Sync & See". *Syncing* between devices, including mobile (where
it's not really syncing) is what made Dropbox so pervasive, giving us a
distributed file-system with almost frictionless *sharing* via emailed
requests, with easy signup for new users. The *see* part refers to the
fact that you can look at your stuff via the web too. And there is a
growing ecosystem of apps that can use Dropbox as an underlying
distributed filesystem.

[ownCloud](http://owncloud.com) is (amongst other things) an open source
alternative to Dropbox.com's file-sync service. A number of institutions
and service providers in the academic world are now looking at it
because it promises some of the killer-app qualities of dropbox in an
open source form, meaning that, if all goes well it can be used to
manage research data, on local or cloud infrastructure, at scale, with
the ease of use and virality of dropbox. If all goes well.

There are a few reasons dropbox and other commercial services are not
great for a university:

-   We need to be able control where data are stored and have the
    flexibility to bring data close to large facilities. This is why
    CERN have the largest ownCloud test lab in the world, so I've heard.

-   It is important to be able to write applications such as Cr8it
    without being beholden to a company like Dropbox.com, Apple, Google
    or Microsoft who can approve or deny access to their APIs at their
    pleasure, and can change or drop the underlying product. (Google
    seem to pose a particular risk in this department, they play fast
    and loose with products like Google Docs, dumping features when it
    suits them)

But ownCloud has some problems. The ownCloud forum is full of people
saying, "tried this out for my company/workgroup/school. Showed promise
but there's too many bugs. Bye." At UWS eResearch we have been using it
more or less successfully for several months, and have experienced some
fairly major issues to do with case-sensitivty and other
incompatibilities between various file systems on Windows, OS X and
Linux.

From my point of view as an eResearch manager, I'd like to see the
emphasis at ownCloud be on getting the core share-sync-see stuff
working, and then on getting a framework in place to support plugins in
a robust way.

What I don't want to see is more of
[this](http://aditya.bhatts.org/2013/12/16/bringing-opendocument-to-the-web/):

> Last week, the first version of OwnCloud Documents was released as a
> part of OwnCloud 6. This incorporates a subset of editing features
> from the upstream WebODF project that is considered stable and
> well-tested enough for collaborative editing.

We tried this editor at eResearch UWS as a shared scratchpad in a
strategy session and it was a complete disaster, our browsers kept
losing contact with the document, and when we tried to copy-paste the
text to safety it turned out that copying text is not supported. In the
end we had to rescue our content by copying HTML out of the browser and
stripping out the tags.

In my opinion, ownCloud is not going to reach its potential when the
focus remains on getting shiny new stuff out all the time, far from
making ownCloud shine, every broken app like this editor tarnishes its
reputation substantially. By all means release these things for people
to play with but the ownCloud team needs to have a very hard think about
what *they* mean by "stable and well tested".

Along with others I've talked to in eResearch, I'd like to see work at
owncloud.com focus on:

-   Define Sync behaviour in detail, complete with automated tests and
    have a community-wide push to get the ongoing sync problems sorted.
    For example, fix [this
    bug](https://github.com/owncloud/mirall/issues/1439) reported by a
    former member of my team along with several
    [others](https://github.com/owncloud/mirall/issues/1385) to do with
    differences between file systems.

-   Create a standard way to generate and store file derivaties such as
    image thumbnails, or HTML document previews, as well as additional
    file metadata. At the moment plugins are left to their own devices,
    so there is no way for apps to reliably access each others data. I
    have put together a simple Alpha-quality framework for generating
    web-views of things via the file system, [Of the
    Web](https://github.com/uws-eresearch/otw), but I'd really like to
    be able to hook it in to ownCloud properly.

-   Get the search onto a single index rather than the current approach
    of having an index per user, something like Elastic Search, Solr or
    Lucene could easily handle a single metadata-and-text index with
    information about sharing, with changes to files on the server fed
    to the indexer as they happen.

-   [Update 2014-04-11] Get the sync client to handle connecting to
    multiple ownCloud servers, in Academia we will definitely have
    researchers wanting to use more than one service, eg [AARNet's
    Cloudstor+](https://www.aarnet.edu.au/services/netplus/cloudstorplus)
    *and* an institutional ownCloud. (Not to mention proper dropbox
    integration)

[![Creative Commons
License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)\
<span property="dct:title" dct="http://purl.org/dc/terms/">Notes on
ownCloud robustness</span> by <span property="cc:attributionName"
cc="http://creativecommons.org/ns#">Peter Sefton</span> is licensed
under a [Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/)

</article>

