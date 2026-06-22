from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            groups=None
            groups=request.user.groups.all()
            for group in groups:
                if group.name in allowed_roles:
                    return view_func(request,*args,**kwargs)
            return redirect('userpage')
        return wrapper_func
    return decorator