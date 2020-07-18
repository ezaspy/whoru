#!/usr/bin/env python -tt

import argparse, os, re, sys, subprocess, time

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="+", help="File where IP addresses are stored.")
args = parser.parse_args()
f = args.file
f, wholist = f[0], []

def main():
    if not os.path.isfile(f):
        print(" >> %s is not a valid file and cannot be processed. Please try again.\n" % (f))
    else:
        try:
            with open(f) as ff:
                for line in ff:
                    w = line.strip("\n")+".csv"
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
                            print(" >> Beginnning whois for %s" % (line.strip("\n")))
                            dowho = subprocess.Popen(["whois", line.strip("\n")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            whoout, _ = dowho.communicate()
                            whoout = str(whoout)[4:-5].split("\\n")
                            for each in whoout:
                                title = re.findall(r"^([^\:]+)\:([^\:]+$)", each)
                                if len(title)!=0:
                                    if title[0][0]=="inetsum" or title[0][0]=="status" or title[0][0]=="changed" or title[0][0]=="NetRange" or title[0][0]=="CIDR" or title[0][0]=="NetType" or title[0][0]=="Organization" or title[0][0]=="RegDate" or title[0][0]=="Updated" or title[0][0]=="OrgName" or title[0][0]=="Address" or title[0][0]=="City" or title[0][0]=="StateProv" or title[0][0]=="Country":
                                        result = str(title[0][0])+","+str(title[0][1]).strip().replace(",",";")+"\n"
                                        with open(w, "a") as fw:
                                            fw.write(result)
                            time.sleep(1)
                            print(" >> whois lookup completed for %s\n" % (line))
                    else:
                        print(" >> No files were selected for processing.\n")
        except IOError:
            print(" >> %s is not accessible and cannot be processed. Please try again.\n" % (f))

if __name__ == '__main__':
	main()
