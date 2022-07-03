from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""属性text是一个CharField——由字符或文本组成的数据
（见❶）。需要存储少量的文本，如名称、标题或城市时，
可使用CharField。定义CharField属性时，
必须告诉Django该在数据库中预留多少空间。在这里，
我们将max_length设置成了200（即200个字符），
这对存储大多数主题名来说足够了。
属性date_added是一个DateTimeField——记录日期
和时间的数据（见❷）。我们传递了实参auto_now_add=True，
每当用户创建新主题时，这都让Django将这个属性自动设置成
当前日期和时间。"""
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


"""像Topic一样，Entry也继承了Django基类Model（见❶）
。第一个属性topic是一个ForeignKey实例（见❷）。
外键是一个数据库术语，它引用了数据库中的另一条记录；
这些代码将每个条目关联到特定的主题。每个主题创建时，
都给它分配了一个键（或ID）。需要在两项数据之间建立联系时，
Django使用与每项信息相关联的键。稍后我们将根据这些联系获
取与特定主题相关联的所有条目。接下来是属性text，它是一个
TextField实例（见❸）。这种字段不需要长度限制，因为我们不
想限制条目的长度。属性date_added让我们能够按创建顺序呈现条目
，并在每个条目旁边放置时间戳。在❹处，我们在Entry类中嵌套了
Meta类。Meta存储用于管理模型的额外信息，在这里，它让我们能
够设置一个特殊属性，让Django在需要时使用Entries来表示多个
条目。如果没有这个类， Django将使用Entrys来表示多个条目。
最后，方法__str__()告诉Django，呈现条目时应显示哪些信息。
由于条目包含的文本可能很长，（见❺）。我们还添加了一个省略"""
class Entry(models.Model):
    """学到的有关某个主题的具体知识
    老版本钟on_delete=models.CASCADE是默认设置
    """
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) >= 50:
            return self.text[:50]+'...'
        else:
            return self.text
