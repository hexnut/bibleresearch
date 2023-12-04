#!/usr/bin/python3

import os,sys

def draw_triangle(fp,rows):
    # Draw a triangle
    from PIL import Image, ImageDraw

    # Calculate canvas size based on 1000^2 = 40 rows
    cw = int((rows*1000)/40)
    canvas = (cw,cw)
    img = Image.new('RGB', (canvas[0], canvas[1]), color = (75, 100, 140))

    # Draw a triangle of circles
    d = ImageDraw.Draw(img)

    # Initialize dot size and image center
    dsize = 20
    center = (int(canvas[0]/2), int(canvas[1]/12))

    # Draw starting dot
    x1 = center[0] - (dsize/2)
    x2 = center[0] + (dsize/2)
    y1 = center[1] - (dsize/2)
    y2 = center[1] + (dsize/2)
    d.ellipse([(x1,y1), (x2,y2)], fill=(255,255,0))

    dcount = 2
    # Additional rows
    for n in range(2,rows+1):
        y1 += dsize
        y2 += dsize
        x1 = center[0] - (dsize/2) * n
        x2 = x1 + dsize
        d.ellipse([(x1,y1), (x2,y2)], fill=(255,255,0))
        dcount += 1
        # Generate the rest of the row
        for m in range(2,dcount):
            x1 += dsize
            x2 += dsize
            d.ellipse([(x1,y1), (x2,y2)], fill=(255,255,0))

    img.save("%s/%s" % (fp,"figure.png"))

if __name__ == "__main__":

    if len(sys.argv) == 2:
        T = int(sys.argv[1])
    else:
        T = 40

    base=os.path.expanduser('~') + "/Sync/Research/"
    fp = base + "images"
    draw_triangle(fp,T)

exit()
