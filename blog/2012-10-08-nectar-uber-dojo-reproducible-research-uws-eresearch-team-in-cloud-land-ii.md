---
Author: ptsefton
Comments: true
Date: 2012-10-08 05:39:02+00:00
Slug: nectar-uber-dojo-reproducible-research-uws-eresearch-team-in-cloud-land-ii

Title: NeCTAR Über Dojo, Reproducible Research (UWS eResearch team in Cloud Land II)
Wordpress_id: 1521
---

<article itemscope="itemscope" itemtype="http://schema.org/ScholarlyArticle">
<section>
# 

Alf (Andrew) Leahy and I were recently in Melbourne for the [NeCTAR Über
Dojo event](http://melbourne-uberdojo.eventbrite.com/).

> By coming to this two day event you will be able to go back to your
> institution with a signed certificate showing that you've been 'black
> belted' as a Cloud expert, specifically we'll train and qualify you in
> using the following tools and data in the Cloud:
>
> -   How to use image management tools for production level VM
>     management on the Cloud, i.e. Puppet or Chef
>
> -   How to use libraries to access storage data APIs, e.g. SWIFT/S3,
>     NFS, Object Store, etc.
>
> -   We'll also use this event to get you the experts to tell us what
>     new features we need for all these new toys (I mean infrastructure
>     ;-)
>
The climax of this thing was an Iron Chef-style challenge. This is an
initial rough post about our two hour hack (which we cleaned up over a
few more hours post-event). Andrew will write up the event for the UWS
eResearch blog. Thanks to Remko Duursma and Craig Barton for letting use
their code and data for the demo.

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Background: HIE\* researchers use [R](http://www.r-project.org/)

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage002.jpg)

\*Hawkesbury Institute for the Environment

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Meet Remko

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage004.jpg)

<http://www.uws.edu.au/hie/people/researchers/doctor_remko_duursma>

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## And Craig

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage006.jpg)

<http://www.uws.edu.au/hie/people/admin_and_technical_staff/dr_craig_barton>

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## They run R to clean data & model stuff…

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage008.jpg)

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## This R Notebook shows code and output together in HTML

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage010.jpg)

</section>
The night before the challenge I asked Remko and Craig if we could use
some sample data and R code:

> Andrew (Alf) and I are at a workshop in Melbourne - I was wondering if
> I can use this as a demo tomorrow - ie it will appear on screen but
> not be made available over the net. The short notice is because the
> idea has only emerged today.
>
> The thing we'd be demoing would be to \_simulate\_ the following:
>
> -   Data set + scripts like the attached is sitting in a web based
>     repository.
>
> -   Repository offers user the opportunity to download the
>     package OR - Get an interactive R-Studio shell where they can
>     re-run the data
>
>     -   Use clicks a "see with interactive shell" link.
>
>     -   Our server:
>
>         -   Fires up a virtual server in the cloud
>
>         -   Installs the server version of R-Studio
>
>         -   Creates a user account 
>
>         -   Pushes the data package onto the new server
>
>         -   Unpacks the package
>
>         -   Sets up R-studio to run Knitr on the main script to create
>             HTML
>
>         -   sends a link to the R-Studio to the user (maybe by email
>             cos this might take a few minutes)
>
> -   The user can see the plots etc, and will have access to the R
>     environment to tweak things
>
<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Our idea…

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage012.png)

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Remko’s reponse

> That sounds fantastic. Please go ahead! Wait actually those are
> Craig's data :)\*\*
>
> \>\* Get an interactive R-Studio shell where they can re-run the data
>
> YES that is perfect!
>
> greetings
>
> remko
>
\*\*Craig gave us the go-ahead as well

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Initial quick and dirty demo approach

We have written a simple CGI web script in Python which simulates a
repository, with the capacity to orchestrate the below:

-   Create a new NeCTAR machine using Python with the Boto library

-   Connect via SSH and install R-Studio and dependencies, and make a
    user account

    TODO: Use Chef for the initial server build – we learned about Chef
    on Monday but not enough to be able to create a new ‘recipe’ in an
    hour or so.

    TODO: Use a snapshot image so users don’t have to wait ten minutes
    for a machine to start up and install all the prerequisites

-   Copy the sample data set onto the VM

    TODO:  Use the cloud object storage so the data set is near to the
    VM (We know how, just didn’t have time)

    TODO: See if we can get R-Studio to launch with an R Notebook by
    default and log-in automatically

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Why is this cool?

-   **Our researcher-colleagues like the idea**

-   It uses the cloud to solve a set of real problems\*:

    1.  Makes it easy for ‘data shoppers’ to evaluate data sets

    2.  Potentially enables research outputs to be re-run in an exact
        environment for real reproducible workflows (Remko notes that
        you really need the exact R library versions sometimes, this
        could be an option.)

\*Assuming a real implementation

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Screenshot : Script creating a virtual server

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage014.jpg)

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Screenshot: our script Installs R-Studio\*

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage016.jpg)

\*This process is really too slow to do on-demand, we should launch from
a pre-built snapshot. And the automation here is really hacky and crude
– it would be better to do it using something like Chef but that’s not a
one-day project if you have never used it before.

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Result – an RStudio Server…

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage018.jpg)

TODO: Automate the login by passing some kind of token?

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## With a data-set pre-loaded\*

![](/wp-content/uploads/2012/10/wpid-NeCTAR_uber_Dojo.docx.htm_NeCTAR_uber_Dojo.docx_filesimage020.jpg)

\*We have not automated the installation of Knitr – so no R Notebook
yet, but the code is runnable, and will spit out plot-images

</section>

<section itemscope itemtype="http://purl.org/ontology/bibo/Slide">
## Show me the code

The code we produced is demo quality hack-day code. This is not
something you’d use in real life but we’re releasing it on [Google
Code](http://code.google.com/p/uws-eresearch/source/browse/#svn%2Ftrunk%2Fnectar-cloud%2Frstudio)
as an example and so we can remember where to start when we come back to
this and try to do it properly, maybe as part of the data capture
project at the [Hawkesbury Institute for the
Environment](http://eresearch.uws.edu.au/blog/projects/data-capture-for-climate-change-and-energy-research/).

</section>

Copyright<span class="apple-converted-space">  </span>Peter Sefton and
Andrew Leahy, 2012. Licensed under<span
class="apple-converted-space"> </span>Creative Commons Attribution-Share
Alike 2.5<span class="apple-converted-space"> </span>Australia.
\<<http://creativecommons.org/licenses/by-sa/2.5/au/>\>

</section>
</article>

