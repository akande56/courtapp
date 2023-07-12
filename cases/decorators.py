from django.contrib.auth.decorators import user_passes_test

def judge_required(function):
    def check_user_role(user):
        return user.is_authenticated and user.is_judge
    
    return user_passes_test(check_user_role)(function)

def chief_judge_required(function):
    def check_user_role(user):
        return user.is_authenticated and user.is_chief_judge
    
    return user_passes_test(check_user_role)(function)

def lawyer_required(function):
    def check_user_role(user):
        return user.is_authenticated and user.is_lawyer
    
    return user_passes_test(check_user_role)(function)

def clerk_required(function):
    def check_user_role(user):
        return user.is_authenticated and user.is_clerk
    
    return user_passes_test(check_user_role)(function)
