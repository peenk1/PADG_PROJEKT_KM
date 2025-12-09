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

def add_restaurant_marker(widget, lat, lon, text):
    return widget.set_marker(lat, lon, text=text, marker_color_circle="red", marker_color_outside="darkred")


def add_employee_marker(widget, lat, lon, text):
    return widget.set_marker(lat, lon, text=text, marker_color_circle="blue", marker_color_outside="navy")


def add_client_marker(widget, lat, lon, text):
    return widget.set_marker(lat, lon, text=text, marker_color_circle="green", marker_color_outside="darkgreen")
