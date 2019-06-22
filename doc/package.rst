Mosaic Plugin
=====================

The ``mosaic`` plugin generates a montage of a mosiac from cover art.

By default the ``mosaic`` generates a mosaic, as mosaic.png in the
current directory, of cover art out of the whole library .

You can customize the output mosaic, overlay and blend a image
as watermark and use a alternative filename as result picture :

  -h, --help            			show this help message and exit
  -r, --random                      randomize the cover art
  -m FILE, --mosaic=file    		save final mosaic picture as FILE
  -w FILE, --watermark=FILE     	add FILE for a picture to blend over mosaic
  -a ALPHA, --alpha=ALPHA       	ALPHA value for blending 0.0-1.0
  -c HEXCOLOR, --color=HEXCOLOR 	background color as HEXCOLOR
  -g GEOMETRY, --geometry=GEOMETRY  Geometry defined as
                <width>x<height>+<marginx>+<marginy>
  -f FONT, --font=FONT              URL of ttf-font

Examples
--------
Create mosaic from all Album cover art::

    $ beet mosaic

Create mosaic from band Tool with a second picture as watermark::

    $ beet mosaic -w c:/temp/tool.png -a 0.4 Tool

Create mosaic from every Album out of year 2012, use background color red::

    $ beet mosaic -b ff0000 year:2012
