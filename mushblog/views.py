from django.shortcuts import render, get_object_or_404
from .models import Mushblog


def home(request):
    mushblogs = Mushblog.objects  # 쿼리셋이라고함
    return render(request, 'home.html', {'mushblogs': mushblogs})


# 퀴리섹과 메소드의 형식
# 모델.쿼리셋(objects).method

def detail(request, mushblog_id):
    mushblog_detail = get_object_or_404(Mushblog, pk=mushblog_id)

    return render(request, 'detail.html', {'mushblog': mushblog_detail})
