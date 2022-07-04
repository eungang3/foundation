import json 

from django.http import JsonResponse, HttpResponse
from django.views import View 
from django.core.exceptions import ObjectDoesNotExist

from owners.models import Owner, Dog 

class OwnersView(View):
    # 신규 주인 등록
    # 요청 : http -v POST 127.0.0.1:8000/owners name='영희' email='younghee@naver.com' age=31
    def post(self, request):
        # http 요청 메시지에서 데이터 불러오기
        data = json.loads(request.body)

        # db에 데이터 저장하기
        Owner.objects.create(
            name=data['name'], 
            email=data['email'], 
            age=int(data['age']
            ))
        return JsonResponse({'message' : 'created'}, status=201)

    # 주인 리스트 반환
    # 요청 : http -v GET 127.0.0.1:8000/owners
    def get(self, request):
        # DB에서 데이터 불러오기
        owners = Owner.objects.all()
        results = []

        # 데이터 딕셔너리 형태로 저장
        for owner in owners:
            results.append({
                "name" : owner.name,
                "email" : owner.email,
                "age" : owner.age
            })

        return JsonResponse({'results' : results}, status=200)

class DogsView(View):
    # 신규 강아지 등록
    # 요청 : http -v POST 127.0.0.1:8000/dogs name='스누피' age='2' owner_id=1
    def post(self, request):
        # http 요청 메시지에서 데이터 불러오기
        data = json.loads(request.body)

        # db에 데이터 저장하기
        try:
            Dog.objects.create(
                name=data['name'], 
                age=int(data['age']),
                owner_id = int(data['owner_id'])
                )
            return JsonResponse({'message' : 'created'}, status=201)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '주인 id가 존재하지 않습니다.'}, status=422)

    # 강아지 리스트 반환
    # 요청 : http -v GET 127.0.0.1:8000/dogs
    def get(self, request):
        # DB에서 데이터 불러오기
        dogs = Dog.objects.all()
        results = []

        # 데이터 딕셔너리 형태로 저장
        for dog in dogs:
            results.append({
                "name" : dog.name,
                "age" : dog.age,
                "owner" : dog.owner.name
            })

        return JsonResponse({'results' : results}, status=200)

class DogOwnersView(View):
    # 각 주인에게 속한 강아지 리스트 반환
    # 요청 : http -v GET 127.0.0.1:8000/dogowners
    def get(self, request):
        # DB에서 데이터 불러오기
        owners = Owner.objects.all()
        results = []

        # 데이터 딕셔너리 형태로 저장
        for owner in owners:
            dogs = owner.dog_set.all()
            results.append({
                "name" : owner.name,
                "email" : owner.email,
                "age" : owner.age,
                "dogs" : [{ 'name' : dog.name, 'age': dog.age } for dog in dogs]
            })

        return JsonResponse({'results' : results}, status=200)