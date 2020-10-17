---
Title: "Implementing IMS packages"
Slug: implementing_ims_packages
Date: 2005-06-19

---
At work, on the [ICE project](http://www.usq.edu.au/dec/staff/ice.htm)
we are implementing IMS packages so that course content authored using
ICE can be exported to learning management systems. I have previously
[disparaged the package spec](blog/2004/08/06), because it does not
allow for linking between web resources.

This time I want to report a more positive experience (although the
link-free approach taken by the IMS is still anti-web and makes no sense
to me).

We are having a reasonably pleasant experience with the specification
this time, because we built the product around it, rather than designing
the product first then trying to force the export to fit. So this time
ICE has classes in the Python code that implement the IMS organization
as an editable table of contents (TOC).

An author can create a number of documents and use the ICE application
to build an editable TOC for them. Just one TOC is allowed at this
stage, but we will add more if and when the users ask. Behind the
scenes, the export process is a simple serialization, turning the
program's internal TOC structure into a valid IMS organization expressed
in XML.

This has been a painless bit of development because we used the standard
we were supporting to guide design.

USQ staff can see the ICE project, code, roadmap, wiki and job-tickets
[here](http://sdt.dec.usq.edu.au/projects/sdt). Outsiders will have to
wait a few more weeks for a peek at it.
