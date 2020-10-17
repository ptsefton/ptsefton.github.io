---
Title: "Installing OpenOffice v2 (beta) for Mac OS X"
Slug: installing_openoffice_v2_(beta)_for_mac_os_x
Date: 2005-06-24

---
I wrote
[before](blog/2005/04/26/openoffice.org_version_2_beta_for_mac_os_x)
about how to find builds of the beta version 2 of OpenOffice.org for Mac
OS X.

Not all the beta builds have had OS X versions, and some have had only
Czech language support, but build 1.9.109 has lots of languages. I got
an English version and it works beautifully - the fonts look nice, it's
dramatically faster than previous versions and it has not crashed at all
in a couple of days of use, even with the [ICE
application](http://www.usq.edu.au/dec/staff/ice.htm) using the same
copy of OpenOffice as me to do document conversions while I am typing in
it. I'm using Tiger (OS X 10.4), but this should work for earlier
versions of OS X, as far as I know.

This is the X11 version which requires Apple's X11 window manager (you
can install it from your original CDs if needed). It is not the same as
the more Mac-like [NeoOffice](http://www.neooffice.org/) which is based
on version 1 of OpenOffice org. Get that one if you want a reliable
tool, rather than beta software.

You can get the beta from
[here](ftp://ftp.linux.cz/pub/localization/OpenOffice.org/devel/680/SRC680_m109/Build-1/).
Download, unpack and click your way through all the installers. You can
select them all and double-click to get started.

One thing I forgot to mention last time is how you run it. Once
everything is installed, start a terminal in X11 and run:

    /Applications/openoffice.org1.9.109/program/soffice

But there is also another way. To make a simple application that you can
double-click to open, or put in the Dock, use the AppleScript editor to
create a little program like this and save it as an application. It's a
bit rough, wants you to click a button before it will start.

     tell application "X11"
     activate
     end tell


     do shell script "export DISPLAY=:0 && /Applications/openoffice.org1.9.109/program/soffice"

(Based on a tip in the [macosxhints
forums](http://forums.macosxhints.com/printthread.php?t=8704&page=4&pp=20))
