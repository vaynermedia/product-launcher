from sugar.views.decorators import render_to


@render_to('rocket/home.html')
def home(request):
    return {}
