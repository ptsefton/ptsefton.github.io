---
Title: "WebCT Vista: First impressions"
Slug: webct_first_impressions
Date: 2004-11-09

---
Now that I work for USQ I thought I had better find out a bit about the
house LMS, (Learning Management System), so last week I attended the two
basic training courses for staff using the system for teaching online
using *WebCT Vista* version 2.

Here are some first impressions, followed by a bit about how I think a
uni like USQ (and they're not all like USQ) can do better. Note that
this is not a review of the application, it's more of a view of the
application as deployed. And obviously these first impressions are mine,
not those of The University of Southern Queensland.

### First impressions

It'll do. Certainly not bad enough for a teacher to use it as an excuse.

But we can do better. By *we* I mean the entire community.

This is a typical LMS, actually one of the first. It helped define a
genre, which is possibly a problem for it.

### Issues with navigation

I was frustrated with the frame-based navigation. The instructor says
"Don't use the back button". Is it just me or does the back button need
to *work* on a web application?

Related to this I managed to get behind when following on in class by
doing this:

Right click on the help link and ask for a new window, and IE throws up
a JavaScript debugger. Oops. Then when you try to close the debugger
*all* your browser windows disappear.

The interface also has tabs that are supposed to let you switch between
modes; to build the course, or to see how a page would look to a
student. Only they don't simply switch modes, they tend to dump you back
to the course home page, and make you click your way back to where you
were.

So, there are a couple of symptoms (there are more) of an aging web
application, and they're both soluble.

### Content

Content handling is not terrible, particularly if you use the 'Learning
Module' feature that lets you build a table-of-contents-navigable set of
resources using an [outliner](http://en.wikipedia.org/wiki/Outliner). If
all you want is a classroom based ad hoc tool, and you don't mind
calling the help desk to re-use your content from one semester to the
next, then this is fine.

But because these systems are sold on features, not enterprise process,
they have to allow people to upload any kind of content they like,
meaning Word and Powerpoint files in most cases. This, I suspect is the
number one reason the frames are still there, because that allows a
table of contents on the left in good honest HTML, and an in-browser
Word document to appear on the right. Maybe. If the version of word and
your operating system and so on allow it.

This leads us to issues with the enterprise. As a university do you want
your students to see a collection of MS Office files, loosely joined
together by a lecturer who may or may not happen to be good at
organizing files? Or would you prefer to present well-linked collections
of HTML resources, with PDF versions as well (this is the web you know)
with a consistent interface that will be more usable and more reliable?
See this [previous post](blog/2004/05/11/caddie) which talks about some
more reasons not to use Word on the web.

This question has been asked and answered before at USQ; there is a
[Distance and e-Learning
Centre](http://www.usq.edu.au/dec/research/overview.htm) (the DeC, where
I am working) which has processes for standardizing learning materials,
and a heavy-duty XML publishing system to back up those processes,
modestly called [GOOD](http://www.usq.edu.au/dec/staff/good.htm). I
quote:

> The GOOD project has enabled USQ to replace its resource-intensive
> legacy production system for courseware with a single document source
> system based on the XML (eXtensible Markup Language) standard.
> XML-tagged courseware documents are structured within uniform,
> comprehensive parameters with the substantive content able to be
> treated discretely from its layout and presentation.

I believe the challenge we face now is to bridge the gap between the
enterprise-strength GOOD system and the teaching staff. How can we
assist them with course delivery frameworks that offer the right blend
of *flexibility*, to do justice to the teaching and learning process,
and *consistency*, so the learners don't get lost, and the university's
high publishing, presentation and pedagogical standards are maintained?

### An enterprise approach

Rather than a free-for all approach to structuring materials using what
WebCT calls *organizers* which would be *folders* anywhere else, or
*directories* in Unix, how about a 'smart outliner' for constructing
your course table of contents with some rules about the way we do things
*here*?

We haven't had a recipe on this site for a while, have we? (the loquat
jam went mouldy; maybe I should post it as a cautionary tale).

### Online course

#### Ingredients

-   One Introduction.

<!-- -->

-   One Staff profile section.

<!-- -->

-   One Assessment section, where you set out the assignment and exam
    dates and rules.

<!-- -->

-   One or more learning modules.

<!-- -->

-   One resources section.

<!-- -->

-   Activities, choose a tasty selection of readings, formative quizzes,
    etc.

#### Method

Present the ingredients in the following order: Introduction, Staff
profile, Assessment, then all the modules, served nestled in a
study-schedule in the order they'll be covered in class. Sprinkle the
modules with activities, and follow with a set of resources.

——

It wouldn't be hard to add a configuration layer in the content handler
for an LMS that allowed for one or a few of these kinds of recipes to be
on the menu for people preparing courses, maybe in addition to the
current free-for-all.

You would be able to pick a pattern that suits your course and build
away knowing that you will be generating courseware that will have the
same interface as other courseware from the same institution.

There still needs to be room for the courses that don't fit a standard
model, and for innovation, but on the other hand, the poor learners
don't need the additional challenge of trying to find their way around
something that's organized like a lecturer's hard drive.

\$LastChangedDate: 2004-11-09 07:03:47 +1000 (Tue, 09 Nov 2004) \$ -
\$Rev: 25 \$
