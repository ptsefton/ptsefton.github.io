---
Title: "Open Repositories 2016: Demo: A repository before breakfast"
Date: 2016-06-15
Category: Repositories

---

I have just returned from the Open Repositories 2016 conference in
Dublin where I did a demo in the Developer Track, curated by my colleagues Claire Knowles and
Adam Field. The demo went OK, despite being interrupted by a fire
alarm.


Here's my abstract:

> Presented by Peter Sefton, University of Technology, Sydney
> peter.sefton@uts.edu.au
> 
> In this session I'd like to show off the technical side of the [open source] platform, [Ozmeka] (based on [Omeka]) which was presented at OR2015.
> 
> In the demo I will:
> 
> * Spin up a fresh instance of a repository using a [vagrant script] my team prepared earlier.
> 
> * Show how to populate the repository via a CSV file, complete with multiple different item types (people, creative works, that sort of thing) with relations between them.
> 
> * Demonstrate that this is a Linked-data-ish system, with relations between items in the repo, and external authorities and talk about why this is better than using string-based metadata which is still the default in most repository systems.
> 
> * Talk about why it is worth considering Omeka/Ozmeka for
> small-to-medium repository and website development.

To which I added:

> Demo loading the same data into a Fedora 4 repository.

The spreadsheet format I demoed is still a work in progress, which I
will [document on github] project; I
think it shows promise as a way of creating simple websites from data,
including multiple types of object, and nested collections. I took the
[first fleet maps](http://data.gov.au/dataset/3643f4b2-0dd7-4bdc-8548-faf6d5445ae1)
data, munged it a little to create a linked-data set for this demo. As
downloaded, the data is a list of map images. I added a couple of
extra rows:

* Two collections, one for the maps and one for people
* Entries for the people mentioned in the metadata the creators of the
maps

And extra columns for relationships:

* Collection membership via a ```pcdm:Collection``` column.
*   A ```REL:dc:creator``` for the dublin core creator relationship.


![A sample Omeka page](/blog/or2016/chart.png)




## What is this?

I presented a paper last year co-authored with  Sharyn Wise
about an Omeka-based project we did at UTS, building a
[cross-disciplinary research repository], [Dharmae]. This time I just wanted to
do a quick demo for the developer track showing out how easy it is to
get started with a dev version of Omeka, and also show some early work
on an Python API for Fedora 4.


## Audience

This is for developers who can run Python and understand virtual environments. NOTE: These instructions have not
been independently tested; you will probably need to do some problem
solving to get this to run, including, but not limited to running
*both* python 3 and python 2.


## Get the dependencies up and running

1.  Get & run Omeka via this [vagrant script], put together by Thom McIntyre.

   - Get an API Key via  ```http://localhost:8080/admin/users/api-keys/1```

  - Install the item relations plugin (it's there, you just need to
    activate it via the install button) ```http://localhost:8080/admin/plugins```

2.  Get the  One-click-run Fedora Application
from the [Fedora downloads page].

## Import some data into Ozmeka

Assuming Omeka is running, as per the instructions above.

NOTE: This is a Python 2 script.

1. Check out the [Ozmeka Python Utils].

2. Follow the instructions on how to [upload some sample data to Omeka] from a
CSV file.

  Remember your API key, and to install the Item Relations plugin.


## Import the same data into Fedora 4

NOTE: this is a Python 3 Script.

Also, note that Fedora 4 doesn't come with a web interface - you'll
just be putting data into it in a raw form like this:

![Data in Fedora 4](/blog/or2016/fedora.png)


1.  Start Fedora by running the Jar file (try double-clicking it).
2.  Select port 8081
3.  Click Start
4.  Install our [experimental Fedora api client] for Python 3.
4.  Follow the instructions to [import csv data into Fedora].



Thanks to Mike Lynch for the Fedora API code.

[Dharmae]: http://dharmae.research.uts.edu.au/
[experimental Fedora api client]: https://codeine.research.uts.edu.au/eresearch/fcrepo4py
[cross-disciplinary research repository]: http://ptsefton.com/2015/06/11/2111.htm
[import csv data into Fedora]: https://github.com/ptsefton/spreadsheet-to-fedora-commons-4
[upload some sample data to Omeka]: https://github.com/ozmeka/omeka-python-utils/blob/master/csv2omeka.md
[Ozmeka Python Utils]: https://github.com/ozmeka/omeka-python-utils
[open source]: https://github.com/ozmeka
[Ozmeka]: https://eresearch.uts.edu.au/2016/03/01/ozmeka.htm
[vagrant script]: https://github.com/ozmeka/auto-ozmeka
[Omeka]: http://omeka.org
[Fedora downloads page]: https://wiki.duraspace.org/display/FF/Downloads
[PCDM]: https://github.com/duraspace/pcdm/wiki
[document on github]: https://github.com/ptsefton/pcdcmlite/blob/master/README.md
