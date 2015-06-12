from artworks.models import *
from django.shortcuts import render_to_response

def main(request):
    random_artwork = Artwork.objects.all().order_by('?')[0]

    context = {
        'random_artwork' : random_artwork,
    }

    return render_to_response(
        'index.html',
        context,
    )

def about(request):
    return render_to_response('about.html')
