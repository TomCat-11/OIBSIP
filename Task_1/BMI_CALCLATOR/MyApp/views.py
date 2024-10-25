from django.shortcuts import render


def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = round(weight / (height ** 2))

        # Interpretation of BMI
        interpretation = get_bmi_interpretation(bmi)

        return render(request, 'result.html', {'bmi': bmi, 'interpretation': interpretation})

    return render(request, 'index.html')


def get_bmi_interpretation(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Healthy Weight'
    else:
        return 'Overweight'