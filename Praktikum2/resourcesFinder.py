
import urllib.request

if __name__ == "__main__":
    contents = urllib.request.urlopen("http://vuln.box:8000").read()
    print(contents)