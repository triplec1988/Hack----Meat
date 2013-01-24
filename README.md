Slot for Slaught
=========

Created by Gabriel Key, Ethan Lo, Chris Clouten, and Jacob Duron.

2nd Place Hack//Meat hackathon December 8-9, 2012.

"Slot for Slaught is a tool to better manage and coordinate the scheduling and processing of animals through meat facilities and enhance communication flow between producers and processors. Farmers can find details about specific plants, book availability for slaughtering, and submit information about their order. Custom or stock follow-up emails can also be generated."

-- [The Next Web](http://thenextweb.com/2012/12/11/carnivores-cut-code-to-hack-meat/)

http://www.slotforslaught.com
http://hackmeat.wikispaces.com/About

Running Slot for Slaught on your local machine
======

1. Open hackmeat/settings.py
2. Uncomment 'local' entry in DATABASES
3. Run `DJANGO_LOCAL=True manage.py syncdb'
4. Run `DJANGO_LOCAL=True manage.py runserver'