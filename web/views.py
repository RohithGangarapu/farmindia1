from django.shortcuts import render,redirect
from web.models import *
import datetime
import requests
from bs4 import BeautifulSoup
import datetime
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
def scrap():
    url = "https://vegetablemarketprice.com/market/andhrapradesh/today"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": "table"})
        if not table:
            print("Could not find the vegetable prices table.")
            return
        rows = table.find_all("tr")
        for row in rows[1:]:
            columns = row.find_all("td")
            name = columns[1].get_text(strip=True)
            price = columns[2].get_text(strip=True)
            PastPrices.objects.create(product=name,price=int(price[1:]),date=datetime.date.today())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the website: {e}")
def login(request):
    return render(request,'home.html')
def home(request):
    if 'id' not in request.session:
        return redirect('login')
    user_type = request.session.get('type')
    
    if user_type == "producer":
        return render(request, 'producer.html')
    elif user_type == "consumer":
        return render(request, 'consumer.html')
    else:
        return redirect('login')
def producer(request):
    if request.method == 'POST':
        if int(request.POST.get('type')) == 1:
            no = request.POST.get('phoneno')
            password = request.POST.get('pass')
            p = Producer.objects.filter(password=password, phone_no=no)
            if p.exists():
                producer = p.first()
                request.session['type'] = "producer"
                request.session['id'] = producer.id
                return render(request,'producer.html')
        else:
            name=request.POST.get('name')
            no = request.POST.get('phoneno')
            password = request.POST.get('pass')
            loc=request.POST.get('location')
            Producer.objects.create(name=name,password=password,location=loc,phone_no=no)
            request.session['type'] = "producer"
            p=Producer.objects.filter(password=password, phone_no=no)
            producer = p.first()
            request.session['id'] = producer.id
            return render(request,'producer.html')
    return redirect('login')

def consumer(request):
    if request.method == 'POST':
        if int(request.POST.get('type')) == 1:
            no = request.POST.get('phoneno')
            password = request.POST.get('pass')
            p = Consumer.objects.filter(password=password, phone_no=no)
            if p.exists():
                producer = p.first()
                request.session['type'] = "consumer"
                request.session['id'] = producer.id
                return render(request,'consumer.html')
        else:
            name=request.POST.get('name')
            no = request.POST.get('phoneno')
            password = request.POST.get('pass')
            loc=request.POST.get('location')
            Consumer.objects.create(name=name,password=password,location=loc,phone_no=no)
            request.session['type'] = "producer"
            p=Consumer.objects.filter(password=password, phone_no=no)
            producer = p.first()
            request.session['id'] = producer.id
            return render(request,'consumer.html')
    return redirect('login')
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
def buyveg(request):
    return render(request,'buyveg.html')
def buycrop(request):
    return render(request,'buycrops.html')
def buyfruits(request):
    product = Product.objects.filter(type="Fruit") 
    return render(request, 'buyfruits.html', {
        'product': product
    })