Does some XML foo to get meeting notes out of your MM file.  FreeMind is great for taking notes very quickly and is highly recommended.  I sometimes project FreeMind on the overhead projector so that everyone can see the notes I'm taking.  The zoom feature (Alt-Down) is very handy so that it isn't too small.

After the meeting you might check-in the .mm file into a source control program (if you are into that kind of thing) and then clean up the notes so that it makes more sense and only the salient points are kept.  Then your run something like:
```
mm2notes WeeklyMeeting.mm -o WeeklyMeeting.html
```
To output the notes in HTML, which you can copy and paste to a variety of places.

## Screen Shots ##

In FreeMind your notes will look something like this:

![http://mm2notes.googlecode.com/svn/trunk/doc/free-mind-shot.png](http://mm2notes.googlecode.com/svn/trunk/doc/free-mind-shot.png)

After running mm2notes on your .mm file the HTML will look like like:

![http://mm2notes.googlecode.com/svn/trunk/doc/html-shot.png](http://mm2notes.googlecode.com/svn/trunk/doc/html-shot.png)

## Features ##

Attendees can be just a list, at list with e-mails under the person's name (very handy) or a list of cities with the list of people in each city below.

Because FreeMind keeps track of all the times that nodes are created I used that time to organize the meeting minutes.  So even though you may freely jump around adding notes under different people or headings, it'll still organize it by time, so it still makes some sense.

## Requirements ##

  * [FreeMind](http://freemind.sourceforge.net/wiki/index.php/Main_Page)
  * [Python](http://www.python.org/)
  * [ElementTree](http://effbot.org/zone/element-index.htm) which you'll have automatically if you run Python 2.5 or greater.