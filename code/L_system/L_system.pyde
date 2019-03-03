def setup():
    axiom = 'X'
    rules = {'X':'F+[[X]-X]-F[-FX]+X','F':'FF'}
    
    global genstring
    genstring = axiom
    for i in range(6):
        newstring = []
        for c in genstring:
            newstring.append(rules.get(c,c))
        genstring = ''.join(newstring)
    
    print len(genstring)
    
    size(400,400)
    writeXML()

def draw():
    background(255)
    translate(width/2,height)
    rotate(PI)
    
    for c in genstring:
        if c == 'F':
            line(0,0,0,2.3)
            translate(0,2.3)
        elif c == '+':
            rotate(-0.4)
        elif c == '-':
            rotate(+0.4)
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()
        else:
            continue

def writeXML():
    out = createWriter('plant.svg')
    
    out.println('<?xml version="1.0" encoding="utf-8"?>')
    out.println('<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"')
    out.println('xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"')
    out.println('viewBox="0 0 400 400" style="enable-background:new 0 0 400 400;" xml:space="preserve">')
    out.println('<style type="text/css">')
    out.println('  .st0{fill:none;stroke:#000000;stroke-linecap:round;stroke-miterlimit:10;}')
    out.println('</style>')
    out.println('<g>')
    
    translate(width/2,height)
    rotate(PI)
    for c in genstring:
        if c == 'F':
            x1 = screenX(0,0)
            y1 = screenY(0,0)
            translate(0,2.3)
            x2 = screenX(0,0)
            y2 = screenY(0,0)
            out.println(linestring(x1,y1,x2,y2))
        elif c == '+':
            rotate(-0.4)
        elif c == '-':
            rotate(+0.4)
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()
        else:
            continue
    #out.println(linestring(2,3,4,5))
    
    out.println('</g>')
    out.println('</svg>')
    
    out.flush()
    out.close()
    
def linestring(a,b,c,d):
    out = '<line class="st0" x1="%f" y1="%f" x2="%f" y2="%f"/>' % (a,b,c,d)
    return out
