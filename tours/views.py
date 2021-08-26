from random import sample

from django.http import Http404
from django.shortcuts import render

from . import data
from . import utils


def main_view(request):
    random_tours = [(data.tours.get(i), i) for i in sample(data.tours.keys(), 6)]
    context = {
        'departures': data.departures,
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'tours': random_tours,
    }
    return render(request, 'tours/index.html', context)


def departure_view(request, departure):
    tours = [(data.tours.get(i), i) for i in data.tours if data.tours.get(i)['departure'] == departure]
    if tours:
        prices = [tour[0]['price'] for tour in tours]
        nights = [tour[0]['nights'] for tour in tours]
        context = {
            'departures': data.departures,
            'departure': data.departures[departure][3:],
            'tours': tours,
            'tours_qty': utils.make_correct_ending(len(tours), 'tour'),
            'min_price': '{:,}'.format(min(prices)).replace(',', ' '),
            'max_price': '{:,}'.format(max(prices)).replace(',', ' '),
            'min_nights': '{:,}'.format(min(nights)).replace(',', ' '),
            'max_nights': '{:,}'.format(max(nights)).replace(',', ' '),
        }
        return render(request, 'tours/departure.html', context)
    else:
        raise Http404


def tour_view(request, tour_id):
    try:
        tour = data.tours[tour_id]
    except KeyError:
        raise Http404
    context = {
        'departures': data.departures,
        'title': tour['title'],
        'description': tour['description'],
        'departure': data.departures.get(tour['departure']),
        'picture': tour['picture'],
        'price': '{:,}'.format(tour['price']).replace(',', ' '),
        'stars': '★' * int(tour['stars']),
        'country': tour['country'],
        'nights_qty': utils.make_correct_ending(tour['nights'], 'night'),
        'date': tour['date'],
    }
    return render(request, 'tours/tour.html', context)
