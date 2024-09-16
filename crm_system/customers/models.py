from django.db import models
from django.utils import timezone



class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100) #学历
    
    major_category = models.CharField(max_length=50, default='IT')  # 专业分类
    major_detail = models.CharField(max_length=255)  # 具体专业

    phone_number = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=50, blank=True, null=True)
    initial_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # 第一次被创建的时间

    last_edited = models.DateTimeField(null=True, blank=True)
    edit_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 如果是更新操作，设置最后编辑时间并增加编辑次数
        if self.pk:  # 如果已经存在（非新增）
            self.last_edited = timezone.now()
            self.edit_count += 1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name