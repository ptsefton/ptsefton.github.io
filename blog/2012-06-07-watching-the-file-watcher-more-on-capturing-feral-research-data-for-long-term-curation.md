---
Author: ptsefton
Comments: true
Date: 2012-06-07 05:40:13+00:00
Slug: watching-the-file-watcher-more-on-capturing-feral-research-data-for-long-term-curation
Category: File Data Capture
Title: 'Watching the file watcher: more on capturing feral research data for long
  term curation'
Wordpress_id: 1073
---

<article>
File wrangling for researchers / Feral-data capture

I wrote recently about a [potential technique to help manage file-based
research
data](http://ptsefton.com/2012/05/09/file-wrangling-for-researchers-feral-data-capture.htm)
so researchers can identify and ‘package’ collections or sets of data
for deposit in a repository. This is an update on that, reporting more
progress on integrating the data capture part of the chain, where a
researcher can identify and package-together a set of data files, and
the catalogue/repository part where librarians are involved in the
process of quality-checking metadata, and publishing a record about the
data, including to Research Data Australia.

My previous post showed screen shots of what the data capture app would
look like. You can now play with[a live demo running on the NeCTAR
cloud](http://115.146.94.153/portal/default/home). If you really want to
play, ask me to share the Dropbox with you so you can add lots of files.
It won’t be there forever and it may break log in with admin/admin and
try making a ‘package’ (let me know if you can figure that out or not).

There is also a copy of the
[ReDBOX](http://www.redboxresearchdata.com.au/) research data
catalogue/repository running on the NecTAR cloud, and it’s watching the
other demo server (answering the question, finally, of who will watch
the file watcher). New packages show up in the OAI-PMH feed there and
get ingested into the ‘investigation’ stage in the repository. Again,
this won’t be there long term but you can [have a
look](http://115.146.94.66/redbox/default/home) (log in as
admin/rbadmin).

[![](/wp-content/uploads/2012/06/image001.png "image001")](/wp-content/uploads/2012/06/image001.png)

Figure 1 Packages created in a file-watching application which have been
automatically fed into the first stage of a ReDBox Research Data
Catalogue workflow

This activity diagram shows the flow of feral files from capture to
catalogue.

[![Description: @startuml title Feral Files Captured and Classified!
Researcher-\>FascinatorFileWatcher: Finds and packages files "Research
Data Catalogue"-\>FascinatorFileWatcher: OAI-PMH Any new records
"Research Data Catalogue"-\>FascinatorFileWatcher: Fetch zipped
collection via web call "Research Data Catalogue"-\>"Research Data
Storage": Store collection Librarian-\>Researcher:More info please
Librarian-\>"Research Data Catalogue":Curate record RDA-\>"Research Data
Catalogue":OAI-PMH New collections @enduml
title=](/wp-content/uploads/2012/06/image003.png)](/wp-content/uploads/2012/06/image003.png)

Figure 2 Activity diagram for the process of getting a collection of
files from a researcher's storage area through to the catalogue and
institutional store, and published to Research Data Australia (RDA)

Copyright Peter Sefton 2012. Licensed under [Creative Commons
Attribution-Share Alike 2.5
Australia](http://ontologize.me/?tl_p=http://creativecommons.org/licence&triplink=http://purl.org/triplink/v/0.1&tl_o=http://creativecommons.org/licenses/by-sa/2.5/au/).
\<http://creativecommons.org/licenses/by-sa/2.5/au/\>

</article>

