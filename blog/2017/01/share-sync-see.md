---
title: Share, Sync and See, or "look ma no UI": My favourite software deployment patterns for file managent and publishing

---


Over the last decade and a half I've been involved in quite a few web publishing and data management projects for a variety of scenarios in the academy. In this post I will look at some of the patterns for software deployment. The magic here words are: *Share*, *Sync* and *See*, like what Dropbox does. It gives you frictionless *sharing* of files, *synch*ronises them between devices and lets you *see* them on your computer, the web or on mobile devices. Apart from the simple benefits of all these S words, it is possible to create software workflows that almost have no User Interface (UI).


This reflection is prompted by my recent experiences [formatting songs automagically], where I implemented some command line software, with a lovely array of command line options in it. As far as I know, I'm still the only user of this thing,  and most of my music friends are not going to download and run a python script with these obscure flags. But they *might* share  a dropbox with me and edit text files in chordpro format. I set things up so that a diligent robot, running on an Amazon cloud computer watches a dropbox, and makes freshly formatted [PDF](https://github.com/ptsefton/chordprobook/blob/master/example_output/uni-verse.cho_key_C_uke.pdf) song sheets every time someone adds or changes a file^[Works well for me, but so far not a whole lot of uptake from my buddies, who prefer to get me to do it, or   but I live in hope.

To me this is almost a UI-less software deployment. All I do is the creative/editorial part and the formatting automagically happens. This is a super-refined version of share-sync-see based software. For example, building a new song book can be pretty much achieved by typing out a setlist, which is something you're going to do anyway for a performance, I have organised my dropbox-based no-UI service so with very minimal extra effort the act of saving a setlist causes a PDF book with song-sheets for use in practice or performance to come into existence.

Back in the early 2000's I lead the development of a course publishing system for the University of Southern Queensland (USQ), called the Integrated Content Environment (ICE). This was used (maybe still is?) at USQ for lecturers to create book-length distance-ed materials for delivery via standardised course packages (IMS), straight web sites, printable PDF, and EPUB ebooks. There were a few things ICE did that I think were ahead of their time:

* **Syncing**: ICE implemented a kind of Dropbox-style syncing, albeit in a clumsy way, via the use of Subversion, a version control system. Course materials were replicated between users' desktops and a central server.

* **Sharing**: This meant that multiple authors could collaborate on the same content, and there was always a server-side copy of everything, and because we built it on Subversion we had a way to manage permissions using the standard Subversion approach. (By the way, having Subversion deeply integrated into the application turned out to be a spectacularly bad idea, it meant we had to constantly update the software with new versions of the subversion library, which didn't always work. Waaaay more trouble than it was worth.)

* **Seeing**: In ICE you would change a file, refresh your browser, **see** your content, via some back-end conversion software. This part was the most innovative at the time. Initially ICE ran as a cross-platform localhost web application. This meant you had a little web server running on your Windows, Mac or Linux computer, and you could see a web (and PDF) view of your Microsoft Word content generated as you went.

Some parts of ICE were almost UI free - the bit where all you had to do was author a course document in a word processor and it would automatically turn into an HTML page. But there were still some parts that had an interface such as compiling documents into an ordered course book/site, and publishing the result.

Looking around now, I see these functions/usage patterns we built into ICE are now mainstream. 

*  Most obviously, Dropbox.com does syncing and sharing, but has also steadily evolved to offer **seeing** content as well. It offers a web-view of whatever you have in your Dropbox folder, including online previews of PDF, Word docs, HTML and so on, and now offers commenting, but the previews are only what the Dropbox people provide, without writing an app, and applying for API keys etc there's no standard way to plugin a conversion service like mine.

* Github, in addition to being built on git which is *the* way to *share* & *sync* for the cool kids on the internets, offers *seeing* of files, including markdown, but also [PDF]. 

*  The recent crop of static website generators offer a very similar experience to ICE - you edit a set of local files in markdown or the like, some local daemon running on your computer converts them to HTML so you can *see* them, then you use the git version control system, successor to Subversion, to *sync* and *share* with collaborators or, if you're not that hard-core, Dropbox. Viewing the site is easy, you just run a little webserver locally or look at them over the web.

For publishing/authoring application where you're working with source files that need to be converted into some other format, such as ICE's word processing documents that were turned into HTML and PDF courseware, with multiple course module documents, or markdown documents making up a website, *share-sync-see* is a winner, it's nice to have local access to files to edit them using desktop tools such as word processors.

# Challenges with share-sync-see applications

One big challenge in designing your own *share-sync-see*  apps is getting the right blend of local and server-side processing, and a permissions scheme that works for your cohort of users. It's easy enough to write an application that runs locally, minus the share and sync bits. Run the application under an user's account and it can automatically access a certain set of files and file-shares, but if you also want to provide a central web-only view then there's a problem - you need an authentication scheme that works globally, and integrates the *see* part of the service with the *share* part. Github and dropbox have this solved, because they are share/sync services they control the files completely, but for an independent developer it's harder; I can't just throw up a web server to show my whole dropbox and have it know who is allowed to see which parts based on who I have shared (yes there's an API and no, as far as I know they don't usually let you write apps that access all of a user's files).

I solved this access-control problem for my music-file conversion use case by signing up for a Dropbox account and running the dropbox sync client on a server - to use the system you can share a folder with that account, and then it will start seeing your files. 

Another big challenge is that there is no standard way to represent a preview, thumbnail, or rendition in a file system.  Imagine if, instead of having to wait for Dropbox to implement a preview for a given file format, there was a *standard* for previews, that could be stored alongside the original file - previews might be in HTML format, for example, or be images, that way you could run a service which would populate the previews and other people could see them on Dropbox, or github or wherever. Alas. there are no widely use conventions for this. Microsoft office has a way of storing image assets alongside HTML documents while in ICE we had a .ice folder for derived files, but there's nothing standard.



[song]: https://github.com/ptsefton/chordprobook/blob/master/samples/i_called_your_name.cho
[examples files]: https://github.com/ptsefton/chordprobook/tree/master/example_output
[formatting songs automagically]: http://ptsefton.com/2015/11/10/scratching-an-itch-my-software-for-formating-song-sheets-into-gasp-pdf.htm
