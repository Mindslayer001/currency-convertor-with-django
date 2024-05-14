import requests
from django.shortcuts import render
from django.http import HttpResponse

def post(request, to_currency, amount, from_currency):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"
    response = requests.get(url)
    print(url)
    data = response.json()
    result = data[from_currency][to_currency] * float(amount)
    context = {
        "rate": result,
        "currency": to_currency
    }
    return render(request, 'template.html', context)

def getInput(request):
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        amount = request.POST.get("amount")
        return post(request, to_currency, amount, from_currency)
    else:
        return render(request, 'input_form.html')
