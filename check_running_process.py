#!/usr/bin/python
import commands, os, string
program = raw_input("Enter the name of the program to check: ")
try:
  list
  output = commands.getoutput("ps -ef | grep " +program)
  proginfo = string.split(output)
  print "\n\
  Full path:\t\t", proginfo[7], "\n\
  Owner:\t\t", proginfo[0], "\n\
  Process ID:\t\t", proginfo[1], "\n\
  Parent process ID:\t", proginfo[2], "\n\
  Time started:\t\t", proginfo[4]
except:
 print "There was a problem with the program."
