#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import json
import sys

from config.config import temp_config
from db_helper.hive_helper import hivehelper
from db_helper.mongo_helper import MongoHelper
from db_helper.mssql_helper import MsSqlHelper
from db_helper.mysql_helper import MySqlHelper
from passutil import PassUtil


def main(config):
    id = config['id']
    dbtype = config['dbtype']
    connection = config['connection']
    sql = config['sql']
    check_type = config['checktype']
    compare_value = config['comparevalue']
    compare_type = config['comparetype']
    create_time = config['create_time']

    result_value = 0
    if dbtype == 'hive':
        hive = hivehelper()
        result_value = hive.sql(sql)
        hive.stop()
    elif dbtype == 'mysql':
        host = connection['mysql']['host']
        port = connection['mysql']['port']
        user = connection['mysql']['user']
        password = connection['mysql']['password']
        db = connection['mysql']['db']

        mysql = MySqlHelper(host, port, user, password, db)
        mysql.connect()
        result_value = mysql.fetchone(sql)[0]
        mysql.disconnect()
    elif dbtype == 'sqlserver':
        host = connection['sqlserver']['host']
        user = connection['sqlserver']['user']
        password = connection['sqlserver']['password']
        db = connection['sqlserver']['db']

        mssql = MsSqlHelper(host, user, password, db)
        mssql.connect()
        result_value = mssql.fetchone(sql)[0]
        mssql.disconnect()


    print '新值：' + str(result_value)
    passutil = PassUtil()
    compare_result = passutil.compare(id, result_value, check_type, compare_type, compare_value)
    if not create_time:
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    passutil.save(id, result_value, create_time)

    print '对比结果：' + str(compare_result)
    if not compare_result:
        raise ValueError('%s error' % id)


if __name__ == '__main__':
    # config_param = sys.argv[1]
    # config = json.loads(config_param)
    # main(config)
    main(temp_config)
