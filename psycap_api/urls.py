from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeePsyCapViewSet
from django.contrib.auth.models import User

# --- كود الإنشاء القسري للمدير (Superuser) ---
try:
    # البيانات الجديدة لضمان الدخول
    username = "shalee_khalil"
    password = "shalee_password_2026"
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, 'shalee@example.com', password)
        print(f"✅ تم إنشاء المستخدم {username} بنجاح!")
    else:
        # تحديث الباسورد في كل مرة لضمان عدم نسيانه أو تعارضه مع القاعدة القديمة
        u = User.objects.get(username=username)
        u.set_password(password)
        u.save()
        print(f"✅ تم تحديث بيانات {username}")
except Exception as e:
    print(f"⚠️ تنبيه: {e}")
# --------------------------------------------

router = DefaultRouter()
router.register(r'employees', EmployeePsyCapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]