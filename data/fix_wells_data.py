import pandas as pd

wells = open( 'csv/wells.csv', 'r' )
f = open( 'csv/wells_fixed.csv', 'w' )

# first row for labels
f.write( 'Longitude, Latitude, Depth, Year, Jan Vol, Jan PSI, Feb Vol, Feb PSI, ' +
          'Mar Vol, Mar PSI, Apr Vol, Apr PSI, May Vol, May PSI, June Vol, June PSI, ' +
          'Jul Vol, Jul PSI, Aug Vol, Aug PSI, Sep Vol, Sep PSI, Oct Vol, Oct PSI, ' +
          'Nov Vol, Nov PSI, Dec Vol, Dec PSI\n' )

rows = wells.readlines()
for idx, row in enumerate( rows ):
    data = row.split( ',' )
    # ignore the first row (just labels)
    if idx == 0:
        continue
    # ignore rows with coordinates (0,0)
    elif data[1] == '0' or data[2] == '0':
        continue

    # process valid rows
    for idx, datum in enumerate( data ):
        # ignore 1st col (empty) and 4th col (irrelevent data)
        if idx == 0 or idx == 3 :
            continue
        # last data point already has newline
        elif idx == len( data ) - 1:
            f.write( datum )
        else:
            f.write( datum + ', ' )

wells.close()
f.close()
