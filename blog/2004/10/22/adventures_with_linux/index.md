---
Title: "Adventures with Linux"
Slug: adventures_with_linux
Date: 2004-10-22

---
It's not like I have been doing nothing, it's just that settling into a
new job and replacing the computer I use at home, which belonged to
someone else and ran Windows XP with one that belongs to me and runs
Linux, and going out three times in one week, and being taken to school
as a show and tell, like a live rat, and all that, it's just that that
has slowed me down a bit on the all important blogging. Actually,
apparently the kids liked the rat better than me singing *The Coat of
Many Colors* with my twelve-string.

However, we now have it all under control. I have made some good
progress on the Word processor interoperability project. I now have a
usable OpenOffice template which I will post here soon. A paper I wrote
with my mate Cameron Loudon, all about Learning Management Systems is
also forthcoming. Also, I think I've found a good place to publish some
stuff about turning MS Word documents into XML. Oh, and barring
lightning strikes (which are pretty common up here on the Darling Downs
this time of year) the courseware aware web publishing system I worked
on for the last four years at NextEd is about to go open source.

But this time, a few comments on the switch to Linux. This may be of
interest if (a) you already know about this stuff and you want to
reassure yourself that I am what my four year old calls an "it wit" or
(b) you want to know about how one goes switching from Windows to Linux
without pausing to [RTFM](http://catb.org/~esr/jargon/html/R/RTFM.html).

(Executive summary: RTFM)

Last time I reported that I had put Ubuntu Linux on my computer for
fairly frivolous reasons. But the battery meter didn't work, and it
would not suspend and resume — actually maybe it would resume but how
would I know when it wouldn't suspend?

So, given that they use this thing called "Red Hat" at work I borrowed
the disks that came with TFM they bought and installed a thing called
"Fedora Core 2". Now I have a battery meter. Yay! And I can suspend the
laptop so the little light in the shape of a croissant comes on.

One day I hope to be able to *resume* the laptop as well, without having
to dip it in a bucket of water until all the lights go out, then put in
the dryer until they come back on.

And, while Ubuntu Linux looked great, the fonts now look really crappy
and I have somehow configured it to use some weird keyboard setup that
gives me accents all over things when I try to type of good old English
quotes, and sometimes the network just Will Not Work. I have to reboot
it, which is a skill I learned from running Windows all those years.

And buying a wifi card for it? Ha! I have asked a few retailers, and
searched for a few others, and looked at lists I found, and I still
can't find a straight answer about a card I can buy that has a better
than maybe chance of working.

Not to mention the Palm, that tiny little computer that is supposed to
talk to the laptop.

But the most annoying part is this. Every time I get a fresh install of
Windows I curse the way it comes configured to hide file extensions, and
system files and so on. And guess what? This week I have been playing
with OpenOffice, and configuring its menus, which are in XML, which is
cool. I learned to hack the 'writermenubar.xml' file that lives
somewhere in there. But while I could get it to work at work on Windows,
to give me a usable way of styling my work, I could not find the same
file at home, not by prodding or poking or using the Search For Files...
thing they give you. Until I worked out something I knew very well
twenty years ago...

There are these directories (folders) and files that you can't see that
have names that start with '.'. And the file search does not go there by
default which given the slightly obscure interface is *worse* than
Windows. In Windows you *know* it's trying to trick you, and I trusted
this Fedora. It wit. I have hereunto considered hats to be benign.

Anyway, you can see the files if you know this; you type |ls -a| or tell
Search for Files to |Show hidden and backup files...|.

Other parts of this Linux this are pretty cool - I am loving the little
terminal thing with the tabs where I type stuff like |zip -r
testdoc.sxw \*| to package up some stuff and then |oowrite testdoc.sxw|
to open it in OpenOffice.org. Better than all that clickety clickety
Windows stuff.

The bottom line is, of course, that if you want to run Linux you should
RTFM. Really.
