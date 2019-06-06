from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
# Create your views here.
def index(request):

    pass

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'import_and_edit_excel/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'import_and_edit_excel/upload.html')


def build_report(request):
    uploaded_file_url = request.GET.get('uploaded_file_url', None)

    # If no uploaded file is specified, redirect to file upload page
    if uploaded_file_url is None:
        return redirect('upload')

    saved_file_url = run_report(file=uploaded_file_url,
                                save_to='/home/martokk/PycharmProjects/tutorials/import_and_edit_excel/edited_files/')




    context = {
        'uploaded_file_url': uploaded_file_url,
        'saved_file_url': saved_file_url
    }


    return render(request, 'import_and_edit_excel/build_report.html', context)


def run_report(file, save_to):
    """
    Demo Report
    See tutorial @ http://zetcode.com/articles/openpyxl/
    """
    import openpyxl
    import os

    file_location, file_name = os.path.split(file)
    file_basename, file_ext = os.path.splitext(file_name)

    book = openpyxl.load_workbook(file)
    sheet = book.active

    sheet['B2'] = 10
    sheet['B3'] = 20

    sheet['C2'].value = "=SUM(A2:B2)"
    sheet['C3'].value = "=SUM(A3:B3)"

    saved_file_url = f"{save_to}/{file_basename}_edited.xlsx"

    book.save(saved_file_url)

    return saved_file_url

