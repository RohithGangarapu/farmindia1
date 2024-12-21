from django.shortcuts import render
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# if api_key is None:
#     print("API Key not found! Check the .env file.")
# genai.configure(api_key=api_key)

# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-2.0-flash-exp",
#   generation_config=generation_config,
# )

# chat_session = model.start_chat(
#   history=[
#   ]
# )
# x=str(input())
# response = chat_session.send_message(x)

# print(response.text)
def login(request):
    return render(request,'home.html')
def home(request):
    if request.POST.get('tip')=="producer":
        return render(request,'producer.html')
    else:
        print(request.POST.get('tip'))
        return render(request,'consumer.html')
def sell(request):
    return render(request,'sell.html')
def sellfruits(request):
    return render(request,'sellfruits.html')
def sellveg(request):
    return render(request,'sellveg.html')
def sellcrop(request):
    return render(request,'sellcrops.html')
def sellinfo(request):
    return render(request,'sellinfo.html')