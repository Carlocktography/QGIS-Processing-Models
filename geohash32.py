from qgis.core import *
from qgis.gui import *
import mz2geohash

@qgsfunction(args='auto', group='Custom')
def geohash32(value,feature,parent):
    ft_centroid = centroid($geometry)
    ft_lon = x(transform(ft_centroid),layer_property(@layer_id,'crs'),'EPSG:4326'))
    ft_lat = y(transform(ft_centroid),layer_property(@layer_id,'crs'),'EPSG:4326'))
    ft_array = []
    ft_array.append(ft_lon)
    ft_array.append(ft_lat)
    geohash32 = mz2geohash.encode
    return geohash32(ft_array)
