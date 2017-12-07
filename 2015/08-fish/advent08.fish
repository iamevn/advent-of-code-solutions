#!/usr/bin/fish

#this expects the input in a file called 'input'
echo "Part 1:"\
     (math (wc -c input | sed "s/ .*\$//") -\
           (sed "s/^\"//;\
                 s/\"\$//;\
                 s/\\\\\\\\/#/g;\
                 s/\\\\\"/#/g;\
                 s/\\\\\x[0-9a-f][0-9a-f]/#/g"\
                 input | wc -c))

echo "Part 2:"\
     (math (sed "s/\"/##/g;\
                 s/\\\\/##/g;\
                 s/^/#/;
                 s/\$/#/"\
                 input | wc -c)\
        - (wc -c input | sed "s/ .*\$//"))
