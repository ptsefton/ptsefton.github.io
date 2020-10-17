---
Title: "A quick test to see how an HTML editor behaves with lists, using FCKeditor"
Slug: fckeditor-lists
Date: 2007-06-06

---
<div>

As part of our ongoing discussion of text editing tools Stijn Dekeyser
sent me a link to the FCKeditor [demo](http://www.fckeditor.net/demo).
It does seem like a candidate for us to use as the basis for an online
editing component in [ICE](http://ice.usq.edu.au/), and for some
research we're planning and Stijn reckons that it produces clean XHTML.

But let me share with you my favourite test of an editor. Being
list-obsessed I like to do this.

I make a list:

![graphics1](/blog/2007/06/06/fckeditor-lists/1.jpg)

I did this by typing 'This is my list' then clicking the bullet button
![graphics2](/blog/2007/06/06/fckeditor-lists/2.jpg).

Then I hit enter and pasted the same text in a few times.

Next, I highlighted two of the items in the list and hit the bullet
button again.

![graphics3](/blog/2007/06/06/fckeditor-lists/3.jpg)

Then I hit the bullet button yet again to put back the bullets.

Guess what?

I now have three lists.

![graphics4](/blog/2007/06/06/fckeditor-lists/4.jpg)

To prove it's three lists see the code:

    <ul>  

     <li>This is my list</li>  

     <li>This is my list</li> 

    </ul> 

    <ul>  

    <li>This is my list</li>  

    <li>This is my list</li> 

    </ul> 

    <ul>  

    <li>This is my list</li> 

    </ul>

What **I** want, if I have 5 bullet points in a row is **one list**. I
can't think of a case where I would want three lists like this. All of
the online HTML editors I've looked at recently, and the Windows Live
Writer application from Microsoft have this problem.

There are related problems in the export from OpenOffice.org <span
class="spCh spChx2013">–</span> why can't the editor code be better at
normalizing HTML structure using indents and other formatting cues? It's
not that hard. Some of us at USQ and the ICE-network of associates are
thinking about this problem.

If we were going to do something with FCKeditor this is the first thing
I'd fix.

</div>
