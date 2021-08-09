qualitis

Python版的数据质量管理
支持对hive、 sql server、mysql数据源进行检查。
检测方式，包括月平均，周平均， 日平均，固定值。


参考了(Qualitis)https://github.com/WeBankFinTech/Qualitis<br/>
做了一个简易版的。



第一步：
新建数据库：qualitis

第二步
新建表：
``` sql
DROP TABLE IF EXISTS `qualitis_result`;
CREATE TABLE `qualitis_result`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '',
  `value` double NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `name_createtime`(`name`, `create_time`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
```

第三步：
```shell
sh run.sh
```
