#! /usr/bin/python2
r14_header = '''  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1014
  9
$HANDSEED
  5
FFFF
  9
$MEASUREMENT
 70
     1
  0
ENDSEC
  0
SECTION
  2
TABLES
  0
TABLE
  2
VPORT
  5
8
330
0
100
AcDbSymbolTable
 70
     4
  0
VPORT
  5
2E
330
8
100
AcDbSymbolTableRecord
100
AcDbViewportTableRecord
  2
*ACTIVE
 70
     0
 10
0.0
 20
0.0
 11
1.0
 21
1.0
 12
210.0
 22
148.5
 13
0.0
 23
0.0
 14
10.0
 24
10.0
 15
10.0
 25
10.0
 16
0.0
 26
0.0
 36
1.0
 17
0.0
 27
0.0
 37
0.0
 40
341.0
 41
1.24
 42
50.0
 43
0.0
 44
0.0
 50
0.0
 51
0.0
 71
     0
 72
   100
 73
     1
 74
     3
 75
     0
 76
     0
 77
     0
 78
     0
  0
ENDTAB
  0
TABLE
  2
LTYPE
  5
5
330
0
100
AcDbSymbolTable
 70
     1
  0
LTYPE
  5
14
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
BYBLOCK
 70
     0
  3

 72
    65
 73
     0
 40
0.0
  0
LTYPE
  5
15
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
BYLAYER
 70
     0
  3

 72
    65
 73
     0
 40
0.0
  0
LTYPE
  5
16
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
CONTINUOUS
 70
     0
  3
Solid line
 72
    65
 73
     0
 40
0.0
  0
ENDTAB
  0
TABLE
'''


r14_style = '''  0
ENDTAB
  0
TABLE
  2
STYLE
  5
3
330
0
100
AcDbSymbolTable
 70
     1
  0
STYLE
  5
11
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2
STANDARD
 70
     0
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
2.5
  3
txt
  4

  0
ENDTAB
  0
TABLE
  2
VIEW
  5
6
330
0
100
AcDbSymbolTable
 70
     0
  0
ENDTAB
  0
TABLE
  2
UCS
  5
7
330
0
100
AcDbSymbolTable
 70
     0
  0
ENDTAB
  0
TABLE
  2
APPID
  5
9
330
0
100
AcDbSymbolTable
 70
     2
  0
APPID
  5
12
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD
 70
     0
  0
ENDTAB
  0
TABLE
  2
DIMSTYLE
  5
A
330
0
100
AcDbSymbolTable
 70
     1
  0
DIMSTYLE
105
27
330
A
100
AcDbSymbolTableRecord
100
AcDbDimStyleTableRecord
  2
ISO-25
 70
     0
  3

  4

  5

  6

  7

 40
1.0
 41
2.5
 42
0.625
 43
3.75
 44
1.25
 45
0.0
 46
0.0
 47
0.0
 48
0.0
140
2.5
141
2.5
142
0.0
143
0.03937007874016
144
1.0
145
0.0
146
1.0
147
0.625
 71
     0
 72
     0
 73
     0
 74
     0
 75
     0
 76
     0
 77
     1
 78
     8
170
     0
171
     3
172
     1
173
     0
174
     0
175
     0
176
     0
177
     0
178
     0
270
     2
271
     2
272
     2
273
     2
274
     3
340
11
275
     0
280
     0
281
     0
282
     0
283
     0
284
     8
285
     0
286
     0
287
     3
288
     0
  0
ENDTAB
  0
TABLE
  2
BLOCK_RECORD
  5
1
330
0
100
AcDbSymbolTable
 70
     1
  0
BLOCK_RECORD
  5
1F
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
*MODEL_SPACE
  0
BLOCK_RECORD
  5
1B
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
*PAPER_SPACE
  0
ENDTAB
  0
ENDSEC
  0
SECTION
  2
BLOCKS
  0
BLOCK
  5
20
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockBegin
  2
*MODEL_SPACE
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
*MODEL_SPACE
  1

  0
ENDBLK
  5
21
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockEnd
  0
BLOCK
  5
1C
330
1B
100
AcDbEntity
 67
     1
  8
0
100
AcDbBlockBegin
  2
*PAPER_SPACE
  1

  0
ENDBLK
  5
1D
330
1B
100
AcDbEntity
 67
     1
  8
0
100
AcDbBlockEnd
  0
ENDSEC
  0
SECTION
  2
ENTITIES
'''


r14_footer = '''  0
ENDSEC
  0
SECTION
  2
OBJECTS
  0
DICTIONARY
  5
C
330
0
100
AcDbDictionary
  3
ACAD_GROUP
350
D
  3
ACAD_MLINESTYLE
350
17
  0
DICTIONARY
  5
D
330
C
100
AcDbDictionary
  0
DICTIONARY
  5
1A
330
C
100
AcDbDictionary
  0
DICTIONARY
  5
17
330
C
100
AcDbDictionary
  3
STANDARD
350
18
  0
DICTIONARY
  5
19
330
C
100
AcDbDictionary
  0
ENDSEC
  0
EOF'''
