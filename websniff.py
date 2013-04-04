import urllib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="The URL of the site to be image sniffed")
args = parser.parse_args()
print args.url
# We get a file-like object at the specified url
f = urllib.urlopen(args.url);
# Read from the object and store the contents of the page in s
s = f.read()
f.close()
print s

