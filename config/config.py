#!/usr/bin/python
# -*- coding: utf-8 -*-
temp_config = {
    "id": "hive.db.tbl.column.func_type",  # 唯一值  格式为 数据源类型.库.表.列.类型
    "desc": "",
    "dbtype": "hive",  # hive mysql  sqlserver
    "connection": {
        "mongodb": {
            "connection": "",
            "db": ""
        },
        "mysql": {
            "host": "",
            "port": "",
            "user": "",
            "password": "",
            "db": ""
        }
    },
    "sql": "select count(1) as cnt  from yy_table",
    "checktype": "month_fluctuation", # month_fluctuation(月波动) week_fluctuation(周波动) day_fluctuation(天波动) fixed_value(固定值)
    "comparevalue": 30,
    "comparetype": "=",  # 只有checktype是FIXED_VALUE时才有意义   =(等于) >(大于) <(小于) >=(大于等于)  <=(小于等于) <>(不等于)
    "create_time": "2021-08-04 12:00:00"
}

sys_config = {
    "connection": {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "qualitis",
    }
}
