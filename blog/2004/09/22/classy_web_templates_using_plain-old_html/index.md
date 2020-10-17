---
Title: "Classy web templates using plain-old HTML"
Slug: classy_web_templates_using_plain-old_html
Date: 2004-09-22

---
The polymathematical James Tauber, author of the
[software](http://james.tauber.name/leonardo) that runs this site has
announced that he's [working on the next
version](http://jtauber.com/blog/2004/09/18/leonardo_rewrite). Which has
prompted me to dust-off one of my firmly held opinions about the best
way to do HTML templates and offer it for consideration.

I think the best mechanism is to use plain-old HTML pages (best if it's
well-formed XML, XHTML even), with class names to mark the substitutable
bits.

How does it look?

This is is a tiny sample. Elements with a class attribute that begins
with 'ins ' would have their content replaced with runtime data, in this
case with a bit of data called 'page-title'. The designer can also
supply a CSS stylesheet with a rule for 'page-title'. (You're allowed to
have multiple space-separated classes, apparently.)

    <html>
    <head>
    <title class='ins page-title'>Placeholder title</title>
    </head>
    <body>
    <h1 class='ins page-title>Placeholder title</h1>    

> ...

Why is this the 'best' way?

-   Templates are completely implementation-language neutral.
-   Designers can work with sample files with their web page and CSS
    design tools of choice, without worrying about yet another set of
    proprietary codes.
-   If the world was perfect, we could all agree on some standard names
    for page elements and then we could swap templates between
    applications. Yes I know, I am being silly.

Limitations? Well it is meant to be very simple.

First of all the fact that you can't embed code in your template, is
emphatically not a limitation. Code does not belong in a web page
template. If you want that kind of thing go see the PHP, ASP or JSP
people.

The minor limitation is that this approach makes it a bit hard to use a
simple regular expression or string interpolation to populate your
template, as the place-holder elements could contain fairly extensive
sample content.

In the case of Leonardo you could pre-compile the templates, so

    <title class='page-title'>...</title> 

ends up just the way it is in the current version of Leonardo:

    <title class='page-title>%(page-title)s</title>

And the entire template can be populated by feeding it a dictionary with
all your page data in it:

    print template % pagestuff

Or even better, wrap it up in a plain-old HTML template class so you can
say.

    page = plainoldhtmltemplate('basic.htm')
    page'page-title' = 'Home page'
    page.render()

The closest existing thing I can find is
[HTMLTemplate](http://freespace.virgin.net/hamish.sanderson/htmltemplate.html),
which allows you to do what I'm talking about here, and couple of other
things, including adding repeating elements, the only problem being that
it will discard the class attributes.

But really, we are talking about only a few lines of Python here to
build a minimal implementation, so this lunchtime I did:

      import libxml2


      class plainoldhtmltemplate(dict):
          templatestring = ""


          def __init__(self, templatefilename = None):
              if templatefilename:
                  self.loadtemplate(templatefilename)


          def loadtemplate(self, templatefilename):   
              try:
                 rawtemplate = libxml2.parseFile(templatefilename, None)
              except:
                  rawtemplate = libxml2.htmlParseFile(templatefilename, None)


              insertions = rawtemplate.xpathEval("//*starts-with(@class,'ins ')")
              #TODO: 'sub ' for places you want to replace the placeholder
              for insert in insertions:
                  classname = insert.prop('class')4: #after insert
                  selfclassname = ''
                  insert.setContent('%%(%s)s' % classname)


              self.templatestring = rawtemplate.serialize()


          def render(self):
              return self.templatestring % self
