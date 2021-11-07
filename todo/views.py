from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti ",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti ",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti ",

    },
    {
        'index': 3,
        'id': 4,
        'name': 'Movie-4',
        'priority': 6,
        'description': "hello iam studying at iti ",

    },
    {
        'index': 4,
        'id': 5,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti ",

    },
    {
        'index': 5,
        'id': 6,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti ",

    },
]


def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda item: item.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])

    return index_of_task


def todo_list(request):
    my_context = {'task_list': my_task_list, }
    return render(request, 'todo/todo_list.html', context=my_context)
    # return HttpResponse('Hello from list ')


def todo_update(request, **kwargs):
    task_id = kwargs.get('task_id')
    item_updated = _get_target_task(task_id)
    my_task_list[item_updated]['name'] = 'Updated {}'.format(my_task_list[item_updated].get('name'))

    return redirect('todo:todo-list')


def todo_delete(request, **kwargs):
    task_id = kwargs.get('task_id')
    item_delete = _get_target_task(task_id)
    if my_task_list:
        my_task_list.pop(item_delete)

    return redirect('todo:todo-list')


def todo_detail(request, **kwargs):
    task_id = kwargs.get('task_id')
    task_index = _get_target_task(task_id)
    my_task_detail= my_task_list[task_index]
    my_context = {
        'task_id': my_task_detail.get('id'),
        'task_name': my_task_detail.get('name'),
        'task_priority': my_task_detail.get('priority'),
        'task_description': my_task_detail.get('description')
    }

    if not request.is_ajax():
        return render(request, 'todo/todo_detail.html', context=my_context)
    else:
        return JsonResponse(kwargs)
    # return HttpResponse('You choice Task number {}'.format(kwargs))

# movies_list = [
#     {"Title":"War","Year":"2007","Rated":"R","Released":"24 Aug 2007","Runtime":"103 min","Genre":"Action, Crime, Thriller","Director":"Philip G. Atwell","Writer":"Lee Anthony Smith, Gregory J. Bradley","Actors":"Jet Li, Jason Statham, Nadine Velazquez","Plot":"An FBI Agent seeks vengeance on a mysterious assassin known as \"Rogue\" who murdered his partner.","Language":"English, Mandarin, Japanese, Cantonese","Country":"Canada, United States","Awards":"1 nomination","Poster":"https://m.media-amazon.com/images/M/MV5BNTIwMjE2Mjc1MF5BMl5BanBnXkFtZTYwNzI0OTI3._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.2/10"},{"Source":"Metacritic","Value":"36/100"}],"Metascore":"36","imdbRating":"6.2","imdbVotes":"88,795","imdbID":"tt0499556","Type":"movie","DVD":"05 Jun 2007","BoxOffice":"$22,486,409","Production":"New Glory Productions","Website":"N/A","Response":"True"}
# ]