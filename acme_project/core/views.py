# core/views.py
from django.shortcuts import render


def csrf_failure(request, exception):
    return render(request, 'core/403csrf.html', status=403)

def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию; 
    # выводить её в шаблон пользовательской страницы 404 мы не станем.
    return render(request, 'core/404.html', status=404)


# def csrf_failure(request, reason=""):
#     context = RequestContext(request)
#     response = render_to_response('core/403csrf.html', context)
#     response.status_code = 403
#     return response

