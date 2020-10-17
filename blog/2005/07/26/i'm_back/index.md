---
Title: "I'm back"
Slug: i'm_back
Date: 2005-07-26

---
I've been away on a [European
Vacation](http://www.imdb.com/title/tt0089670/).

Back now, and about to present a tutorial on Word Processing and XML at
the [Open Publish](http://www.openpublish.com.au/) conference. I'll use
this blog to follow-up questions from the tutorial session and my
presentation in the conference.

This is an interesting time to be talking about word processing and XML,
with the Microsoft Word team blogging as hard as they can about their
new XML formats.

There's a [podcast interview with Brian
Jones](http://blogs.msdn.com/brian_jones/archive/2005/07/25/443044.aspx)
about the new XML format, and [a post by
Brian](http://blogs.msdn.com/brian_jones/archive/2005/07/25/443044.aspx)
about how to use custom schemas with Word.

> When we built the support for customer defined schemas into Word 2003
> there were a couple scenarios we had in mind. The main goal though was
> that we wanted people to take existing Word documents and existing
> Word solutions, and make them more powerful. There has long been
> support for bookmarks, which have some similarities to the XML
> support, but that just wasn't enough. The custom XML support finally
> gave developers the ability to add structure to a Word document and to
> program against it. Did you know that once you add you're XML to a
> Word document, you can capture events when a user moves in or out of
> that element? Did you know that you can use XPath queries to navigate
> the Word document based on your XML, and get a Word range object as a
> result? There is a ton of power here, even if your end goal has
> nothing to do with XML. Of course you can always save out as XML and
> use that data in some other process, but even if you don't care about
> getting XML out, the XML support still makes building solutions
> easier.

I'm not convinced. This looks like high-cost, fragile development to me,
particularly with a new format coming. I think a better alternative is
to use a 'microformat' approach, and embed information in something like
a table, with a known structure, so that it can be found and processed.
I have been doing this for years with educational content, using simple
mechanisms like two-cell tables to mark-up content such as activities or
readings. This is the approach we are taking in
[ICE](http://www.usq.edu.au/dec/staff/ice.htm).
