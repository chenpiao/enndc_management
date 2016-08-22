from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response


def new_res(request):
    user = request.user

    return render_to_response(
        'itsm/new_res.html', {
            'user': user,
        }
    )