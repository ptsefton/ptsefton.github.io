---
Title: "Some sample lists using styles"
Slug: list-samples
Date: 2006-06-13

---
<div>

I have been talking in email with Stuart Stuple, a Microsoft Program
Manager for Word.

Stuart asked me to clarify what I meant by ‘a list’ – I thought I’d do
so publicly because if I’m confusing the experts then I might be
confusing some of the rest of you.

I’ll start with some lists that Stuart sent me, and show you how they
look in Word.

Stuart’s list:

1.  My point

    1.  Ordered entry

    2.  Ordered entry

    3.  Ordered entry

2.  My point

    -   Unordered entry

    -   Unordered entry

Here’s a screenshot of how that looks in Word when I’m writing it:

<span
id="graphics1"></span>![graphics1](/blog/2006/06/13/list-samples/1.png)

The styles show to the left. You don’t need to remember the cryptic
names, though, as there is a nice menu for applying them and keyboard
shortcuts:

<span
id="graphics2"></span>![graphics2](/blog/2006/06/13/list-samples/2.png)

What we have here is three lists. An ‘outer’ numbered list with two
sub-lists, one ordered and one unordered.  You can view the source of
this page to see how it comes out in HTML. If you’re viewing this page
via the ATOM feed on my site then you may not see the correct style of
numbering, ICE needs to be fixed up so it adds a ‘style’ attribute to
lists.

    <p>Stuart’s list:</p>
        <ol class="lin">
            <li>
                <p>My point</p>
                <ol class="li-lower-alpha">
                    <li>
                        <p>Ordered entry</p>
                    </li>
                    <li>
                        <p>Ordered entry</p>
                    </li>
                    <li>
                        <p>Ordered entry</p>
                    </li>
                </ol>
            </li>
            <li>
                <p>My point</p>
                <ul class="lib">
                    <li>
                        <p>Unordered entry</p>
                    </li>
                    <li>
                        <p>Unordered entry</p>
                    </li>
                </ul>
            </li>
        </ol>

The three lists are implied by the styles. There is no actual list
structure underneath, except what Word constructs internally – and
authors don’t have to worry too much about that because the ICE styles
clearly imply the nesting.

You can’t use a single outline list to do this, because there are two
different things going on at the second level. Outline lists would be
good if you were working in an environment (like law) where the
numbering is always going to be a certain way. More on outline lists
below.

Another of Stuart’s lists:

1.  Test1

    1.  Sample paragraph

        Separate paragraph

    2.  Another sample paragraph

2.  Test2

    Test3

    Test4

Here we have two lists. I’d say that the above is one two-item list
(Test 1, Test 2) with another list embedded in it.

Looks like this in the word processor:

<span
id="graphics3"></span>![graphics3](/blog/2006/06/13/list-samples/3.png)

You can see that to continue a list item you use the ‘liXp’ style where
‘X’ is the appropriate level.

A new lists starts when you put in a style that implies it. So if you
have a paragraph in plain-old ‘p’ style followed by a li1n then that
means start a new numbered list. The algorithm is fairly simple. Does
the next item belong inside the same container as me? If so, include it,
otherwise close the container and start a new one.

The styles are a kind of contract with the ICE software. And they can
mix and match with other styles like blockquotes and pre-formatted text.
So if I were to quote someone I would use a blockquote style. Let’s
quote the example above.

Putting the first line in bq1 style starts a new quote, and the styles
imply that the lists belong in the quote.

> Another of Stuart’s lists:
>
> 1.  Test1
>
>     1.  Sample paragraph
>
>         Separate paragraph
>
>     2.  Another sample paragraph
>
> 2.  Test2
>
>     Test3
>
>     Test4
>
Or I could include preformatted text in a list, say in a user guide:

1.  Type this:

        cd ~
        ls

2.  Make a cup of tea.

Which looks like this with the styles showing:

<span
id="graphics4"></span>![graphics4](/blog/2006/06/13/list-samples/4.png)

Without styles converting this stuff to HTML is basically impossible;
how do you know where lists start and end? Which bits are quotes? Which
bits are pre-formatted?

Behind the scenes, our lists are actually associated with Word outline
lists. Here’s another screenshot showing the Bullets and Numbering…
 dialog This is showing the formatting for the style ‘li3a’.  This is
part of the outline called LLowercaseAlpha. I’m still not sure why this
optional name field was not used more fully in Word and why list styles
were introduced.

(Don’t try this at home, kids. Read [<span class="Internet_20_link">my
previous
post</span>](http://ptsefton.com/blog/2006/06/07/word_lists_without_tears)
about how to manage lists using macros. Even while writing this post I
had some bizarre and unusual things happen to my lists, but because I’m
using [<span class="Internet_20_link">the ICE
template</span>](http://ice.usq.edu.au/instructions/downloads.htm) I can
run a macro to fix up most of the issues.)

<span
id="graphics5"></span>![graphics5](/blog/2006/06/13/list-samples/5.png)

We don’t set up outline lists for every possible combination, because
it’s not possible, but we do use them to group together all the
formatting for each type of numbering. So all five levels of lowercase
Roman numbered lists are part of the same outline.

There’s lots more to this list business but we find that with a couple
of hours of experience most users get the hang of it. The best teacher
is the ICE rendering system which turns styled Word documents into HTML
in a couple of seconds, so users can see how their implied lists are
interpreted by the ICE formatting software.

I’d love to see a similar (optional) approach in Word 2007 for blogging
and general-purpose HTML export.

Why not make an ICE-like template that bloggers can use to produce posts
like this one, complete with lovely nested structures?

</div>
