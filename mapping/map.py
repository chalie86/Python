>>> import folium
>>> dif(follium)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dif' is not defined
>>> dir(folium)
['Choropleth', 'Circle', 'CircleMarker', 'ClickForMarker', 'ColorLine', 'ColorMap', 'CssLink', 'CustomIcon', 'Div', 'DivIcon', 'Element', 'FeatureGroup', 'Figure', 'FitBounds', 'GeoJson', 'GeoJsonTooltip', 'Html', 'IFrame', 'Icon', 'JavascriptLink', 'LatLngPopup', 'LayerControl', 'LinearColormap', 'Link', 'MacroElement', 'Map', 'Marker', 'PolyLine', 'Polygon', 'Popup', 'Rectangle', 'RegularPolygonMarker', 'StepColormap', 'TileLayer', 'Tooltip', 'TopoJson', 'Vega', 'VegaLite', 'WmsTileLayer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_version', 'branca', 'features', 'folium', 'map', 'raster_layers', 'sys', 'utilities', 'vector_layers']
>>> map = folium.Map(location=[80,-100],)
>>> map
<folium.folium.Map object at 0x000001879A2C84E0>
>>> map.add_child(folium.Marker(location=[38.2,-90.1,popup="Hi A am a Marker",icon=folium.Icon(color='green')))
  File "<stdin>", line 1
    map.add_child(folium.Marker(location=[38.2,-90.1,popup="Hi A am a Marker",icon=folium.Icon(color='green')))
                                                          ^
SyntaxError: invalid syntax
>>> map.add_child(folium.Marker(location=[38.2,-90.1],popup="Hi A am a Marker",icon=folium.Icon(color='green')))
<folium.folium.Map object at 0x000001879A2C84E0>
>>> map.add_child(folium.Marker(location=[-25.819506, 28.290369],popup="Hi A am a Marker",icon=folium.Icon(color='green')))
<folium.folium.Map object at 0x000001879A2C84E0>
>>> map.save("map6.html")
>>> fg = folium.featureGroup(name="My Map")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'folium' has no attribute 'featureGroup'
>>> fg = folium.FeatureGroup(name="My Map")
>>> fig.add_child(folium.Marker(location=[-25.819506, 28.290369],popup="Hi A am a Marker",icon=folium.Icon(color='green')))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fig' is not defined
>>> fg.add_child(folium.Marker(location=[-25.819506, 28.290369],popup="Hi A am a Marker",icon=folium.Icon(color='green')))
<folium.map.FeatureGroup object at 0x000001879D6D8550>
>>> map.add_child(fg)
<folium.folium.Map object at 0x000001879A2C84E0>
>>> map.save("map7.html")