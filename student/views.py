from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
import openpyxl
from easy_pdf.views import PDFTemplateView

# Create your views here.

def index(request):
    if "GET" == request.method:
        return render(request, 'student/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row[:1]:
                # if str(cell)[15]=='A':
                row_data.append(str(cell.value))
            for cell in row[-1:]:
                # if str(cell)[15]=='A':
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'student/index.html', {"excel_data":excel_data})


class UserProfileDetailView(generic.DetailView):
	model=UserProfile

	def get_context_data(self, **kwargs):
		context = super(UserProfileDetailView, self).get_context_data(**kwargs)
		return context

class WorkDetailView(generic.DetailView):
    model = Work
