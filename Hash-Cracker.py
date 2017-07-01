#########################################
#	This tool was created By;	#
#		ZeR0Day			#
#########################################

#!/usr/bin/python
import StringIO
import getopt
import hashlib
import sys
import os
import time

print "  "
print "Welcome To Pass Crack"
print "Created By ZeR0Day"
print "Version 0.1 Stable"


def info():
  print " "
  print "Information:"
  print "[*] Options:"
  print "[*](-h) Hash"
  print "[*](-t) Type [See supported hashes]"
  print "[*](-w) Wordlist"
  print "[*](-n) Numbers bruteforce"
  print "[*](-v) Verbose [{WARNING}Slows cracking down!]\n"
  print "[*] Examples:"
  print "[>] ./Hash-Crack.py -h <hash> -t md5 -w DICT.txt"
  print "[>] ./Hash-Crack.py -h <hash> -t sha384 -n -v"
  print "[*] Supported Hashes:"
  print "[>] md5, sha1, sha224, sha256, sha384, sha512"
  

def checkOS():
    if os.name == "nt":
        operatingSystem = "Windows"
    elif os.name == "posix":
        operatingSystem = "posix"
    else:
        operatingSystem = "Unknown"
    return operatingSystem


class hashCracking:
  
  def hashCrackWordlist(self, userHash, hashType, wordlist, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % hashType
       exit()
    with open(wordlist, "rU") as infile:
      for line in infile:
        line = line.strip()
        lineHash = h(line).hexdigest()
        if (verbose == True):
            sys.stdout.write('\r' + str(line) + ' ' * 20)
            sys.stdout.flush()
        if (lineHash == userHash.lower()):
            end = time.time()
            print "\n[+]Hash is: %s" % line
            print "[*]Words tried: %s" % self.lineCount
            print "[*]Time: %s seconds" % round((end-start), 2)
            exit()
        else:
            self.lineCount = self.lineCount + 1
    end = time.time()
    print "\n[-]Cracking Failed"
    print "[*]Reached end of wordlist"
    print "[*]Words tried: %s" % self.lineCount
    print "[*]Time: %s seconds" % round((end-start), 2)
    exit()

  def hashCrackNumberBruteforce(self, userHash, hashType, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % hashType
       exit()
    while True:
       line = "%s" % self.lineCount
       line.strip()
       numberHash = h(line).hexdigest().strip()
       if (verbose == True):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (numberHash.strip() == userHash.strip().lower()):
           end = time.time()
           print "\n[+]Hash is: %s" % lineCount
           print "[*]Time: %s seconds" % round((end-start), 2)
           break
       else:
         self.lineCount = self.lineCount + 1

def main(argv):
  hashType = userHash = wordlist = verbose = numbersBruteforce = None
  print "\n" 
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      print '[*]Type ./Hash-Cracker.py -i for information'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--type"):
          hashType = arg
      elif opt in ("-h", "--hash"):
          userHash = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      elif opt in ("-v", "--verbose"):
          verbose = True
      elif opt in ("-n", "--numbers"):
          numbersBruteforce = True
  if not (hashType and userHash):
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      sys.exit()
  print "[*]Hash: %s" % userHash
  print "[*]Hash type: %s" % hashType
  print "[*]Wordlist: %s" % wordlist
  print "[+]Please wait while we crack with hash"
  try:
      h = hashCracking()
      if (numbersBruteforce == True):
         h.hashCrackNumberBruteforce(userHash, hashType, verbose)
      else:
         h.hashCrackWordlist(userHash, hashType, wordlist, verbose)

  except IndexError:
        print "\n[-]Hash not cracked:"
        print "[*]Reached end of wordlist"
        print "[*]Try another wordlist"
        print "[*]Words tried: %s" % h.lineCount
        
  except KeyboardInterrupt:
        print "\n[Exiting...]"
        print "Words tried: %s" % h.lineCount
        
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
        
if __name__ == "__main__":
    main(sys.argv[1:])
