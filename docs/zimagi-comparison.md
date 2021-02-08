# Comparison of `noaa-stations` tool with `module-noaa-stations`

This document describes differences between an implementation of 
similar functionality within a stand-alone command line tool written
in Python and a Zimagi module.

## Code required 

This snapshot is NOAA-stations commit b910e2e1 with commit 89f227fe of
module-noaa-stations.  Lines of code used and features supported may
change in future revisions.

Zimagi module:

```
module-noaa-stations % cloc .
      17 text files.
      17 unique files.
       9 files ignored.

github.com/AlDanial/cloc v 1.86  T=0.02 s (760.2 files/s, 36315.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
YAML                             8             69             66            272
Python                           4             26             11            110
Markdown                         1             23              0             44
-------------------------------------------------------------------------------
SUM:                            13            118             77            426
-------------------------------------------------------------------------------
```

Command-line tool:

```
NOAA-Stations % cloc .
       7 text files.
       7 unique files.
       3 files ignored.

github.com/AlDanial/cloc v 1.86  T=0.01 s (789.9 files/s, 30489.7 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           2             12             34             85
Markdown                         2             21              0             31
YAML                             1              0              0             10
-------------------------------------------------------------------------------
SUM:                             5             33             34            126
-------------------------------------------------------------------------------
```

*Note*: The small YAML file in NOAA-Stations is a conda environment 
configuration file.  It is only indirectly related to the tool itself,
but providing the necessary dependencies is reasonable to consider part
of tool requirements.  A pip `requirements.txt` would be similar length.

*Note2*: The Markdown files in both repositories are entirely documentation
and are not directly related to the functionality of either.

*Note3*: 3 of the 4 Python files in module-noaa-stations are auto-generated.
The only file written by hand contains 33 code lines (and some comments).

## Feature comparisons

| Feature description             | Zimagi module | Command-line tool 
|---------------------------------|---------------|------------------
| Exposes all source data columns | No[3]         | Yes
| Download by year range          | Partial[1]    | Yes
| Download by station list        | Partial[1]    | Yes
| Download of all stations        | No[2]         | Yes
| Flexible querying of local DB   | Yes           | Yes
| RESTful API to access local DB  | Yes           | No
| Missing data cleaned            | Partial       | Yes
| Performs good normalization     | Yes           | No[4]
| Provisions for cloud deployment | Yes           | No[5]
| Supports "pretty" output        | Yes           | Yes
| Supports CSV export             | ???           | Yes
| Supports TSV export             | ???           | Yes
| Supports JSON export            | ???           | Yes


[1] Only a `test` import subcommand defined currently, but data model 
supports parameters for min year, max year, and station list.

[2] Logic for obtaining station list within year currently stubbed out
but should follow identical logic to that used in command-line tool.

[3] Data definitions could be created for columns not currently utilized.
My estimate is that it would require about 150 additional lines of YAML
and maybe 20 lines of Python.

[4] The current command-line tool simply uses the same table structure
as the source CSV files.  Adding a child talbe with foreign key would 
require about 6 extra lines of Python, and 8 extra lines of SQL (which
is currently defined as a Python string rather than separate file).

[5] No current code knows about any clouds, but the code that would need
to be distributed to one is very minimal. 


