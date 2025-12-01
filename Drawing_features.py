import ezdxf
import os

script_dir = os.path.dirname(__file__)
rel_path = "challenge_material/10991360"


def number_vertices(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    vertices = set()

    for e in msp:
        etype = e.dxftype()

        # Closed 2D polyline
        if etype == "LWPOLYLINE" and e.closed:
            vertices.add(e.vertices)

        # Open 2D polyline
        elif etype == "LWPOLYLINE" and not e.closed:
            vertices.add(e.vertices)

        # Old-style 3D polyline (2D projection)
        elif etype == "POLYLINE":
            vertices.add(e.vertices)

        # Circle
        elif etype == "CIRCLE":
            vertices.add(e.vertices)

        # Line
        elif etype == "LINE":
            try:
                vertices.add(e.vertices)
            except:
                print("LINE couldnt find vertex")
    print(vertices)



def load_dxf_geometry(file_path):
    """Extract 2D geometry from DXF file into Shapely objects."""
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    polygons = []
    lines = []

    for e in msp:
        etype = e.dxftype()

        # Closed 2D polyline
        if etype == "LWPOLYLINE" and e.closed:
            points = [(p[0], p[1]) for p in e.get_points()]
            polygons.append(Polygon(points))

        # Open 2D polyline
        elif etype == "LWPOLYLINE" and not e.closed:
            points = [(p[0], p[1]) for p in e.get_points()]
            lines.append(LineString(points))

        # Old-style 3D polyline (2D projection)
        elif etype == "POLYLINE":
            points = [(v.dxf.x, v.dxf.y) for v in e.vertices]
            if e.is_closed:
                polygons.append(Polygon(points))
            else:
                lines.append(LineString(points))

        # Circle
        elif etype == "CIRCLE":
            c = e.dxf.center
            r = e.dxf.radius
            circle = Point(c[0], c[1]).buffer(r, resolution=64)
            polygons.append(circle)

        # Line
        elif etype == "LINE":
            s, t = e.dxf.start, e.dxf.end
            lines.append(LineString([(s[0], s[1]), (t[0], t[1])]))

    return polygons, lines



number_vertices("C:/Users/adity/PycharmProjects/DS4ME/challenge_material/10991360/Geo (7).DXF")