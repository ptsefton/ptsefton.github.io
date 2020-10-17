---
Title: "New computer"
Slug: new_computer
Date: 2004-10-10

---
Along with most of the rest of NextEd's Toowoomba staff, I am changing
jobs(aka *redundant*); off to work for ["The University of Southern
Queensland" USQ](http://www.usq.edu.au) for at least a little while.
This means giving up my work computer, but at the staff auction on
Friday I scored an IBM T20 notebook for practically nothing. It's now
running Linux, happily connected to the ADSL connection at home, as is
the old Compaq desktop I got for \$25.

I was seriously considering forking out about \$2000 (Aussie) for a new
IBook to try OS X like all the proper geeks but at \$150 so far this one
seems pretty good value.

A few notes about the experience so far follow.

The only problem with my new computer is that the removable DVD drive
only works "about once in twenty times" as the previous user put it. My
colleague Ron Ward peered into the connector and said "spray some WD40
on it", which I would do, if I could find it (won't be able to find it
until I finish reading [Getting Things
Done](http://merlin.blogs.com/43folders/2004/09/getting_started.html)
and Implement a System, and buy a label maker, and so on). What works,
though, is licking it. Well not so much licking it as blowing in it with
nice slobbery moist breath. That makes enough contact to run the thing
for a few hours.

First up I booted from a Knoppix CD, which is a way of running Linux
without spoiling your computer, and managed to get in a spot of web
surfing. Emboldened I tried to get Knoppix to copy itself to the hard
disk by running the |knoppix-install| command, using [instructions I
found](http://doc.vic.computerbank.org.au/authorsplaypen/playpen/knoppix_install_draft/).
Two problems there:

-   The partioning process seems to go alright but the installer can't
    recognize the partitions. Eventually I tried |ignore\_check=1 sudo
    knoppix installer| and got through to the next part, whereupon,

<!-- -->

-   the system starts installing itself and then starts reporting
    screenfulls of disk-related errors, maybe to do with the slobber on
    my DVD drive drying up, or maybe not.

So, to plan B.

Plan B was to download [Ubuntu Linux](http://www.ubuntulinux.org/), make
a CD and try that. The process took a whole evening, mostly because the
installer can get the latest packages from the net, and that took a few
hours for each computer, over the 256Kb/s ADSL. Luckily we were watching
[Hidalgo](http://www.imdb.com/title/tt0317648/) on DVD, and I had plenty
of time to wander out and check on the installs without feeling like I
was missing out on anything, not to mention catching up on an hour or so
of sleep.

Why Ubuntu? Well, it was [on Slashdot last
week](http://linux.slashdot.org/article.pl?sid=04/10/03/1233220&tid=106).
Sounded alright to me.

So I now have two Linux computers, both of which can connect to the Net
with no problem; and for a Linux newbie, with some Unix experience a
long time ago, it's all pretty friendly. I even got Flash working with
the (supplied, yay) Firefox web browser so the kids could play games,
but some didn't work, I guess because they use Shockwave, for which
there is apparently no plugin.

The next steps are to:

-   Get connected to the Windows shares that hold all our data here. Not
    working yet.

<!-- -->

-   Get subversion running on the Linux desktop/server to keep track off
    all our documents.

<!-- -->

-   Get the power management to stop lying to me; it claims the battery
    is 0% charged and that it is running from the battery, even when
    plugged in.

<!-- -->

-   Move my Python experiments and the start of the [Word Processing
    Interoperability project](blog/2004/08/16/wordprocessorinterop) to
    the Linux machines.

<!-- -->

-   Figure out how to organize myself on Linux without making a big mess
    of it. This is urgent, because the mess has started as I experiment
    with bits and pieces. Already there are half-ripped CDs and empty
    files created with Emacs in strange (to me) places.

<!-- -->

-   Get a wireless card working. We have a laptop here with a Belkin
    card; no luck with that so far.

<!-- -->

-   [Learn Emacs](http://www.chris.spear.net/emacs/default.htm). Emacs
    is a, a everything that I have been meaning to get to grips with for
    many years. I will set aside an afternoon for that.

It is possible I will update this, or post further on how to switch from
Windows to Linux.
