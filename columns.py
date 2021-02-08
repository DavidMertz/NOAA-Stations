na_values = {"TEMP": 9999.9, "DEWP": 9999.9, "SLP": 9999.9, "STP": 9999.9,
             "MAX": 9999.9, "MIN": 9999.9, "PRCP": 99.99, "SNDP": 999.99,
             "VISIB": 999.9, "WDSP": 999.9, "MXSPD": 999.9, "GUST": 999.9}

sql_create = """
CREATE TABLE IF NOT EXISTS noaa (
    STATION TEXT NOT NULL,      -- Station number (WMO/DATSAV3 possibly combined w/WBAN number).
    DATE TEXT NOT NULL,         -- mm/dd/yyyy format.
    LATITUDE REAL,              -- decimated degrees (Southern Hemisphere negative).
    LONGITUDE REAL,             -- decimated degrees (Western Hemisphere negative).
    ELEVATION REAL,             -- Given in meters.
    NAME TEXT,                  -- Name of station/airport/military base.
    TEMP REAL,                  -- Mean temp in degrees Fahrenheit to tenths.
    TEMP_ATTRIBUTES INTEGER,    -- #observations used in calculating mean temperature.
    DEWP REAL,                  -- Mean dew point for the day in degrees Fahrenheit to tenths.
    DEWP_ATTRIBUTES INTEGER,    -- #observations used in calculating mean dew point.
    SLP REAL,                   -- Mean sea level pressure for the day in millibars to tenths.
    SLP_ATTRIBUTES INTEGER,     -- #observations used in calculating mean sea level pressure.
    STP REAL,                   -- Mean station pressure for the day in millibars to tenths.
    STP_ATTRIBUTES INTEGER,     -- #observations used in calculating mean station pressure.
    VISIB REAL,                 -- Mean visibility for the day in miles to tenths.
    VISIB_ATTRIBUTES INTEGER,   -- #observations used in calculating mean visibility.
    WDSP REAL,                  -- Mean wind speed for the day in knots to tenths.
    WDSP_ATTRIBUTES INTEGER,    -- #observations used in calculating mean wind speed.
    MXSPD REAL,                 -- Max sustained wind speed for the day in knots to tenths.
    GUST REAL,                  -- Max wind gust reported for the day in knots to tenths.
    MAX REAL,                   -- Max temp reported during the day in Fahrenheit to tenths.
    MAX_ATTRIBUTES INTEGER,     -- Blank indicates taken from the explicit maximum not 'hourly'
    MIN REAL,                   -- Min temp reported during the day in Fahrenheit to tenths.
    MIN_ATTRIBUTES INTEGER,     -- Blank indicates taken from the explicit minimum not hourly
    PRCP REAL,                  -- Total precip (rain and/or melted snow) in inches.
    PRCP_ATTRIBUTES TEXT,       -- Fulll explanation in Column-Descriptions-NOAA.txt
    SNDP REAL,                  -- Snow depth in inches to tenths
    FRSHTT TEXT,                -- Full explantion in Column-Descriptions-NOAA.txt
    PRIMARY KEY (station, date)
)
"""
