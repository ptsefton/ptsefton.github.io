---
title:  >
  DataCrate: a method of packaging, distributing, displaying and archiving Research Objects
date: 2018-10-29
slug: sefton-ro2018
category: DataCrate
author: Peter Sefton
---

Here are the slides for presentation I delivered this week at [Research Object 2018](http://www.researchobject.org/ro2018/)
in Amsterdam. The [paper we wrote for this workshop](https://doi.org/10.5281/zenodo.1445817)
is available. The contributors to the article are:

- Peter Sefton
- Michael Lynch
- Gerard Devine
- Duncan Loxton
- Sharyn Wise
- Christian Evenhuis

This presentation is _my_ view on some the issues in data packaging and linked
data metadata. In addition to giving a quick intro to DataCrate I tried to
contrast it with the [Research Object](http://www.researchobject.org/) and [Frictionless Data](https://frictionlessdata.io/data-packages/)
approaches and to talk about some of the issues we had with software tooling for
linked data in JSON-LD.


<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide01.png' alt='' title='' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 1

</summary>


DataCrate is a specification for packaging research data for distribution and reuse. DataCrate packages may be distributed as archives with or without compression, and hosted on web sites, as they contain an index.html page that summarizes the contents of the package for human readers. For machines, there is a JSON-LD file containing metadata that will aid in the re-use of the data including licensing, publication dates, parties involved in creating the data. Where possible the terms from schema.org are used for metadata, with other ontologies used where needed. DataCrate optionally uses the BagIt data packaging standard which is widely used in libraries and archives and increasingly in research data management, including in recent discussions about data packaging at the Research Data Alliance (RDA).



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide02.png' alt='
🧙‍♂️
' title='
🧙‍♂️
' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 2

</summary>


Hi, I’m Peter, you can call me Petey.

I’ve made a solemn vow never to invent an ontology. 

Also, I seem to have become the main contributor to a new standard. This was NOT one of my ambitions as a kid, frankly I’d like to spend my spare time playing or writing music rather than maintaining standards.



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide03.png' alt='Motivation: package data with maximum useful context
Who …  made it? funded the work? 
What … format are these files? … is the research about?
Where … was it collected? … is it about? 
Why … was it done?  … &lt;link to publication&gt;
How … were these files created? … can I repeat that process? 
' title='Motivation: package data with maximum useful context
Who …  made it? funded the work? 
What … format are these files? … is the research about?
Where … was it collected? … is it about? 
Why … was it done?  … &lt;link to publication&gt;
How … were these files created? … can I repeat that process? 
' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 3

</summary>


We wanted to be able to show data on the web and distribute it with useful metadata. That means allowing a data packager to anticipate what others (including their future self) might want to do with data, and providing enough detail on data provenance to make that possible.




</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide04.png' alt='

' title='

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 4

</summary>


The [spec is available on github](https://github.com/UTS-eResearch/datacrate/blob/master/spec/1.0/data_crate_specification_v1.0.md)



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide05.png' alt='

“As a researcher…I’m a bit bloody fed up with Data Management”
Cameron Neylon
' title='

“As a researcher…I’m a bit bloody fed up with Data Management”
Cameron Neylon
' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 5

</summary>


Here’s an example. This is the dataset used as the test-case for the first [DataCrate](https://data.research.uts.edu.au/examples/v1.0/Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies/CATALOG_files/pairtree_root/Po/li/cy/%5E2/0a/nd/%5E2/0I/mp/le/me/nt/at/io/n%5E/20/Re/vi/ew/%5E2/0I/nt/er/vi/ew/s=/In/te/rv/ie/w_/Au/di/o=/In/te/rv/ie/w-/25/_0/9_/20/15/-1/4_/02/-S/im/on/_H/od/so/n,/fl/ac/index.html). 

This came from Cameron Neylon’s [As a researcher…I’m a bit bloody fed up with Data Management](http://cameronneylon.net/blog/as-a-researcher-im-a-bit-bloody-fed-up-with-data-management/), which I covered in the [First presentation about DataCrate](/2017/10/19/datacrate.htm)



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide06.png' alt=' 🛄it 
+
⛓💾 
+
 &lt;html&gt;&lt;/html&gt;
+

' title=' 🛄it 
+
⛓💾 
+
 &lt;html&gt;&lt;/html&gt;
+

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 6

</summary>


DataCrate uses several standards:

 🛄it - BagIT

⛓💾  - Linked data as JSON-LD

 &lt;html&gt;&lt;/html&gt; - HTML

And the [Schema.org](http://schema.org) vocabulary.







</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide07.png' alt='' title='' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 7

</summary>


Human-readable [HTML data about files](https://data.research.uts.edu.au/examples/v1.0/sample/CATALOG_files/pairtree_root/pi/cs/=2/01/7-/06/-1/1%5E/20/12/,5/6,/14/,j/pg/index.html) including detailed metadata.





</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide08.png' alt='

' title='

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 8

</summary>


Which allows us to describe [individual items of equipment](https://code.research.uts.edu.au/MIF/microscope-instructions/wikis/Nikon-Ti/Nikon-Ti-inverted-epifluorescent-microscope) ...

As [Carl Kesselman](https://www.isi.edu/~carl/) said at the workshop:

> Why isn't [FAIR](https://www.force11.org/group/fairgroup/fairprinciples) important when you take it off the microscope?


Chris Evenhuis at UTS thinks the same way. He is doing stuff because it is the **right** thing to do.




</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide09.png' alt='

' title='

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 9

</summary>


… people ...



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide10.png' alt='' title='' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 10

</summary>


All the metadata for a Datacrate is in a [single JSON-LD file](https://data.research.uts.edu.au/examples/v1.0/sample/CATALOG.json). This is easy for programmers to deal with, and in my opinion, much more straightforward than the Research Object approach of using multiple annotation files - this has nothing to do with differences in the information model, its an implementation detail.



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide11.png' alt='

' title='

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 11

</summary>


Processes  by which files are created



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide12.png' alt='URIs as names for things

' title='URIs as names for things

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 12

</summary>


Because DataCrate is based on JSON-LD, and linked data pricnples, each term used can have a link to its definition, eg: <https://schema.org/CreateAction>




</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide13.png' alt='But (🔧🔨🔩🔪🔬)ing is limited:
JSON-LD →  🙅
⛓💾 →  👶 

' title='But (🔧🔨🔩🔪🔬)ing is limited:
JSON-LD →  🙅
⛓💾 →  👶 

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 13

</summary>


Tools (🔧🔨🔩🔪🔬) for humans to generate linked-data are under-developed.

JSON-LD tooling is limited to high-level transformations and there are no easily
available libraries for Research Software Engineers to do simple stuff like
traversing graphs or looking up context keys.

Linked Data data tooling is also extremely lacking, there are very few good
example of systems that allow people to enter linked-data metadata.



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide14.png' alt='⛓💾’s still too much like

🚀⚗️
👩🏽‍🚀👷‍🏗️🏢
🛐
' title='⛓💾’s still too much like

🚀⚗️
👩🏽‍🚀👷‍🏗️🏢
🛐
' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 14

</summary>


Linked data is still too much like rocket science (🚀⚗️) because of all the architecture (👩🏽‍🚀👷‍🏗️🏢) astronauts.


[Joel Splosky](https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/):

> These are the people I call Architecture Astronauts. It’s very hard to get them to write code or design programs, because they won’t stop thinking about Architecture. They’re astronauts because they are above the oxygen level, I don’t know how they’re breathing. They tend to work for really big companies that can afford to have lots of unproductive people with really advanced degrees that don’t contribute to the bottom line.


There’s also religious aspect to some of this.



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide15.png' alt='
Stop treating ontologies like https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/
' title='
Stop treating ontologies like https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/
' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 15

</summary>


We need to stop treating ontologies like toothbrushes (ie avoiding using other people’s) and get on with implementing usable systems.



</details>
</section>
<br/><br/><hr/>

        
<section typeof='http://purl.org/ontology/bibo/Slide'>
<img src='{static}Slide16.png' alt='

' title='

' border='1'  width='85%'/>

<details open="open">

<summary>

### Notes - Slide 16

</summary>


So I’ll finish with a provocation. 

Do we really really need more complicated ontologies when you can describe the what where when and why of research data in a _useful_ way with schema.org and JSON-LD? We need to recruit content and get experience describing it, not wait.



</details>
</section>
<br/><br/><hr/>

        