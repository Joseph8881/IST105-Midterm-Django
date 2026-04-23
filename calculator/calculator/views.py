from django.shortcuts import render
from .forms import CalculatorForm

def calculate(request):
    result = None

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            op = form.cleaned_data['operation']

            if op == 'add':
                result = num1 + num2
            elif op == 'sub':
                result = num1 - num2
            elif op == 'mul':
                result = num1 * num2
            elif op == 'div':
                result = num1 / num2 if num2 != 0 else "Error"

    else:
        form = CalculatorForm()

    return render(request, 'calculator/index.html', {
        'form': form,
        'result': result
    })