from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Applicant
import openpyxl

# Display and submit form
def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicants.html', {'applicants': applicants})

# Handle form POST
def submit_applicant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Save to database
        Applicant.objects.create(name=name, email=email, phone=phone)

        return redirect('applicant_list')  # redirect to list after saving

# Export to Excel (already exists)
def export_applicants_to_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Applicants"

    ws.append(['Name', 'Email', 'Phone', 'Applied On'])

    applicants = Applicant.objects.all()
    for applicant in applicants:
        ws.append([
            applicant.name,
            applicant.email,
            applicant.phone,
            applicant.applied_on.strftime("%Y-%m-%d %H:%M:%S")
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=applicants.xlsx'
    wb.save(response)
    return response
