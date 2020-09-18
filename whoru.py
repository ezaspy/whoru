#!/usr/bin/env python3 -tt

import argparse, os, re, sys, json, time, whois

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="+", help="File where IP addresses are stored.")
parser.add_argument("-v", "--verbose", help="Show progress", action='store_const', const=True, default=False)
args = parser.parse_args()

f, verbose = args.file, args.verbose
f, wholist = f[0], []

def main():
    if not os.path.isfile(f):
        print(" >> %s is not a valid file and cannot be processed. Please try again.\n" % (f))
    else:
        try:
            with open(f) as ff:
                for line in ff:
                    w, jsonlist = line.strip("\n")+".json", []
                    if os.path.isfile(w):
                        lasttime = re.findall(r"st_mtime\=([^\,]+)\,", str(os.stat(w)))[0]
                        lasttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(lasttime)))
                        overwrite = input("\n >> The output for '%s' already exists.\n >> It was last scanned:\n     @ %s\n >> Did you want to overwrite it?\n" % (w.split(".csv")[0], lasttime))
                        if overwrite!="n":
                            os.remove(w)
                            wholist.append(w)
                        else:
                            pass
                    else:
                        wholist.append(w)
                    if len(wholist) > 0:
                        for w in wholist:
                            if verbose:
                                print(" >> Beginnning whois for %s" % (line.strip("\n")))
                            else:
                                pass
                            jsonlist.append(whois.query(line.strip("\n")).__dict__)
                            with open(w, "a") as whoout:
                                whoout.write(re.sub(r"(\:\s\{\"[^\"]+\")", r"\1: \"\"", str(str(re.sub(r"(\S), \"(\S)", r"\1\", \"\2", re.sub(r"(\S)\": ([^\s\{])", r"\1\": \"\2", str(jsonlist).replace("'","\"")[1:-1]+"\n"))).replace("\\\"","\"").replace("\"\"\"\"","\"\"").replace("\\r",""))).replace("\\\"\\\"","\"\""))
                            if verbose:
                                print(" >> whois completed for %s\n" % (line.strip("\n")))
                                time.sleep(0.5)
                            else:
                                pass
                    else:
                        print(" >> No files were selected for processing.\n")
        except IOError:
            print(" >> %s is not accessible and cannot be processed. Please try again.\n" % (f))

if __name__ == '__main__':
	main()
