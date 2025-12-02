import ezdxf
import matplotlib.pyplot as plt
import os
import numpy as np

# Load DXF
files = os.path.join('challenge_material\\10991360', "Geo (26).DXF")

doc = ezdxf.readfile(files)
msp = doc.modelspace()


def show_straight_edges():
    xs = []
    ys = []

    edges = []

    # Extract vertices & edges
    for entity in msp:
        if entity.dxftype() == "LINE":
            x1, y1, *_ = entity.dxf.start
            x2, y2, *_ = entity.dxf.end

            xs.extend([x1, x2])
            ys.extend([y1, y2])
            edges.append(((x1, y1), (x2, y2)))

        elif entity.dxftype() in ["LWPOLYLINE", "POLYLINE"]:
            points = [p[:2] for p in entity.get_points()]  # (x,y) pairs
            for i in range(len(points) - 1):
                edges.append((points[i], points[i+1]))
                xs.append(points[i][0])
                ys.append(points[i][1])
            # Close polyline if needed
            if entity.closed:
                edges.append((points[-1], points[0]))

    # Visualization
    plt.figure(figsize=(6, 6))
    for (x1, y1), (x2, y2) in edges:
        plt.plot([x1, x2], [y1, y2])

    # Scatter vertices
    plt.scatter(xs, ys, s=10)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Straight Edges and Vertices")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def show_curved_edges():
    curve_points = []   # list of point sequences (for plotting curves)
    vertices = []       # all sampled points for scatter


    def sample_arc(entity, n=100):
        center = np.array(entity.dxf.center)
        r = entity.dxf.radius
        start = np.radians(entity.dxf.start_angle)
        end   = np.radians(entity.dxf.end_angle)

        theta = np.linspace(start, end, n)
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        return np.column_stack((x, y))


    def sample_circle(entity, n=200):
        center = np.array(entity.dxf.center)
        r = entity.dxf.radius

        theta = np.linspace(0, 2*np.pi, n)
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        return np.column_stack((x, y))


    def sample_spline(entity, n=200):
        try:
            pts = entity.approximate(n)
            return np.array(pts)
        except:
            return None



    # from dxf files
    for entity in msp:

        if entity.dxftype() == "ARC":
            pts = sample_arc(entity)
            curve_points.append(pts)
            vertices.extend(pts.tolist())

        elif entity.dxftype() == "CIRCLE":
            pts = sample_circle(entity)
            curve_points.append(pts)
            vertices.extend(pts.tolist())

        elif entity.dxftype() == "SPLINE":
            pts = sample_spline(entity)
            if pts is not None:
                curve_points.append(pts)
                vertices.extend(pts.tolist())

    #plotting
    plt.figure(figsize=(6, 6))

    # Plot curves
    for pts in curve_points:
        plt.plot(pts[:, 0], pts[:, 1], linewidth=1.2)

    # Plot vertices
    if vertices:
        v = np.array(vertices)
        plt.scatter(v[:, 0], v[:, 1], s=10)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Curved Edges with Vertices")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

show_curved_edges()
