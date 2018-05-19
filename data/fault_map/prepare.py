import geopandas as gpd

fp = 'Comprehensive.shp'

data = gpd.read_file( fp )

print( data.head() )

geometry = data['geometry']

for coord in geometry:
    print( coord )
