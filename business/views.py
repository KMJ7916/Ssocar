from django.shortcuts import render

# Create your views here.
# 자동차 리스트
def index(request):
    cars = Car.objects.all()
    context = {
        "cars":cars
    }
    return render(request,template_name="business/index.html",context=context)

#어던 고객이 어떤 차를 빌려갔는지 표시하는 detail view
def  customer_detail(request):
    pass