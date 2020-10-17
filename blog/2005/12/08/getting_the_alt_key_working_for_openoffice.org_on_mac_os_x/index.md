---
Title: "Getting the Alt key working for OpenOffice.org on Mac OS X"
Slug: getting_the_alt_key_working_for_openoffice.org_on_mac_os_x
Date: 2005-12-08

---
<div>

The OpenOffice.org version 2.0 I have for the Mac does not reliably work
with the Alt key. It gives you menu access from the keyboard. Using the
[ICE](http://ice.usq.edu.au/) template, I type `ALT-S `to access the
styles menu, and life is miserable without it. Miserable also is life
with Microsoft Word for the Mac. No Alt key there either even though the
shortcuts are there for Windows users.

So a couple of weeks ago I got around to googling for a fix, and came up
with [this page
on](http://www.macosxhints.com/article.php?story=20030704084450466)
macosxhints. I tried some of the stuff suggested there and got it
working for OpenOffice.org. Or so I thought.

But do you know what? When I started writing this post, and re-testing
to make sure I had everything right I had to shut down X windows and
restart it completely a few times, and the Alt key began to work only
sometimes.

Turns out that I thought I had made changes to my config that made the
Alt key work, but now I don't think they really did anything. Alt works
for me if start X first, then click the OpenOffice.org icon to start the
.app. if you let the OpenOffice.org application start X for you then Alt
ends up not working.

It took ages for me to figure this out because I reboot this Mac very
infrequently, like at intervals of a few weeks.

I do have a nice .Xdefaults file in my home directory that adds a scroll
bar to the Xterm application, and allows you to make text bigger and
smaller with `Cmd –` and `Cmd +`. That bit comes from [another
post](http://forums.macosxhints.com/showthread.php?t=8451&page=2) on the
same site. Make sure you read the **whole thread** if you want to try
it.

****

</div>
