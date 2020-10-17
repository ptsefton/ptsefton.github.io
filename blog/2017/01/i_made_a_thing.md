---
title: Announcing my engagement (how to track who you're talking to)
author: ptsefton
date: 2017-01-19
comments: true
category: Repositories
slug: Tools
---

In this post I introduce a little command line Python script designed
to report on who you (and your team) have been interacting with via
email. Given access to an IMAP email server (including Office 365),
and an LDAP server with some divisional or organisational grouping
info it will draw bar-charts to show which divisions you've been
talking to, including being able to aggregate information. It will
almost certainly need some adapting to work outside of UTS but if
anyone's up for that then maybe we can turn it into a more
general-purpose tool.


At work, we have a monthly reporting cycle which we're constantly
trying to optimise. One of the problem areas has been how to efficiently  track and
demonstrate how we're engaging with our internal stakeholders and
clients. A lot of interaction is captured in the help desk system, but
not all. We've tossed around various ideas for capturing interactions,
including local CRM (bad idea), spreadsheets or time-logging systems
(yuck), recording everything in a wiki or project system (we do, but adding enough
metdata to generate reports would basically mean inventing a CRM
(*really* bad idea).

Then Matt from our team had an idea: why not mine our email? We tossed
around a few ways to do this, involving special mailboxes, and
forwarding important interactions, and I had a play with the idea on
one of my long train commutes. Eventually I settled on a slightly
different approach, investing about a day's work time in a script:

- Connects to an IMAP server using the email address you give it. We
   use Microsoft's office365.com - works a treat!

- You tell it which mail folder to look in - ```Sent Items``` is the most
  useful for our purposes  (some people might find their sent stuff is in plain-old
  ```Sent``` or somewhere else if they've been using non-mainstream
  clients).

- You give it the address of your LDAP server and a parameter for
  which LDAP property to look in for group info. Ours is
  "utsUnitLevel1", I'll bet my left liver yours is different -
  unless you're from UTS. I need all my livers.

- You give it a JSON file mapping the group names returned by LDAP to
  something shorter (for the chart), and tell it to ignore some
  groups, like your own division if you like (we do, 'cos all the
  internal chatter otherwise drowns out the interactions we want to
  report on, which are those with the customers).

- There's some experimental code in there to build a network graph,
  might come in handy some day.

Once you have had your team all run the script to generate a summary
report each, you can aggregate the results. Here's an anonymised
result showing five of the eResearch team's interactions with eight
faculties and institutes. Oh, did I mention there are flags to anonymise group and
individual's names?

![Stacked bar chart showing how many emails various people have sent to groups you can about](/blog/2017/01/figure_2.png)

