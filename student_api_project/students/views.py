from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET','POST'])
def student_list(request):
    if request.method == "GET":
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"student created"
            })
        else:
            return Response(serializer.errors)
        
        
@api_view(['PUT','PATCH',"DELETE"])
def student_detail(request,id):

    student=Student.objects.get(id=id)

    if request.method == 'PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"student fully updated"
            })
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PATCH':
        serializer=StudentSerializer(student,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Student Partially Updated"
            })
        else:
            return Response(serializer.errors)
    
    elif request.method=="DELETE":
        student.delete()
        return Response({
                "message":"Student Delete Successfully"
            })
        
        



    
    