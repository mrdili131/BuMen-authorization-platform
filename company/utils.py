from django.shortcuts import redirect

def is_company(request):
    if request.user.role == 'company' or request.user.role == 'admin':
        return True
    else:
        return False