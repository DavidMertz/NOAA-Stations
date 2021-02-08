#!/usr/bin/env python
import sys
import argparse

def main():
    desc = "Read remote NOAA data,  store in local database, and query it"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-f', '--fetch', action='store_true',
                        help="Obtain data from remote NOAA weather data")
    parser.add_argument('-q', '--query', type=str,
                        help="Query string against local RDMBS copy of remote data")
    parser.add_argument('-m', '--min-year', type=int,
                        help="Starting year for data to retrieve")
    parser.add_argument('-M', '--max-year', type=int,
                        help="Ending year for data to retrieve")
    parser.add_argument('--stations', type=str, default='ALL', nargs='+',
                        help="Space separated list of the station IDs of interest")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
