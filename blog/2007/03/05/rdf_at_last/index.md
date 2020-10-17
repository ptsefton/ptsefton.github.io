---
Title: "RDF appears on my short-range radar"
Slug: rdf_at_last
Date: 2007-03-05

---
<div>

I [wrote
today](http://ptsefton.com/blog/2007/03/05/zotero_word_processor) about
Zotero, which uses
[RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework)
metadata, in a way that I have not yet grasped.

RDF has been coming up a lot in our work on the RUBRIC project as well
lately. It's been around for quite a while, but I have never had to deal
with it, or felt that I needed it. Now I'm beginning to see how it can
be used for descriptive metadata, like in Zotero and how it might be
useful for constructing interfaces and authorization systems for
institutional repositories. The bit I had never thought of before is to
use RDF to describe ontologies such as subject classification or
organization structures, and be able to build applications that
understand the relationships between items based on these ontologies.

I'm using the word **ontology** in the computer-science sense <span
class="spCh spChx2013">–</span> sounds a bit odd to me in this context
but that's how the RDF community talk. Here's part of what Wikipedia
said about [Ontology (computer
science)](http://en.wikipedia.org/wiki/Ontology_(computer_science)%20):

> In both computer science and information science, an ontology is a
> data model that represents a set of concepts within a domain and the
> relationships between those concepts. It is used to reason about the
> objects within that domain.
>
> http://en.wikipedia.org/wiki/Ontology\_%28computer\_science%29

Here's how it might work, in three steps:

1.  Repository manager **defines an ontology** for, say, the structure
    of a university, with all the faculties, schools, departments and so
    on. RDF does not have to be a tree-structure, so you can **express
    complex relationships** such as you might get when an institute has
    multiple parents.

2.  Repository manager defines **metadata mappings** between descriptive
    metadata 'this item belongs to the Maths Department' and RDF
    expressions that make the link between the item and the organization
    structure.

3.  The repository software finds and infers all the relationships
    inherent in the metadata and the university structure; it will know
    that a paper written by an author in Maths, is **automatically part
    of the Faculty** of Science, for example. This is the 'reason about'
    mentioned by Wikipedia; and it's the ability to do this reasoning,
    within reason, that is of value when using RDF.

    This means being able to broaden and narrow searches by department,
    control access across the university heirarchy and build
    browse-based indexes all **automatically**.

I think there will be a lot of RDF in the rest of my year 2007, trying
now to get the various projects I'm involved in to come up with some
demos of the three-step RDF-ization of an Institutional Repository.

</div>
