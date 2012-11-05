import Image, ImageDraw, struct, sys, os


if len(sys.argv) != 3:
  print "dataviz.py for.exe bar.png"
  os._exit(1)
  
fileSize = os.path.getsize( sys.argv[1] )

width = 100
height = (fileSize/3) / width 
imageSize = ( width, height )          
im   = Image.new( 'RGB', imageSize )
draw = ImageDraw.Draw( im )

with open(sys.argv[1], "rb") as f:
    
    for y in range(height):
      for x in range(width):
        try:
          r = struct.unpack('B', f.read(1))[0]
          g = struct.unpack('B', f.read(1))[0]
          b = struct.unpack('B', f.read(1))[0]
          
          draw.point((x, y), fill=( r, g, b))

        except Exception, e:
          print 'Error: %s' % e
          break
        
          
del draw 
im.save( sys.argv[2], "PNG")


raw_input("Press Enter to continue...")