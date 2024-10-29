from django.db import models


# 迁移脚本,
# python manage.py makemigrations
# 同步到数据库
# python manage.py migrate
class SysUser(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    createTime = models.DateTimeField(auto_now_add=True, db_column="create_time")  # 字段，审计，添加时间

    class Meta:
        db_table = 'sys_user'  # 将表名设置为您期望的名称

    # def __str__(self):
    #
    #     return f"SysUser(id={self.id}, name={self.name})"
