---
Title: "The Affiliation Issue in Institutional Repository software"
Slug: the_affiliation_issue_in_institutional_repository_software
Date: 2006-06-06

---
<div>

My favourite issue in the work we're doing with institutional
repositories is what I call the Affiliation Issue. It's all about how
you record authors and their institutional affiliation in your
repository. In the Australian context there are two very good reasons to
do this:

1.  **For reporting** to the Australian Department of Education, Science
    and Training and Training, know to its friends as
    [DEST](http://dest.gov.au/), institutions need to keep track of
    research output.

2.  For their own purposes institutions often also want to know not just
    the total number of publications, but **which departments are
    publishing**.

Sounds simple, but there are lots of issues. Affiliation can change over
time. Departments change their names or merge and as with any metadata
consistency is important. Am I the same Peter Sefton who also calls
himself Petie Sefton, whose honours thesis is cited in [this
paper](http://portal.acm.org/citation.cfm?id=972659&dl=GUIDE&coll=GUIDE).

(Answer: yes. Google Scholar seems to be able to work out that Peter
Sefton and Petie Sefton are synonyms. Cuts my vanity searching time in
half. But I'm not the only Peter Sefton mentioned.).

I'll talk about the four repository software packages with which I have
some experience through the RUBRIC project. They are:

1.  [ePrints](http://www.eprints.org/software/) (not part of RUBRIC but
    used by USQ)

2.  [Fez](http://sourceforge.net/projects/fez/)

3.  [DSpace](http://www.dspace.org/)

4.  [VTLS Vital](http://www.vtls.com/Products/vital.shtml)

But first, a few words on identity management.

# <span id="id801514"></span>Identity management

Broadly speaking, there are two approaches to identify management in
repository software. Either it's managed or it aint.

That is, in some systems there is a table of Authors, and the metadata
for a record contains a key that points to that table. So instead of
putting my name in the author field I pick it off a list and the system
stores the fact that author 8342947 (that's my student number from the
University of Sydney) wrote this item.

Other systems just store a name, as a string.

Author identities managed:
:   ePrints and Fez both do it this way. Fez has a lot of functionality
    in this area for describing the structure of your organization.

Not managed: 
:   DSpace and VTLS Vital / VALET.

I think that managed identities need to be used with caution.
Affiliations change, even potentially over short timeframes so someone
might be publishing from two departments and departments can change
their names, split and merge.

# <span id="id801492"></span>Affiliation

So the repository solutions we're looking at divide neatly into ID
Managed and ID Not Managed, but it gets better. They also divide equally
on the issue of whether affiliation can be stored with the author's name
as a bundle or not.

Some repository software, like DSpace uses flat metadata consisting of
name value pairs. So you can say:

<div class="Table49" align="left">

Name

Value

Name

Peter Sefton

Affiliation

Rubric Project, USQ

</div>

Which is OK until we get to two authors. Now which affiliation belongs
with which person? There are no guarantees that the order of the
metadata will stay the same as it goes in and out of repositories.

<div class="Table50" align="left">

Name

Value

Author Name

Peter Sefton

Author Affiliation

Rubric Project, USQ

Author Name

Catherine Sefton

Author Affiliation

Department of Presents, Summer Hill University

</div>

There are a number of ugly hacks one might use to record author
affiliation in systems that use flat metadata:

1.  Make a field with author and affiliation concatenated. Yuck.
    Violates several basic principles of computer science, the names of
    which I have forgotten. Error prone.

2.  Create another data stream that **does** do nested metadata and then
    change the repository to be aware of it. This is a possible DSpace
    solution, but would take some work.

3.  Add special fields like author1, affiation1, author2, affiliation2.
    Workable, but really, really ugly.

Some solutions do allow nested metadata so if I were to write a paper
with my little sister the repository could keep track of our affiliation
like so:

<div class="Table51" align="left">

Name

Value

Author

+--------------------------------------+--------------------------------------+
| Name                                 | Peter Sefton                         |
+--------------------------------------+--------------------------------------+
| Affiliation                          | Rubric Project, University of        |
|                                      | Southern Queensland                  |
+--------------------------------------+--------------------------------------+

Author

+--------------------------------------+--------------------------------------+
| Name                                 | Catherine Sefton                     |
+--------------------------------------+--------------------------------------+
| Affiliation                          | Department of Presents, Summer Hill  |
|                                      | University                           |
+--------------------------------------+--------------------------------------+

</div>

That's nested metadata. Now our simple taxonomy of repository solutions
looks like this. The two that support nested metadata are both based on
the [Fedora repository backend](http://www.fedora.info/), which is no
surprise as it is a very flexible component that allows multiple streams
of structured metadata.

<div class="Table48" align="left">

**ID Managed**

**ID Not Managed**

**Flat metadata**

GNU ePrints

DSpace

**Nested metadata**

Fez (sort-of the feature is there but I ran into some bugs trying it
out)

VTLS VITAL

</div>

# <span id="id857341"></span>My opinion

This is my opinion, which is why this is being posted here rather than
on the RUBRIC site, but I think that storing references to database
tables is not a good idea for repositories. Repositories should reflect
the state of an item when it was created, with the name of the person
and department involved **as they were at the time**. If the repository
software stores references to information elsewhere instead then
important information will be lost.

Lookup tables that help you pick canonical versions of author names and
correctly spelled department names are a good idea. But I think that the
details of author affiliation need to be a snapshot in time, and not a
reference to database tables that might change. Although a unique ID as
well might be a good idea, so if I change my name from Petie Sefton to
Peter Sefton to ptsefton you can track me.

I want to be clear that I don't think one should or should not use any
of the above software just because of this issue. What I do think is
that repository implementors need to be aware of the affiliation issue
and work out what they're going to do about it.

My feeling (not a RUBRIC recommendation, my feeling) is that even if one
is using one of the ID managed repositories there should be a plain-text
'snapshot' of author affiliation as well as any managed ID, so that's
not a barrier to using something like Fez or ePrints. For recording
affiliation repositories that allow nested metadata make it much more
straightforward.

Note that I left out a lot of technical detail here – and generalized a
fair bit to make this simple taxonomy of repositories.

(I'll leave the comments open here for a change, so please contribute if
you have anything to add.)

</div>
