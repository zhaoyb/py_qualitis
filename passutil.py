#!/usr/bin/python
# -*- coding: utf-8 -*-
from config.config import sys_config
from db_helper.mysql_helper import MySqlHelper


class PassUtil(object):

    def __init__(self):
        connection = sys_config['connection']
        host = connection['host']
        port = connection['port']
        user = connection['user']
        password = connection['password']
        db = connection['db']
        self.mysql = MySqlHelper(host, port, user, password, db)

    def compare(self, name, result_value, check_type, compare_type, compare_value):
        fluctuation_sql = '''
        SELECT 
            AVG(value) 
        FROM QUALITIS_RESULT 
        WHERE 
            name='%s' 
            AND  
            (create_time  BETWEEN DATE_SUB(NOW(),INTERVAL 1 %s) AND NOW())
        '''


        last_1_sql='''
          SELECT 
            value 
        FROM QUALITIS_RESULT 
        WHERE 
            name='%s' 
        order by 
            create_time desc 
        limit 1
        
        '''


        if check_type == "month_fluctuation":
            sql = fluctuation_sql % (name, 'MONTH')
            self.mysql.connect()
            avg_value = self.mysql.fetchone(sql)[0]
            self.mysql.disconnect()
            return self.more_than_fluctuation_thresholds(result_value, avg_value, compare_value)
        elif check_type == "week_fluctuation":
            sql = fluctuation_sql % (name, 'WEEK')
            self.mysql.connect()
            avg_value = self.mysql.fetchone(sql)[0]
            self.mysql.disconnect()
            return self.more_than_fluctuation_thresholds(result_value, avg_value, compare_value)
        elif check_type == "day_fluctuation":
            sql = fluctuation_sql % (name, 'DAY')
            self.mysql.connect()
            avg_value = self.mysql.fetchone(sql)[0]
            self.mysql.disconnect()
            return self.more_than_fluctuation_thresholds(result_value, avg_value, compare_value)
        elif check_type == "last1_fluctuation ":
            sql = last_1_sql % name
            self.mysql.connect()
            value = self.mysql.fetchone(sql)[0]
            self.mysql.disconnect()
            return self.more_than_fluctuation_thresholds(result_value, value, compare_value)
        elif check_type == "fixed_value":
            return self.more_than_fixed_thresholds(result_value, compare_value, compare_type)

    def save(self, name, value, time):
        sql = '''
        INSERT INTO qualitis_result (name,value,create_time) VALUES ('%s',%s,'%s') 
        ''' % (name, value, time)
        self.mysql.connect()
        self.mysql.save(sql)
        self.mysql.disconnect()

    @staticmethod
    def more_than_fluctuation_thresholds(result_value, compare_value, percentage):
        if compare_value:
            if not result_value:
                return True
            else:
                max_percentage = 1 + (percentage / 100)
                min_percentage = 1 - (percentage / 100)

                maxvalue = max_percentage * compare_value
                minvalue = min_percentage * compare_value
                return maxvalue >= result_value >= minvalue
        else:
            return False

    @staticmethod
    def more_than_fixed_thresholds(result_value, compare_value, compare_type):
        if not result_value:
            return True

        if compare_type == '=':
            return result_value == compare_value
        elif compare_type == '>':
            return result_value > compare_value
        elif compare_type == '<':
            return result_value < compare_value
        elif compare_type == '>=':
            return result_value >= compare_value
        elif compare_type == '<=':
            return result_value <= compare_value
        elif compare_type == '<>':
            return result_value != compare_value

        return False
