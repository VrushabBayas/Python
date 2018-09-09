

def overLappingArea(R1X1Y1, R1X2Y2, R2X1Y1, R2X2Y2):
    R1x1 = R1X1Y1.get("x1")
    R2x1 = R2X1Y1.get("x1")
    R1x2 = R1X2Y2.get("x2")
    R2x2 = R2X2Y2.get("x2")
    R1y1 = R1X1Y1.get("y1")
    R2y1 = R2X1Y1.get("y1")
    R1y2 = R1X2Y2.get("y2")
    R2y2 = R2X2Y2.get("y2")

    width = min(R1x2, R2x2) - max(R1x1, R2x1)
    height = min(R1y2, R2y2) - max(R1y1, R2y1)
    # height=min()-max()
    if width <= 0 or height <= 0:
        return None
    else:
        return width*height


if __name__ == "__main__":
    print(overLappingArea({"x1": 2, "y1": 4}, {"x2": 3, "y2": 5}, {
          "x1": 2, "y1": 2}, {"x2": 3, "y2": 2}))
