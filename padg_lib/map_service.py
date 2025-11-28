import tkintermapview

def init_map(parent_frame):
    map_widget = tkintermapview.TkinterMapView(
        parent_frame,
        width=1920,
        height=700,
        corner_radius=0
    )
    map_widget.set_position(52.0, 21.0)
    map_widget.set_zoom(6)
    map_widget.grid(row=0, column=0, sticky="nsew")
    return map_widget