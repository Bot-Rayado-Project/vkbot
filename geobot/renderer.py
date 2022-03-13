from ipyleaflet import AntPath, WidgetControl, Map, Marker
from ipywidgets import IntSlider, jslink, HTML


class Route(object):
    def __init__(self, center: list, locations: list):
        self.center = tuple(center)
        self.locations = locations+[locations[0]]
        self.startendpoint = locations[0]
        self.map = Map(center=self.center, zoom=17)

    def render(self):
        start_marker = Marker(location=self.startendpoint)
        self.map.add_layer(start_marker)
        finish_marker = Marker(location=self.startendpoint)
        self.map.add_layer(finish_marker)
        marathon_path = AntPath(
            locations=[self.locations],
            dash_array=[1, 10],
            delay=1000,
            color='#9500ff',
            pulse_color='#9500ff'
        )
        self.map.add_layer(marathon_path)
        zoom_slider = IntSlider(description='Масштаб:',
                                min=16, max=17, value=17)
        jslink((zoom_slider, 'value'), (self.map, 'zoom'))
        widget_control1 = WidgetControl(
            widget=zoom_slider, position='topright')
        self.map.add_control(widget_control1)
        return self.map
