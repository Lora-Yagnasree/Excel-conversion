from django.shortcuts import render

# Create your views here.
# views.py
import openpyxl
from django.http import HttpResponse
from .models import Applicant

def export_applicants_to_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Applicants"

    # Add column headers
    ws.append(['Name', 'Email', 'Phone', 'Applied On'])

    # Add data rows
    applicants = Applicant.objects.all()
    for applicant in applicants:
        ws.append([applicant.name, applicant.email, applicant.phone, applicant.applied_on.strftime("%Y-%m-%d %H:%M:%S")])

    # Create HTTP response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=applicants.xlsx'
    wb.save(response)
    return response
def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicants.html', {'applicants': applicants})
