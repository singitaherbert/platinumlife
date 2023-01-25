from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def get_params(request):
    name = request.query_params('name')
    surname = request.query_params('surname')
    
    content = {'name':name,'surname':surname
    }
    return Response(content, status=status.HTTP_200_OK)
