---
Title: "Agility on ICE"
Slug: agility
Date: 2006-09-01

---
<div>

Nigel Ward asked me recently to summarize the agile project management
methodology I use at work. The general principle is [explained
well](http://en.wikipedia.org/wiki/Agile_software_development)on the
 Wikipedia.

> Most agile methods attempt to minimize risk by developing software in
> short timeboxes, called iterations, which typically last one to four
> weeks. Each iteration is like a miniature software project of its own,
> and includes all of the tasks necessary to release the mini-increment
> of new functionality: planning, requirements analysis, design, coding,
> testing, and documentation. While an iteration may not add enough
> functionality to warrant releasing the product, an agile software
> project intends to be capable of releasing new software at the end of
> every iteration. At the end of each iteration, the team reevaluates
> project priorities.
>
> Agile methods emphasize realtime communication, preferably
> face-to-face, over written documents. Most agile teams are located in
> a bullpen and include all the people necessary to finish software. At
> a minimum, this includes programmers and their "customers." (Customers
> are the people who define the product. They may be product managers,
> business analysts, or actual customers.) The bullpen may also include
> testers, interaction designers, technical writers, and managers.
>
> [http://en.wikipedia.org/wiki/Agile\_software\_development](http://en.wikipedia.org/wiki/Agile_software_developmen)

I'm involved in two projects that both use agile processes to reduce
risk. We use a lot of the same tools on the two projects, but in
slightly different ways.

1.  ICE is a software development project, that works with two-week
    development iterations. We release (usually) usable code at the end
    of each iteration.

2.  RUBRIC is a project that is assisting a number of institutions to
    build their first Institutional Repository. We do a bit of software
    development, a lot of software testing, and a lot of things that are
    straight project management. We use many of the same tools as ICE.

I'll focus on the ICE experience, because that project has been going
for longer and it's more

The ICE development processes is 'inspired by' XP – Extreme Programming.
XP has a lot of rules and principles, which I can't cite off the top of
my head. We definatley don't do XP. There are no index cards involved,
just for a start. Tried cards. Hated it.

## <span id="id863442"></span>The process

1.  **Start** with a statement of the aims of the project. What is it
    for, what it it going to do. Ours was approved by the powers that
    be, and published on the university website. This is a general
    statement, not a 500 page requirements document.

2.  **Pick a tame customer**. We picked Shirley Rueshle – education
    lecturer extraordinaire. XP says you need one customer embedded in
    the team, but that just didn't work in our context. We have a few
    other stakeholders from various parts of the university as well.

3.  Then **start building something for a live pilot**. Make
    **something** that works. Ask the customer what she thinks, what she
    needs next. Fix what doesn't work and build then next most important
    bit.

4.  Work towards **regular sort-range milestones**. ICE uses a two week
    cycle. The team meets. The programmers and roll-out people report
    what they did. The whole team discusses what's going to be done next
    cycle. They say: “We got 100 work-units done last cycle. Which 100
    units worth of stuff do you want next?

5.  Learn to **get good at estimating** by breaking tasks down into
    units of no more than half a day. This builds trust. You say what
    can be done each cycle and the customers get to believe you.

6.  For major version releases, pick either some **firm release dates**
    or a **set of functionality** that has to be there. ICE did the
    former. We defined what needed to be in version one and worked until
    the features were there.  ICE-RS will work the other way; we'll have
    guaranteed quarterly releases with whatever we have managed to build
    in them.

7.  Use **good development practices** and tools:

    -   Test-first programming, to define the and document the expected
        behaviour of your code.

    -   Revision control.

    -   A good IDE.  

    -   Estimating.

## <span id="id857400"></span>Software

I'll say a few words about the software we use.

[Subversion](http://subversion.tigris.org.au/) for version control of
code, documentation, websites. We love Subversion for revision control
so much that we built it into ICE itself.

We use and recommend [Trac](http://trac.edgewall.org/) project
management software, with some added macros by Sally Macfarlane of USQ
which help with estimation and give summaries of the tasks assigned to a
particular milestone. Trac has a wiki for communal pages and a slightly
clumsy but workable job-ticket system. The tasks and the wiki are well
integrated.

And Trac knows all about subversion, so you can sign-off on a task right
there in your commit statement...

    svn commit -m “Fixes #1234”

... and ticket 1234 is closed for you, with a link to the subversion
change-set you just committed.

For unit testing we travel
[py.test](http://codespeak.net/py/current/doc/test.html) and
[UTF-X.](http://utf-x.sourceforge.net/)

And, of course the ICE team uses ICE for documentation, and to build the
[ICE website](http://ice.usq.edu.au/).

</div>
