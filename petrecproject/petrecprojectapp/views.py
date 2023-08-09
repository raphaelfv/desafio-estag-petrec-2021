from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import csv

# Create your views here.

def home(request):
    return render(request, 'petrecprojectapp/home.html')

def data(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            # Store the CSV file in the session
            request.session['uploaded_csv_file'] = csv_file.read().decode('utf-8')

            # Redirect to the graph page
            return redirect('graph')
    else:
        form = CSVUploadForm()
    return render(request, 'petrecprojectapp/data.html', {'form': form})

def graph(request):
    # Retrieve the CSV file from the session
    uploaded_csv = request.session.get('uploaded_csv_file')

    # Parse CSV data and pass it to the template
    csv_data = []
    if uploaded_csv:
        reader = csv.reader(uploaded_csv.splitlines())
        for row in reader:
            csv_data.append(row)

    # Clear the session data to clean up
    if 'uploaded_csv_file' in request.session:
        del request.session['uploaded_csv_file']

    return render(request, 'petrecprojectapp/graph.html', {'csv_data': csv_data})

def feedback(request):
    return render(request, 'petrecprojectapp/feedback.html')