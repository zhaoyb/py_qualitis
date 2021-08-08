#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymssql


class MsSqlHelper(object):

    def __init__(self, host, user, password, db):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        self.conn = pymssql.connect(self.host, self.user, self.password, self.db, charset='utf8')
        self.cursor = self.conn.cursor()

    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def disconnect(self):
        self.conn.close()
