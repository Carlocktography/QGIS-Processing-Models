from qgis.core import *
from qgis.gui import *
import mz2geohash

@qgsfunction(args='auto', group='Custom')
def geohash32(value1,feature,parent):
    ft_tup = ()
    ft_centroid = centroid($geometry)
    ft_lon = x(transform(ft_centroid),layer_property(@layer_id,'crs'),'EPSG:4326'))
    ft_lat = y(transform(ft_centroid),layer_property(@layer_id,'crs'),'EPSG:4326'))
    ft_tup = (ft_lon,ft_lat)
    return mz2geohash.encode((ft_tup))
