from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour
    print(f'hour = {hour}')
    return render(request, 'index.html',locals())

def showpost(request, slug):
    try:
        post=Post.objects.get(slug=slug)
        if post !=None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
import random
def about(request,num=-1):
        quotes = ['今日事，今日畢',
                  '要怎麼收穫，先那麼栽',
                  '知識就是力量',
                  '一個人的個性就是他的命運']
        if num == -1 or num > 4:
            quote = random.choice(quotes)
        else:
            quote = quotes[num]
        return render(request, 'about.html', locals())

def carprice(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    car_list = [
        [{'model':'Fiesta','price': 203500},
        {'model':'Focus', 'price': 605000}, 
        {'model':'Mustang', 'price': 900000}], 
        [{'model':'FIT', 'price':450000},
        {'model':'CITY', 'price': 150000}, 
        {'model':'NSX', 'price': 1200000}],
        [{'model':'Mazda3', 'price': 329999},    
        {'model':'Mazda5', 'price': 603000},
        {'model':'Mazda6', 'price':850000}],]
    
    maker = maker
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carprice.html', locals())



'''

def homepage(request):
    posts = Post.objects.all()
    post_list = list()
    for counter, post in enumerate(posts):
        post_list.append(f'NO. {counter}-{post} <br>')
    return HttpResponse(post_list)
    
'''