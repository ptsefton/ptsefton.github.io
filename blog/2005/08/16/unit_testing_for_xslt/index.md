---
Title: "Unit Testing for XSLT"
Slug: unit_testing_for_xslt
Date: 2005-08-16

---
Unit testing is a Good Thing. An Essential Thing, even, for people who
write computer programs. The idea is that you make sure that each little
bit of the program is tested automatically to ensure that it does its
job, and you keep running the tests as you add to the program. Helps
catch the bugs that you create when changes have side effects on other
parts of the program and makes it very easy to make major changes to a
program. Other kinds of testing like getting users to use it to do stuff
with it and simulating users doing stuff are still required.

A long time ago, I [wrote about unit testing for
XSLT](blog/2004/05/17/xslt_unit_testing) as practiced Jacek Radajewski -
back then he worked for USQ and I didn't. Now I do and he doesn't.

Anyway the system Jacek and the team at USQ developed has been released.
If you do XSLT, and you can run Java (which means pretty much everyone
if they persevere) then you should look at Jacek's UTF-X project.

There's a [UTF-X page here](http://utf-x.dev.java.net/) (I think he
wants java.net to be the home eventually):

There's a bit more to see on
[Sourceforge](http://utf-x.sourceforge.net/).

We use UTF-X to test all the XSLT code written for the [ICE
project](http://www.usq.edu.au/dec/staff/ice.htm) we're working on at
USQ. If you're doing XSLT you care about and you don't have some kind of
unit test framework then you should use it too. If you use some other
framework would you mind telling me what it is?

(Updated - I forgot to mention that UTF-X was a team effort)
