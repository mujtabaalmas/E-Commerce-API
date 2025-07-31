# # core/middleware.py (or wherever you prefer)

# import uuid

# class SessionIDMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         session_id = request.COOKIES.get('session_id')

#         if not session_id:
#             session_id = str(uuid.uuid4())
#             request.new_session_id = session_id  # mark for later use

#         request.session_id = session_id  # always available in views/serializers

#         response = self.get_response(request)

#         if hasattr(request, 'new_session_id'):
#             # Set session_id cookie if new
#             response.set_cookie('session_id', session_id, max_age=60*60*24*30)  # 30 days

#         return response
