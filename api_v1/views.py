import json
from http import HTTPStatus
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def _get_numbers(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return None, None, JsonResponse(
            {"error": "Некорректный JSON"},
            status=HTTPStatus.BAD_REQUEST
        )

    A = data.get('A')
    B = data.get('B')

    if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
        return None, None, JsonResponse(
            {"error": "Введите цифры."},
            status=HTTPStatus.BAD_REQUEST
        )

    return A, B, None


def add(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    A, B, error = _get_numbers(request)
    if error:
        return error

    return JsonResponse({"answer": A + B})


def subtract(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    A, B, error = _get_numbers(request)
    if error:
        return error

    return JsonResponse({"answer": A - B})


def multiply(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    A, B, error = _get_numbers(request)
    if error:
        return error

    return JsonResponse({"answer": A * B})


def divide(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    A, B, error = _get_numbers(request)
    if error:
        return error

    if B == 0:
        return JsonResponse(
            {"error": "Нельзя делить на ноль."},
            status=HTTPStatus.BAD_REQUEST
        )

    return JsonResponse({"answer": A / B})
