import json 

from django.http import JsonResponse, HttpResponse
from django.views import View 

from movies.models import Actor, Movie 

class ActorsView(View):
    # http -v GET 127.0.0.1:8000/movies/actors
    def get(self, request):
        results = []
        
        # 배우 쿼리셋 생성
        actors = Actor.objects.all()

        # for문으로 배우 쿼리셋의 각 배우 오브젝트에 접근 
        for actor in actors:
            results.append({
                "first_name": actor.first_name,
                "last_name": actor.last_name,
                "date_of_birth" : actor.date_of_birth,
                # 현재 배우와 연결된 영화 쿼리셋 생성
                # for문으로 영화 쿼리셋의 각 영화 오브젝트에 접근
                "starred_in" : [movie.title for movie in actor.movie_set.all()]
            })
        return JsonResponse({'results' : results}, status = 200)

    '''
    # http -v POST 127.0.0.1:8000/movies/actors
    def post(self, request):
        Actor.objects.bulk_create([
            Actor(first_name='봄', last_name='김', date_of_birth='1990-01-10'),
            Actor(first_name='여름', last_name='이', date_of_birth='1982-07-08'),
            Actor(first_name='가을', last_name='송', date_of_birth='1970-11-11'),
            Actor(first_name='겨울', last_name='최', date_of_birth='1960-12-25'),
            Actor(first_name='계절', last_name='사', date_of_birth='2000-05-05'),
        ])
      
        m1 = Movie.objects.get(id=1)
        m2 = Movie.objects.get(id=2)
        m3 = Movie.objects.get(id=3)
        a1 = Actor.objects.get(id=1)
        a2 = Actor.objects.get(id=2)
        a3 = Actor.objects.get(id=3)
        a4 = Actor.objects.get(id=4)
        a5 = Actor.objects.get(id=5)

        m1.actor.add(a1)
        m1.actor.add(a2)
        m1.actor.add(a3)
        m1.actor.add(a5)
        m2.actor.add(a1)
        m2.actor.add(a4)
        m3.actor.add(a4)
        m3.actor.add(a1)

        return JsonResponse({'result' : 'ok'})
      '''

class MoviesView(View):
    # http -v GET 127.0.0.1:8000/movies/movies
    def get(self, request):
        results = []
        movies = Movie.objects.all()
        
        for movie in movies:
            results.append({
                'title' : movie.title,
                'release_date' : movie.release_date,
                'running_time' : movie.running_time,
                'starring' : [actor.last_name + actor.first_name for actor in movie.actor.all()]
            })
        return JsonResponse({'results' : results}, status = 200)

    '''
    # http -v POST 127.0.0.1:8000/movies/movies
    def post(self, request):
        Movie.objects.bulk_create([
            Movie(title='인터스텔라', release_date='1990-01-10', running_time=90),
            Movie(title='그래비티', release_date='2009-02-09', running_time=160),
            Movie(title='너구리', release_date='2012-05-08', running_time=140),
        ])
        return JsonResponse({'result' : 'ok'})
    '''

