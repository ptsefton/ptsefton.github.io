---
Title: "Learning to live with NeoOffice: applying styles via the keyboard"
Slug: neo-office-keys
Date: 2006-09-22

---
<div>

[NeoOffice](http://www.neooffice.org/)is OpenOffice.org for the Mac.
It's certainly nicer to use. Looks better. You can actually copy from
other applications and paste into a document, a feature that no longer
even works sometimes with the X11 version.

There was one thing that stopped me from adopting it, though. Like other
Mac apps it has no Alt-key access to menus even though the windows and
Linux versions do. I have been typing `Alt-s` to bring up a **styles
menu** for  ICE styles and their predecessors since 1997.  <span
class="T1">Alt-s h</span> gets me a heading.  `Alt-s l 1 b` gets me a
bulleted list. It's a few key strokes but it's very quick to use.

There are way too many ICE styles to bind each one to a key combination.

Today, between 6:24 and 6:29, before I even made coffee I came up with
the start of a solution that will make NeoOffice bearable.

First of all – I added this to the WPInterop macros that come with ICE.

    function GetStyle()  
      styleName = InputBox("Style?")  
      'TODO - allow abbreviations such as 'l2b' for 'li2b' 
      'and 'l' for 'li1b'  
      SetStyle(StyleName) 
    end function

Then I used Tools / Customize to bind that macro to `Cmd-9`. The key
binding seems to be attached to NeoOffice itself, whereas the macro
resides in the template and is copied into each new document instance by
NeoOffice.

Now `Cmd-9 `gives me a text input box and I can type the name of the
style I need. ICE styles have short names, but as the comment in the
code says this macro could be improved with a bit of string handling to
allow shortcuts.

Kylie will put this into the ICE Writer template soon and we'll start
incrementally improving it. We could do one for Word too – it doesn't
support Alt-Keys either.

Note that NeoOffice does not come with Python (it should, must be a
mistake) so you need to install the X-11 version as well and get it to
listen on port 2002  to get ICE to work, at least for now.

</div>
