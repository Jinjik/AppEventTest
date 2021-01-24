from django.http import HttpResponse, JsonResponse
from django.core.exceptions import FieldError
from django.views.generic.base import View

from .tools.parser import main
from .tools.limitoutrange import LimitOutOfRange
from .models import News


class Posts(View):

    @staticmethod
    def post(request):
        message = main()
        return HttpResponse(message)

    @staticmethod
    def get(requset):
        order = requset.GET.get('order')
        offset = int(requset.GET.get('offset')) if requset.GET.get('offset') else 0
        limit = int(requset.GET.get('limit')) if requset.GET.get('limit') else 5 + offset
        queryset = News.objects.values('id', 'title', 'url', 'created')

        try:

            if order:
                queryset = queryset.order_by(order)

            if limit > len(queryset):
                raise LimitOutOfRange('limit out of range')

            queryset = queryset.all()[offset:limit]
        except FieldError:
            return HttpResponse('Такого атрибута для order не существует')
        except AssertionError:
            return HttpResponse('Вы задали отрицательное значение атрибута для limit')
        except LimitOutOfRange:
            return HttpResponse('Вы задали большое значение атрибута для limit')

        return JsonResponse(list(queryset), safe=False)