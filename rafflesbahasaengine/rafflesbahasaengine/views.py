from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .permissions import Check_API_KEY_Auth


@api_view(['POST'])
@permission_classes((Check_API_KEY_Auth, ))
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)