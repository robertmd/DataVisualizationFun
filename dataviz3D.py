import Image, ImageDraw, struct, sys, os


if len(sys.argv) != 3:
  print "dataviz3D.py for.exe bar.png"
  os._exit(1)
  
fileSize = os.path.getsize( sys.argv[1] )
imageLayers = 40

size = ( 256, 256 )          


with open(sys.argv[1], "rb") as f:
    x = struct.unpack('B', f.read(1))[0]
    y = struct.unpack('B', f.read(1))[0]
    
    for layer in range(imageLayers):
      im   = Image.new( 'RGB', size )
      draw = ImageDraw.Draw( im )
      for i in range((fileSize/imageLayers)):
        try:
          r, g, b = im.getpixel( (x, y) )
          
          if   r < 255:
            draw.point((x, y), fill=( r+2, g, b))
          elif g < 255:
            draw.point((x, y), fill=( r, g+2, b))
          else: 
            draw.point((x, y), fill=( r, g, b+2))
          
          x = y
          y = struct.unpack('B', f.read(1))[0]
        except Exception, e:
          break
                  
      del draw 
      im.save( str(layer) + sys.argv[2], "PNG")
      del im


raw_input("Press Enter to continue...")