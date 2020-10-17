---
Title: "Classy web templates - take two"
Slug: classy_web_templates_-_take_two
Date: 2005-05-29

---
A while ago I wrote a piece called [Classy web
templates](blog/2004/09/22/classy_web_templates_using_plain-old_html)
which is a minor source of incoming traffic from search engines,
although I don't think the people arriving here are going to be all that
impressed - they probably meant classy as in *classy*, not classy as in
*uses the class attribute to identify areas for replacement or
content-substitution in a web templating system based on ordinary web
pages functioning as templates*. Poor things.

I still think that my approach is classy, though. The idea is that you
express the template for a site (or part thereof) in plain old HTML,
with some example content, and simply mark the variable parts with a
class attribute. No fancy extra syntax, and definately no PHP or ASP
style embedded code.

I have now put the code for 'classy web templates' into a [new bit of
Python
code](http://trac.officecontent.net/browser/wpinterop/trunk/apps/sitemap/)
that's available at
[trac.officecontent.net](http://trac.officecontent.net), as part of the
sitemap class. The tests use
[py.test](http://codespeak.net/py/current/doc/test.html). Not much in
the way of documentation yet. You can use the sitemap as an ultra-simple
template system in any application, or take advantage some extra
functionality that lets you manage the presentation of a site driven by
path-like URLS. More on the sitemap part later.
