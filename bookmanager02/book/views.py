from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from book.models import BookInfo


def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2020-1-1',
        readcount=10
    )
    return HttpResponse("create")


def shop(request, city_id, shop_id):
    query_params = request.GET
    print(query_params)
    # order = query_params.get('order')
    # print(order)
    print(city_id, shop_id)
    return HttpResponse('小饭店')


def register(request):
    data = request.POST
    print(data)
    return HttpResponse("OK")


def json(request):
    body = request.body
    body_str = body.decode()
    print(body_str)
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse('json')


from django.http import HttpResponse, JsonResponse


def response(request):
    # response = HttpResponse("res", status=200)
    # response['name'] = 'root'
    # return response
    info = {
        'username': 'root',
        'password': 12345
    }
    info = [
        {
            'username': 'root',
            'password': 12345
        },
        {
            'username': '12345',
            'password': 12345
        }
    ]
    # response = JsonResponse(data=info, safe=False)
    # import json
    # data = json.dumps(info)
    # response = HttpResponse(data)
    # return response
    return redirect('http://www.baidu.com')


def set_cookie(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    response = HttpResponse('set_cookie')
    response.set_cookie('name', username, max_age=60*60)
    response.set_cookie('password', password)
    return response


def get_cookie(request):
    print(request.COOKIES)
    print(request.COOKIES.get('name'))
    return HttpResponse(request.COOKIES.get('name'))


def set_session(request):
    username = request.GET.get('username')
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse('set_session')


def get_session(request):
    # user_id = request.session.get('user_id')
    # username = request.session.get('username')
    user_id = request.session['user_id']
    username = request.session['username']

    # content = "{},{}".format(user_id, username)
    print(user_id, username)
    # return HttpResponse("OK")
    # return "%s,%s" % (user_id, username)
    return HttpResponse('get_session')
