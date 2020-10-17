---
Title: "Why keep that $25 Linux machine?"
Slug: why_budget_linux
Date: 2005-03-07

---
I think I mentioned my $25 computer that I bought from my previous
employer's going out of (this particular) business sale. It's a Compaq
Presario 2294, few hundred meg processor, runs Ubuntu Linux and is about
six years old I think. I have been keeping it to do Subversion hosting
for my personal projects, but I have now signed up for SVN and Trac
hosting at my ISP. So why keep it sitting there at home, burning coal?

Well, today at work we discovered that we were unable to check out
[Trac](http://www.edgewall.com) from Subversion (and we wanted to do
that because we have been lightly hacking it) and I thought it was
probably firewalls or proxies and offered to try at home. Then I
remembered the ISP - logged onto ptsefton.com and tried. Same issue.
Offered to do it when I got home. Then I remembered the ex-NextEd
machine.

It was called Spike at NextEd, so I renamed it Spite, out of, you know,
respect. I'm no network adminstrator so there's some mucking around to
manually route packets for port 22 from the ADSL router here to that
machine, depending on what address it got assigned and then setting up
'spite' in the hosts file on my work laptop depending on what address the
router got. (There is a better way, right?)

Anyway, I was able to connect to the machine at home from work, grab
Trac, pack it up, copy it back to the Mac at work, then up to a server.
Not quite \$25 worth, but I reckon that alone was worth \$1.75.

The error in question is this. You ask for a subversion checkout via
http.

    $ svn co http://svn.edgewall.com/repos/trac/

And get this:

    svn: PROPFIND request failed on '/repos/trac'
    svn: PROPFIND of '/repos/trac': could not connect to server (http://svn.edgewall.com)

I had the same problem just yesterday trying to get
[Leonardo](http://www.jtauber.com/leonardo) (the software that powers
this site).
