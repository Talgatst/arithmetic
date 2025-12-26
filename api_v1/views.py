import json
from django.http import JsonResponse
from django.http import HttpStatus
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET requests are allowed')


def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        A = data.get('A')
        B = data.get('B')

        if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
            return JsonResponse(
                {"error": "Введите цифры."},
                status=HttpStatus.BAD_REQUEST
            )

        answer = A + B
        return JsonResponse({"answer": answer})


def subtract(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        A = data.get('A')
        B = data.get('B')

        if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
            return JsonResponse(
                {"error": "Введите цифры."},
                status=HttpStatus.BAD_REQUEST
            )

        answer = A - B
        return JsonResponse({"answer": answer})


def multiply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        A = data.get('A')
        B = data.get('B')

        if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
            return JsonResponse(
                {"error": "Введите цифры."},
                status=HttpStatus.BAD_REQUEST
            )

        answer = A * B
        return JsonResponse({"answer": answer})


def divide(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        A = data.get('A')
        B = data.get('B')

        if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
            return JsonResponse(
                {"error": "Введите цифры."},
                status=HttpStatus.BAD_REQUEST
            )

        if B == 0:
            return JsonResponse(
                {"error": "Нельзя делить на ноль."},
                status=HttpStatus.BAD_REQUEST
            )

        answer = A / B
        return JsonResponse({"answer": answer})