from django.http import HttpResponseForbidden
import time
class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the incoming request
        print(f"[middleware] Request Method: {request.method}, Path: {request.path}")
        
        response = self.get_response(request)
        # process after view is called

        print(f"[middleware] Response Status Code: {response.status_code}")
        
        return response
    



class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        start_time = time.time()
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        print(f"[TimerMiddleware] Request processing time: {duration:.2f} seconds")
        
        return response
    




class BlockIPMiddleware:
    blocked_ips = ['127.0.0.2']  # Example blocked IP
    def __init__(self, get_response):
        
        self.get_response = get_response
        
    
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.blocked_ips:
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)