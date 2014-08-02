import sys
from PIL import Image

header = "const byte myBitmap[] PROGMEM = {";
footer = "};";
output = "";


if len(sys.argv) < 2:
	sys.exit(0)

im = Image.open(sys.argv[1])
width, height = im.size
output_width = width;

print width, height

if not width % 8 == 0:
	output_width = (width + (8 - (width % 8)));

rawimdata = im.tostring()
imdata = []
for i in rawimdata:
	imdata.append(ord(i))
	

output = output + header + '\n'
output = output + str(width) + ', ' + str(height)
for i in range (height):
	for j in range (output_width/8):
		output = output + ', '
		if j == 0:
			output = output + '\n'
		output = output + 'B'
		for k in range (8):
			if (j*8+k+1) > width:
				output = output + '0'
			elif imdata[((i*width)+(j*8+k))*3]+imdata[((i*width)+(j*8+k))*3+1]+imdata[((i*width)+(j*8+k))*3+2] > 382:
				output = output + '0'
			else:
				output = output + '1'
output = output + '\n' + footer


outfile = open('output.txt', 'w')
outfile.write(output)
outfile.close();

print 'done'
