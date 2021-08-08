#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark import SparkConf, SparkContext, HiveContext, SQLContext
from pyspark.sql import HiveContext


class hivehelper(object):
    def __init__(self):
        conf = (SparkConf().set("spark.driver.maxResultSize", "4g")
                .set('spark.executor.memory', '8g')
                .set('spark.driver.memory', '1g')
                .set('spark.executor.instances', '20')
                .set('spark.sql.shuffle.partitions', 10)
                .set('spark.yarn.executor.memoryOverhead', 2000))
        self.sc = SparkContext(conf=conf)
        self.sql_context = SQLContext(self.sc)
        self.hive_context = HiveContext(self.sc)

    def sql(self, sql):
        df = self.hive_context.sql(sql)
        result = df.collect()
        value = result[0][0]
        return value

    def stop(self):
        self.sc.stop()
