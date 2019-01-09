# graphic-builder
A Python script that automates the creation of social images for Brutal Damage's Weekly Warmahordes matches.

# Prerequisites
* Python 3.5
* ImageMagick 7.0.8-17-Q16-x64 [Download](https://imagemagick.org/download/binaries/ImageMagick-7.0.8-17-Q16-x64-dll.exe)
* Wand 0.4.5 [Documentation](http://docs.wand-py.org/en/0.4.5/index.html)

# Setup
1. Clone or download this repository.
2. Install all of the prerequisites, making sure to add the various libraries to your PATH environment variable.
3. Open your favorite command line tool (I use [Cmder](http://cmder.net/) on Windows) and have at it!  Example usage below.

# Usage
`python main.py -c1 harkevich1 -c2 haley2 -d 10/13/2018 -t 6:00PM`

Created graphics are saved into the `output/` folder of this repository.
