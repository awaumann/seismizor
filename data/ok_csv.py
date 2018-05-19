"""
Author: Alejandro Waumann
Date: 05.19.2018

Description: Takes in the plain text (.asc) file in the project's
data/asc folder and puts the relevant data points from OK in a csv
file.
"""
import sys

def main( argc, argv ):
    '''
    '''
    # determine the root filename
    earthquake_type = 'induced'
    if argc == 2:
        earthquake_type = argv[1]

    # generate input/output filenames
    asc = 'asc/' + earthquake_type + '.asc'
    csv = 'csv/' + earthquake_type + '.csv'

    asc_file = open( asc, 'r' )
    csv_file = open( csv, 'w' )

    csv_file.write( 'Magnitude, Longitude, Latitude, Depth, Year, Month, Day, Error\n' )
    rows = asc_file.readlines()
    for row in rows:
        data = row.split()
        # only add to dataset if coordinates are inside of OK
        lng = float( data[1] )
        lat = float( data[2] )
        if lng >= -99.990018 and lng <= -94.622067 and lat >= 33.692826 and lat <= 36.996495 or \
           lng >= -102.986504 and lng <= -99.990018 and lat >= 36.526683 and lat <= 36.979498:
            for idx, datum in enumerate( data ):
                if idx < 7:
                    csv_file.write( datum + ', ' )
                elif idx == 10:
                    csv_file.write( datum + '\n' )

    asc_file.close()
    csv_file.close()

if __name__ == '__main__':
    main( len(sys.argv), sys.argv )
