from django.contrib.auth.models import User

def baka(request):
    user = User.objects.filter(pk__in=[1, 2])
    habr = [x for x in user]
    print(habr)
    context = {
        'baka': habr
    }
    return context
