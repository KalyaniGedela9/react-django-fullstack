import json
 
from django.http import JsonResponse
 
from django.views.decorators.csrf import csrf_exempt
 
from .models import Role, AppUser
 
 
# GET ALL ROLES
 
def get_roles(request):
 
    roles = Role.objects.all()
 
    data = []
 
    for role in roles:
 
        data.append({
 
            'id': role.id,
 
            'role_type': role.role_type,
 
            'description': role.description
 
        })
 
    return JsonResponse(data, safe=False)
 
 
# CREATE USER
 
 
@csrf_exempt
 
def create_user(request):
 
    if request.method == 'POST':
 
        body = json.loads(request.body)
 
        email = body.get('email')
 
        first_name = body.get('first_name')
 
        last_name = body.get('last_name')
 
        empid = body.get('empid')
 
        role_id = body.get('role_id')
 
        supervisor_email = body.get('supervisor_email')
 
 
        # ROLE VALIDATION
 
        try:
 
            role = Role.objects.get(id=role_id)
 
        except Role.DoesNotExist:
 
            return JsonResponse({
 
                'error': 'Invalid role'
 
            }, status=400)
 
 
        supervisor = None
 
 
        # OWNER SHOULD NOT HAVE SUPERVISOR
 
        if role.role_type != 'owner':
 
            if not supervisor_email:
 
                return JsonResponse({
 
                    'error': 'Supervisor email required'
 
                }, status=400)
 
            try:
 
                supervisor = AppUser.objects.get(
 
                    email=supervisor_email
 
                )
 
            except AppUser.DoesNotExist:
 
                return JsonResponse({
 
                    'error': 'Supervisor email not found'
 
                }, status=400)
 
 
        # CREATE USER
 
        user = AppUser.objects.create(
 
            email=email,
 
            first_name=first_name,
 
            last_name=last_name,
 
            empid=empid,
 
            role=role,
 
            supervisor=supervisor
 
        )
 
 
        return JsonResponse({
 
            'message': 'User created successfully',
 
            'user_id': user.id
 
        })
 
# GET USERS
 
def get_users(request):
 
    users = AppUser.objects.select_related(
 
        'role',
 
        'supervisor'
 
    ).all()
 
    data = []
 
    for user in users:
 
        data.append({
 
            'id': user.id,
 
            'email': user.email,
 
            'first_name': user.first_name,
 
            'last_name': user.last_name,
 
            'empid': user.empid,
 
            'role': {
 
                'id': user.role.id,
 
                'role_type': user.role.role_type
 
            },
 
            'supervisor': (
 
                {
 
                    'id': user.supervisor.role.id,
 
                    'email': user.supervisor.email
 
                }
 
                if user.supervisor else None
 
            )
 
        })
 
    return JsonResponse(data, safe=False)
 
 