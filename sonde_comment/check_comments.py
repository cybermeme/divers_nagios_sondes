#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 07:49:05 2021

v:2.0

@author: cybermeme
"""


#lib importation

import os
import sys
import argparse
import mysql.connector


#arguments to parse

parser = argparse.ArgumentParser()


parser.add_argument('-w', '--warn', dest='warning', type=int, required=True, 
                    help='Warning value')

parser.add_argument('-c', '--crit', dest='critical', type=int, required=True ,
                    help='Critical value')

parser.add_argument('-t', '--time', dest='time', type=int, required=True ,
                    help='duration of the search (in hour)')


args = parser.parse_args()


#Database / data to change

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="pass",
  database="wordpress"
)

mycursor = mydb.cursor()


#mycursor.execute("SELECT * FROM wp_comments")
# search for the total of comments during the last n hours (n = -t argument)
mycursor.execute("select count(*) from wp_comments where comment_date >= from_unixtime(unix_timestamp(curtime())-3600*" + str(args.time) + ")")

# extract the number of comments
nbr_comments = mycursor.fetchall()[0][0]


#Main
if nbr_comments < args.warning:
    print("OK - {} comments during the last {} hours.".format(nbr_comments, args.time))
    sys.exit(0)
elif nbr_comments < args.critical:
    print("WARNING - {} comments during the last {} hours.".format(nbr_comments, args.time))
    sys.exit(1)
elif nbr_comments >= args.critical:
    print("CRITICAL - {} comments during the last {} hours.".format(nbr_comments, args.time))
    sys.exit(2)
else:
    print("UKNOWN - No data returned")
    sys.exit(3)

