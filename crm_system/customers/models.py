from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)  # 学历
    
    major_category = models.CharField(max_length=50, default='IT')  # 专业分类
    major_detail = models.CharField(max_length=255)  # 具体专业

    phone_number = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=50, blank=True, null=True)

    initial_notes = models.TextField(blank=True, null=True)  # 当前笔记

    created_at = models.DateTimeField(default=timezone.now)  # 第一次被创建的时间
    last_edited = models.DateTimeField(null=True, blank=True)
    edit_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 如果是更新操作且 initial_notes 有变化，保存历史记录
        if self.pk:  # 如果已经存在（非新增）
            original = Customer.objects.get(pk=self.pk)  # 获取数据库中的原始记录
            if original.initial_notes != self.initial_notes:  # 检查 initial_notes 是否有变化
                NoteHistory.objects.create(customer=self, note_content=original.initial_notes)  # 保存旧的 initial_notes
            self.last_edited = timezone.now()  # 更新最后编辑时间
            self.edit_count += 1  # 增加编辑次数
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class NoteHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='note_history')
    note_content = models.TextField()  # 保存之前的 initial_notes 内容
    timestamp = models.DateTimeField(auto_now_add=True)  # 记录更新时间

    def __str__(self):
        return f'Note for {self.customer.name} on {self.timestamp}'