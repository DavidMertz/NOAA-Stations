# Acquire and query data from NOAA weather stations

This project is developed primarily as a project to compare and contrast with 
the Zimagi module https://github.com/zimagi/module-noaa-stations.

This project will use only commonplace Python libraries, and will accomplish 
the following goals:

* Selectively pull data from the NOAA weather stations
* Perform modest data cleaning
* Store the acquired data in a local relational database
* Provide a query interface to "slice and dice" the data
* Provide exports from queries to several data formats, including CSV.
* Have code that is understandable to beginner Python developers
* Expose data queries as a RESTful JSON API
 

# Resources

Historical through current weather data, by station, is available at:

> https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/

Metadata about meaning of station data fields is at:

> https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt

Cross reference station information by identifier is (probably) at:

> https://www.ncdc.noaa.gov/homr/file/mshr_enhanced.txt.zip

Metadata about the meaning of station fields is at:

> https://www.ncdc.noaa.gov/homr/file/MSHR_Enhanced_Table.txt

General station metadata landing page:

> https://www.ncdc.noaa.gov/homr/reports

Additional 3rd-party human-readable documentation of station metadata details:

> http://www.weathergraphics.com/identifiers/master-location-identifier-database.pdf

