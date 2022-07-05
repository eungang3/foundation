import json 

from django.http import JsonResponse, HttpResponse
from django.views import View 

from movies.models import Actor, Movie, Actor_movie 

# http -v GET 127.0.0.1:8000/movies/actors
class ActorsView(View):
    def get(self, request):
        results = []
        
        # 배우 쿼리셋 생성
        actors = Actor.objects.all()

        # for문으로 배우 쿼리셋의 각 배우 오브젝트에 접근 
        for actor in actors:
            
            # 연결 테이블에서 현재 배우가 포함된 row 모두 선택
            # 영화-배우 쿼리셋 생성
            actor_movies = Actor_movie.objects.filter(actor=actor)
            starred_in = []

            # for문으로 영화-배우 쿼리셋의 각 영화-배우 오브젝트에 접근
            for actor_movie in actor_movies:
                # 현재 영화-배우 오브젝트와 연결된 영화 오브젝트 생성
                movie = actor_movie.movie.title
                # 생성한 영화 오브젝트를 starred_in 리스트에 추가
                starred_in.append(movie)

            results.append({
                "first_name": actor.first_name,
                "last_name": actor.last_name,
                "date_of_birth" : actor.date_of_birth,
                "starred_in" : starred_in
            })
        return JsonResponse({'results' : results}, status = 200)

# http -v GET 127.0.0.1:8000/movies/movies
class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actor_movies = Actor_movie.objects.filter(movie=movie)
            casts = []
            for actor_movie in actor_movies:
                last_name = actor_movie.actor.last_name
                first_name = actor_movie.actor.first_name
                casts.append(last_name + first_name)
            results.append({
                "title": movie.title,
                "release_date": movie.release_date,
                "running_time" : movie.running_time,
                "starring" : casts
            })
        return JsonResponse({'results' : results}, status = 200)

