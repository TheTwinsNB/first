from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from book.models import BookInfo


def index(request):
    # 查询全部
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')


from book.models import BookInfo

# 保存数据1
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
book.save()
# 保存数据2
BookInfo.objects.create(
    name='爬虫',
    pub_date='2020-1-1',
    readcount=11
)
# 修改数据1
book = BookInfo.objects.get(id=6)
book.name = 'pachong'
book.save()
# 修改数据2
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=666)
# 删除数据1
book = BookInfo.objects.get(id=6)
book.delete()
# 删除数据2
BookInfo.objects.filter(id=5).delete()

from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))

from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
