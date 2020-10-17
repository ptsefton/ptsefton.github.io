---
Title: "Styles clarified"
Slug: styles_clarified
Date: 2005-09-18

---
<div>

I've been going on here about using styles, but some concrete examples
are probably worthwhile as Bryan D. Wilhite has [asked on his
blog](http://www.kintespace.com/rasxlog/?p=198) about what I mean by
this:

> why not use the built-in word processing features and layer your
> semantics on top of them? Use the methods already provided for
> expressing your own semantics. Method number one is styles. Method
> number two is tables. This approach will work in versions of Word that
> don't have XML export, and with forthcoming Word formats that have
> been announced but not released and with other word processors that
> save in XML such as OpenOffice.org Writer.

> <http://ptsefton.com/blog/2005/08/13/more_on_microsoft_word_vs_xml_schemas>

Mr Wilhite shows how he uses his clean XTHML tool to write his blog in
Word 2003, and wonders whether I use tables where he uses XML elements
mixed in with Word's markup. The answer is no. I don't use tables. I
[use styles](http://ptsefton.com/blog/2005/03/02/use_styles).

First of all, there's one area we have in common. A paragraph is a
paragraph.

In his screenshot it appears that Bryan has used Word's built in
structure to represent paragraphs. It looks like links are handled in a
similar way – using Word's built-in hyperlinking function. Again, when I
am producing a blog entry that's what I do too (only I am using
OpenOffice.org Writer, not Word).

Where we differ is in the use of inline elements like `acronym`.

(In the spirit of Bryan Whilite's self-referential post I have added the
style names I used to write this post to the rest of the paragraphs).
`{p}`

So, to answer Bryan Wilhite's questions of me: `{p}`

-   For the example you have given I would not resort to tables, but
    would use the in-build word processor structures for paragraphs,
    links and images. In your example I'd use a style like 'p' for every
    paragraph and then have the back-end code turn that into an XTHML ``

    . `{li1b}`

    For the inline elements, such as acronym I'd use a character style.
    In the ICE system, we use character styles based on XHTML element
    names so you would mark XML with the character-style `i-acronym`.
    (For a list of the styles we use see [my word processing
    site](http://trac.officecontent.net/wiki/WpInteropStyles)). `{li1p}`

    Where I would use tables would be in a case like a sidebar or in the
    educational context, a reading or an activity. Say I want to put in
    an activity, I would use a table with two cells in one column. The
    top cell would contain a paragraph in style `h-activity`, and the
    bottom cell would contain the activity itself, a mixture of text and
    graphics. The back-end processing system would recognize that it's
    dealing with an activity and could treat it specially, probably by
    throwing away the table code and putting the activity into a iv
    `class='activity'>`.

-   I don't think much about the Word XML task pane, I have never used
    Word's XML features in the way that you're using them, because as
    [noted before
    here](http://ptsefton.com/blog/2005/08/13/more_on_microsoft_word_vs_xml_schemas)
    I think they are a bad idea for writing documents. `{li1b}`

-   It's a bit tricky to answer Bryan's final question about what's
    wrong with the system he's built. I think it is solving a problem
    that I don't have. I wouldn't like to try to roll it out to authors
    here are the university because: `{li1b}`

    1.  It uses Word 2003, which means it locks out Mac and Linux users
        and probably working from home for many people. `{li2n}`

    2.  It uses WordProcessingML which is about to become obsolete and
        code that runs in Word that I would not like to try to run in a
        server environment. `{li2n}`

    3.  It requires users to deal with new interface elements like the
        XML task pane. `{li2n}`

    4.  We have [our own way of making XHTML](http://ice.usq.edu.au/)
        which uses styles to do most of the heavy lifting, and can
        create course-packages for upload to a Learning Management
        System. `{li2n}`

So Bryan Wilhite, I have a question for you. Would you be interested in
exploring with me whether we can get your clean XHTML system to use
styles to produce its output? `{p}`

****

</div>
