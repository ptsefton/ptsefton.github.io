---
Title: "Unit testing for VBA in 2 minutes"
Slug: vba_unit_tests
Date: 2007-03-13

---
<div>

Here's the story of how I came to write a 5 line [unit
test](http://en.wikipedia.org/wiki/Unit_test) framework for use in
Microsoft Word macros. OK <span class="spCh spChx2013">–</span> so it's
not a framework, but it's very useful.

It's been a long time since I've written more than a few lines of VBA.
That's Visual Basic for Applications. It's not exactly a pleasant
experience, rather like communicating with the computer via grunts.
String manipulation in particular is a real pain after using languages
with regular expressions built-in. I guess these days in the Windows
world you can use the .NET libraries with your choice of language; C\#,
VB, even Python. But for code that will work across lots of version of
Word and on the Mac it's still VBA.

At the [ICE project](../http%3B//ice.usq.edu.au) we're attempting to
improve our user interface, which means putting in some new toolbar
buttons to apply style features. Want a bulleted list? Hit the bullet
button. Want to increase or decrease the level of indent on a list item?
Or promote or demote a heading? Use the new array of buttons.

The buttons will look something like:

     * 1. (a) (A) (i) (I) | <- -> | [P] [H] [B] [I]

Thats demote `->`, promote `<-`, bullet, a few kinds of lists, H for
heading and Bold and Italic. Obviously the buttons will look nicer than
those shown above. I've left off blockquotes and a few other things.

Anyway, to make all this happen there needs to be some fairly smart code
behind the scenes. What should happen if I press the 'promote' or
'de-indent' left-pointing button when I'm typing an ordinary paragraph
like this? Nothing much. How about the 'demote' button? Should that give
me a blockquote? I think so, but maybe a bulleted list. There are **a
lot** of permutations to think about.

Over the last few years I've become used to taking a test-first approach
to this kind of problem. We can sit down and map out the behaviour we'd
like and express it as a set of tests that both specify and document the
code we're writing.

Enter the unit test framework for VBA. Only there doesn't seem to be
one.

So I wrote this five line subroutine.

    Sub AssertEqual(name, string1, string2)

        If string1 <> string2 Then

            MsgBox ("Failed: " + name + ": '" + string1 + "' <> '" + string2 + "'")

        End If

    End Sub

All this does is take a test **name** and **two things** that are
supposed to be the same (they're called strings in my code but actually
they're variants which could contain anything, silly me) and compare
them. If they don't match then it throws up a message box. That's all.

Then all I had to do was write a test subroutine. Here's a few sample
tests:

     Sub tests()

        Call AssertEqual("Don't Indent li1b after p", Indent("li1b", "p"), "li1b")

        Call AssertEqual("Indent li1b after li1b", Indent("li1b", "li1b"), "li2b")

        Call AssertEqual("Indent p after li3b", Indent("p", "li3b"), "li3p")

        Call AssertEqual("Indent p after bq2", Indent("p", "bq2"), "bq2")

        Call AssertEqual("Indent p after dt1", Indent("p", "dt1"), "dd1")

        Call AssertEqual("Indent p after p", Indent("p", "p"), "bq1")

        Call AssertEqual("Indent li5b", Indent("li5b", "li5b"), "li5b")

    End Sub

Take one line of this:

        Call AssertEqual("Indent li1b after li1b", Indent("li1b", "li1b"), "li2b")

This is saying, when I'm currently in style li1b, a first level bulleted
list, and the previous style is the same when I press the demote `->`
button I want the result to to be a second level bulleted list

The idea is to write the tests before the `Indent()` function; I have
started the job in an iterative way. Add a few tests, write a bit more
code. You can see yesterday's version of [the
code](http://ice.usq.edu.au/trac/browser/ice/trunk/templates/word-macros/toolbar.txt?rev=6472)
on the ICE website; I have built on stuff written by other USQ staff,
and they'll go on to do more.

I didn't bother with all the usual unit test framework stuff, counting
tests, reporting on which ones worked and didn't and so on, just an
annoying message box that pops up when something fails. This a great
incentive to make things work, cos clicking the box is really annoying.

</div>
