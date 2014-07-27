Gamebuino-Bitmap-Encoder
========================

simple command line python script to encode a bitmap for use with the gamebuino. You will need PIL to use it: http://www.pythonware.com/products/pil/


###Usage

python BitmapEncoder.py \<image-to-encode\>

The image will not be scaled so make sure it's the correct size, the encoder assumes any pixels 'darker' than 50% grey are 'black' (1) and those lighter are 'white' (0). the output will be saved in the current directory in output.txt
