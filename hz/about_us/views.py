from django.shortcuts import render


def certificate(request):
    """Вывод страницы Сертификат качества"""
    return render(request, 'about_us/certificate.html')


def contract(request):
    """Вывод страницы Договор оферты"""
    return render(request, 'about_us/contract.html')


def privacy_policy(request):
    """Вывод страницы Политика конфиденциальности"""
    return render(request, 'about_us/privacy_policy.html')


