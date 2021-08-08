#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import time
import MySQLdb


class MySqlHelper(object):

    def __init__(self, host, port, user, password, db):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db

    def connect(self):
        self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()

    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def save(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()
