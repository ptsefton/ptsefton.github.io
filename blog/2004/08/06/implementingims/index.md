---
Title: "Links considered too difficult for online education software"
Slug: implementingims
Date: 2004-08-06

---
At work I have been implementing the IMS content packaging
specification, mainly so we can feed content from our publishing system
to our new Distributed Learning System, but here again we are [running
into the 'anti web'](localhost:8000/blog/2004/05/11/caddie). Basically
the IMS package lets you put all your stuff (in this case HTML pages and
images, MP3s and so on) in a directory structure, add a manifest file to
say what's there and zip it all up. The most important bit of the
manifest is the organizations section, which lets you provide multiple
tables-of-contents or other navigation for the materials. There is also
a place to put metadata, if you are optimistic enough to think it might
be useful later, and boring but necessary lists of files.

But how to deal with links? The [IMS Content
Packaging](http://www.imsglobal.org/content/packaging/index.cfm)
specification does not seem to mention links between content items at
all. Maybe I missed something. I can't comment on what commercial or
technical pressures caused this, but the situation is, um, sub-optimal.

Googling got me this [useful (PDF) resource on the basics of content
packaging](http://www.cetis.ac.uk/lib/media/CPbrief.pdf). Here's a calm
and reasonable explanation for why you can't have links.

> To make an IMS Package that is truly reusable, however, you need to be
> careful about how you author the content within it, as it may be used
> in a different context.
>
> For example, if your resources contain hyperlinks to other resources
> it makes it more difficult to separate the resources and reuse them in
> another way. Instead, you can use the Organizations section of the IMS
> Package to provide a navigation structure for the user without the
> need for hyperlinks in the resources themselves. The CETIS Educational
> Content Special Interest Group has support materials available to help
> you with writing reusable content (see People, Products and Services).

Without the need for hyperlinks? Oh dear. And what about plain old
linguistic references — you know, talking about something covered
earlier in the course. Do I need to get rid of that too?

One of the things our clients like about our system is that we allow
them to link between resources explicitly, inline, where they want a
link. We also add navigation to every page to supplement the
typically-basic LMS navigation.

This is the web, you know.
