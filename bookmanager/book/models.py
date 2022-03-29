from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

    def __str__(self):
        return self.name

# insert into bookinfo(name,pub_date,readcount,commentcount,is_delete) values
# ('射雕英雄传','1980-5-1',12,34,0),
# ('天龙八部' ,'1986-7-24', 36,40,0),
# ('笑傲江湖','1995-12-24', 20,80,0),
# ('营山飞狐','1987-11-11',58,24,0);


class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name

# insert into peopleinfo(name, gender, book_id, description, is_delete) values
# ('郭靖',1,1,'降龙十八掌',0),
# ('黄蓉',0,1,'打狗棍法',0),
# ('黄药师',1,1,'弹指神通',0),
# ('欧阳锋',1,1,'蛤蟆功',0),
# ('梅超风',0,1,'九阴白骨爪',0),
# ('乔修',1,2,'降龙十八掌',0),
# ('段誉',1,2,'六脉神剑',0),
# ('虚竹',1,2,'天山六阳掌',0),
# ('王语嫣',0,2,'神仙姐姐',0),
# ('令狐冲',1,3,'独孤九剑',0),
# ('任盈盈',0,3,'弹琴',0),
# ('岳不群',1,3,'华山剑法',0),
# ('东方不败',0,3,'葵花宝典',0),
# ('胡斐',1,4,'胡家刀法',0),
# ('苗若兰',0,4,'黄衣',0),
# ('程灵素',0,4,'医术',0),
# ('袁紫衣',0,4,'六合拳',0);
