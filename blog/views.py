from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def new_view(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        category = request.POST.get('category', '')
        content = request.POST.get('content', '')

        if title == '' or category == '' or content == '':
            return render(request, 'new.html', {'error': '내용을 입력해주세요!'})
        else:
            article = Article()
            article.title = title
            article.category = category
            article.content = content
            article.save()

            return redirect('/new')




def category_view(request):
    return render(request, 'category.html')