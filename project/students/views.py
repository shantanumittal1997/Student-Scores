from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *

class SubjectViewSet(viewsets.ModelViewSet):

    queryset = Subject.objects.all().prefetch_related('scores')
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny,]

    def list(self, request, *args, **kwargs):
        '''
        Method to information of all the subjects stored in DB
        '''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''
        Method to get information of subject by id
        Pass pk of subject in url
        '''
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''
        Method to delete information of subject by id
        Pass pk of subject in url
        '''
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        '''
        Method to add information of subject by id
        Pass pk of subject in url
        '''
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''
        Method to update information of subject by id
        Pass pk of subject in url
        '''
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        '''
        Method to partially update information of subject by id
        Pass pk of subject in url
        '''
        return super().partial_update(request, *args, **kwargs)

class ScoreViewSet(viewsets.ModelViewSet):

    '''
    ViewSet for CRUD operations of Student scores information

    GET: /scores/ -> listing all scores
    GET: /scores/<score_object_id>/ -> get information of particular score
    POST: /scores/ -> add a new score
    PUT: /scores/<score_object_id>/ -> update information of score
    PATCH: /scores/<score_object_id>/ -> partially updating information of score
    '''

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny,]

    def list(self, request, *args, **kwargs):
        '''
        Method to information of all the student scores stored in DB
        '''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''
        Method to get information of student score by id
        Pass pk of student score in url
        '''
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''
        Method to delete information of student score by id
        Pass pk of student score in url
        '''
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        '''
        Method to add information of student score by id
        Pass pk of student score in url
        '''
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''
        Method to update information of student score by id
        Pass pk of student score in url
        '''
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        '''
        Method to partially update information of student score by id
        Pass pk of student score in url
        '''
        return super().partial_update(request, *args, **kwargs)

class StudentViewSet(viewsets.ModelViewSet):

    '''
    ViewSet for CRUD operations of Students information

    GET: /students/ -> listing all students
    GET: /students/<student_object_id>/ -> get information of particular student
    POST: /students/ -> add a new student
    PUT: /students/<student_object_id>/ -> update information of student
    PATCH: /students/<student_object_id>/ -> partially updating information of student
    '''

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny,]

    def list(self, request, *args, **kwargs):
        '''
        Method to information of all the students stored in DB
        '''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''
        Method to get information of student by id
        Pass pk of student in url
        '''
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''
        Method to delete information of student by id
        Pass pk of student in url
        '''
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        '''
        Method to add information of student by id
        Pass pk of student in url
        '''
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''
        Method to update information of student by id
        Pass pk of student in url
        '''
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        '''
        Method to partially update information of student by id
        Pass pk of student in url
        '''
        return super().partial_update(request, *args, **kwargs)