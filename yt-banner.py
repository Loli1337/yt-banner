from requests import get
from re import search
from sys import argv
open('channels4_banner.png', 'wb').write(get(search('https://yt3.ggpht.com/[^=]+=w2560', get(argv[1]).text).group()).content)