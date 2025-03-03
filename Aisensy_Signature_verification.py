# import hmac
# import hashlib
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View

# class TestWebhookSignature(View):
#     @csrf_exempt
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def create_hash(self, text, secret):
#         byte_key = bytes(secret, 'utf-8')
#         message = text
#         signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
#         return signature

#     def post(self, request):
#         try:
#             notification = request.body  # Get the raw request body
#             received_signature = request.headers.get('X-AiSensy-Signature')
#             shared_secret = "WEBHOOK_SHARED_SECRET"

#             # Provide the notification data as it is
#             generated_signature = self.create_hash(notification, shared_secret)

#             if received_signature == generated_signature:
#                 return JsonResponse({"message": "Signature Matched"}, status=200)
#             else:
#                 return JsonResponse({"message": "Signature didn't Match"}, status=500)

#         except Exception as e:
#             print(e)
#             return JsonResponse({"message": "An error occurred"}, status=500)

import hmac
import hashlib

class TestWebhookSignature:
    def create_hash(self, text, secret):
        byte_key = bytes(secret, 'utf-8')
        message = bytes(text, 'utf-8')  # Encode the notification string to bytes
        signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        return signature

    def post(self, notification, received_signature, shared_secret):
        try:
            # Provide the notification data as it is
            generated_signature = self.create_hash(notification, shared_secret)

            if received_signature == generated_signature:
                return  "Signature Matched", True
            else:
                return "Signature didn't Match", False

        except Exception as e:
            print(e)
            return {"message": "An error occurred"}, 500

# Sample inputs
notification = b"payment_id=XYZ9876&customer_email=john.doe@example.com&amount=99.99&currency=USD&status=successful"
received_signature = "a07640c10e8eebc6a8bce63120dd093fbbff8593162e85bec34d4ce4af102a80"
shared_secret = "my$ecr3tK3y"

test_instance = TestWebhookSignature()
result, status_code = test_instance.post(notification, received_signature, shared_secret)
print(result)
print(status_code)


###############################################################################################
