from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

@register(User)
class UserAdmin(UserAdmin):
    """ User admin """