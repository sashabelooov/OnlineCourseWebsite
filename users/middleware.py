# from django.shortcuts import redirect
# from django.urls import reverse

# class ProfileCompletionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)

#         # Faqat autentifikatsiya qilingan va superuser bo'lmagan userlar
#         if request.user.is_authenticated and not request.user.is_superuser:
#             # Foydalanuvchi to‘liq bo‘lmagan malumotlarini tekshirish
#             need_update = (
#                 not request.user.username or
#                 not request.user.phone or
#                 not request.user.profile_image
#             )

#             current_url = request.path
#             # Agar malumot to‘liq bo‘lmasa va hozir update sahifada bo‘lmasa, yo‘naltirish
#             if need_update and not current_url.startswith(reverse('profile_update')) and not current_url.startswith(reverse('register')):
#                 return redirect('profile_update')


#         return response
