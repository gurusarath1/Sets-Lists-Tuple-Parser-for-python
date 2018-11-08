# Written by Guru Sarath
# Date: 1st Nov 2018

import LST_Parser as LST

fp = open('LST_Sample.txt')
lineX = fp.readline()
while lineX:
	op = LST.LST_parse(lineX.strip())
	print(op)
	lineX = fp.readline()



"""
INPUT -----------
['AXC',2.6,3,4,'AB']
(67,23,97,0,45)
{1,2,2,2,2,     3, 5   }
[(1,2),("AB",1,3,4,7,{1,2,3,'A','C','1'})]
12
"ABCF"
{1,2,3
(1,2,3]
[]
[[1,2,3]]


OUTPUT -----------
['AXC', 2.6, 3, 4, 'AB']
(67, 23, 97, 0, 45)
{1, 2, 3, 5}
[(1, 2), ('AB', 1, 3, 4, 7, {1, 2, 3, 'C', 'A', '1'})]
12
ABCF
Invalid
Invalid
Invalid
[[1, 2, 3]]
[Finished in 0.1s]
"""