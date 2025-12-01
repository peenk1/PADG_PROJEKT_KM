import tkintermapview

def init_map(parent_frame):
    map_widget = tkintermapview.TkinterMapView(
        parent_frame,
        width=1220,
        height=450,
        corner_radius=0
    )
    map_widget.set_position(52.0, 21.0)
    map_widget.set_zoom(6)
    map_widget.grid(row=0, column=0, sticky="nsew")
    return map_widget

def add_marker(widget, lat, lon, text):
    return widget.set_marker(lat, lon, text=text)