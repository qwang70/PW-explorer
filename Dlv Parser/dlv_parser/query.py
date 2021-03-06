#!/usr/bin/env python2.7
import sys, os
from sys import argv
import AntlrDlv as dlv
import pandas as pd
import numpy as np
import inspect
import string
import argparse
import sqlite3
import errno  
import logging
FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT)

class SqlQuery:
    def __init__(self, location):
        self.location = location
        if os.path.exists(location):
            try:
                self.conn = sqlite3.connect(location)
                self.c = self.conn.cursor()
            except sqlite3.Error:
                logging.error(traceback.format_exc())
                exit()
        
        else:
            logging.error("location \"" + location + "\" doesn't exist")
            exit()
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    #Some Possible Queries:

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

    #1: Intersection

    #SQLite Version:
    def intersection_sqlite(self, relation):
        self.c.execute("SELECT * FROM META WHERE relation_name=?", (relation,))
        meta = self.c.fetchone()
        relation_name = meta[0]
        pw_num = meta[1]
        field_num = meta[2]

        # list of pws number
        pws_to_consider = [j for j in range(1, pw_num +1)]
        #"x1, x2, ..."
        col_names = ', '.join(["x"+str(i) for i in range(1, field_num+1)])
        query_intersection = ''
        for j in pws_to_consider[:-1]:
            query_intersection += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(j) + ' intersect '
        query_intersection += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(pws_to_consider[-1]) + ';'
        # run sql query with pandas
        try:
            # run with sqlite3
            #for row in self.conn.execute(command):
            #    print row
            # run with pandas
            df = pd.read_sql_query(query_intersection, self.conn)
            pd.set_option('display.max_rows', len(df))
            print(df.to_csv(index=False))
        except :
            pass
        # run sql query with sqlite3
        #self.c.execute(query_intersection)
        #print (self.c.fetchall())
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

    #2: Union

    def union_sqlite(self, relation):
        self.c.execute("SELECT * FROM META WHERE relation_name=?", (relation,))
        meta = self.c.fetchone()
        relation_name = meta[0]
        pw_num = meta[1]
        field_num = meta[2]

        # list of pws number
        pws_to_consider = [j for j in range(1, pw_num +1)]
        #"x1, x2, ..."
        col_names = ', '.join(["x"+str(i) for i in range(1, field_num+1)])
        query_union = ''
        for j in pws_to_consider[:-1]:
            query_union += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(j) + ' UNION '
        query_union += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(pws_to_consider[-1]) + ';'
        # run sql query with pandas
        try:
            # run with sqlite3
            #for row in self.conn.execute(command):
            #    print row
            # run with pandas
            df = pd.read_sql_query(query_union, self.conn)
            pd.set_option('display.max_rows', len(df))
            print(df.to_csv(index=False))
        except :
            pass
        # run sql query with sqlite3
        #self.c.execute(query_union)
        #print (self.c.fetchall())

    def displaySchema(self):
        for row in self.conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;"):
            print row[4]

    def query(self,q):
        # all SQL commands (split on ';')
        q = q.translate(None, "\r\n")
        sqlCommands = q.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            if len(command) == 0:
                continue
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                # run with sqlite3
                #for row in self.conn.execute(command):
                #    print row
                # run with pandas
                df = pd.read_sql_query(command, self.conn)
                pd.set_option('display.max_rows', len(df))
                print(df.to_csv(index=False))
            except :
                print "Command skipped: "+command

    def queryFile(self, filename):
        #TODO: decide the output format of query. pandas or tuple
        # Open and read the file as a single buffer
        if os.path.exists(filename):
            with open(filename, 'r') as fd:
                sqlFile = fd.read()
        else:
            logging.error("location \"" + filename + "\" doesn't exist")
            exit()
        self.query(sqlFile)

def handler_sql():
    # TODO only output query result
    if args.output:
        sys.stdout = open(args.o[0], 'w')
    if args.database:
        sqlQuery = SqlQuery(args.database[0])
        if args.intersection:
            sqlQuery.intersection_sqlite(args.intersection[0])
        if args.union:
            sqlQuery.union_sqlite(args.union[0])
        if args.display:
            sqlQuery.displaySchema()
        if args.file:
            sqlQuery.queryFile(args.file[0])
        if args.query:
            sqlQuery.query(args.query[0])

def handler_csv():
    if args.csv:
        pass
def argParser():
    parser = argparse.ArgumentParser(description='Possible world query explorer.')
    subparsers = parser.add_subparsers(help='sub-command help')
    #sql subparser
    parser_sql = subparsers.add_parser('sqlQuery', help='sqlQuery help')
    parser_sql.add_argument('database', nargs = 1, help='Input SQLite database location')
    parser_sql.add_argument('-d', '--display', action='store_true', help='Display Schema')
    parser_sql.add_argument('--intersection', nargs = 1, help='intersection relation name')
    parser_sql.add_argument('--union', nargs = 1, help='union relation name')
    parser_sql.add_argument('-f', '--file', nargs = 1, help='Run SQLite query from the input file')
    parser_sql.add_argument('-query', nargs = 1, help='query input')
    parser_sql.add_argument('-o', '--output', nargs = 1, help='Output file location')
    parser_sql.set_defaults(func=handler_sql)
    
    # pandas subparser
    parser_csv = subparsers.add_parser('pandasQuery', help='pandasQuery help')
    parser_csv.add_argument('csv', nargs = 1, help='Input csv file location')
    parser_csv.set_defaults(func=handler_csv)
    
    return parser
def init(arguments):
    global args
    parser = argParser()
    args = parser.parse_args(arguments)
    args.func()
if __name__ == '__main__':
    parser = argParser()
    args = parser.parse_args()
    args.func()
