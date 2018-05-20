import pandas as pd

wells = open( 'asc/wells.asc', 'r' )
f = open( 'csv/wells.csv', 'w' )

# first row for labels
f.write( 'Latitude, Longitude, Depth, Year, Jan Vol, Jan PSI, Feb Vol, Feb PSI, ' +
          'Mar Vol, Mar PSI, Apr Vol, Apr PSI, May Vol, May PSI, June Vol, June PSI, ' +
          'Jul Vol, Jul PSI, Aug Vol, Aug PSI, Sep Vol, Sep PSI, Oct Vol, Oct PSI, ' +
          'Nov Vol, Nov PSI, Dec Vol, Dec PSI\n' )

rows = wells.readlines()
for idx, row in enumerate( rows ):
    data = row.split( ',' )
    # ignore the first row (just labels)
    if idx == 0:
        continue
    # ignore rows with coordinates ( , )
    elif data[0] == '' or data[1] == '':
        continue

    # process valid rows
    for idx, datum in enumerate( data ):
        # ignore 3th col (irrelevent data)
        if idx == 2 :
            continue
        # last data point already has newline
        elif idx == len( data ) - 1:
            f.write( datum )
        else:
            f.write( datum + ', ' )

wells.close()
f.close()
