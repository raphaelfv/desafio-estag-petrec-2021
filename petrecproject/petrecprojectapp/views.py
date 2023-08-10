from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import csv
from .forms import FeedbackForm
import json

# Create your views here.

def home(request):
    homeCondition = True
    return render(request, 'petrecprojectapp/home.html', {'homeCondition': homeCondition})

def data(request):
    dataCondition = True
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
    return render(request, 'petrecprojectapp/data.html', {'form': form, 'dataCondition': dataCondition})

def graph(request):
    graphCondition = True
    uploaded_csv = request.session.get('uploaded_csv_file')

    csv_data = []
    if uploaded_csv:
        reader = csv.DictReader(uploaded_csv.splitlines())
        csv_data = [row for row in reader]

    if 'uploaded_csv_file' in request.session:
        del request.session['uploaded_csv_file']

    csv_data_json = json.dumps(csv_data)

    csv_columns = csv_data[0].keys() if csv_data else []

    return render(request, 'petrecprojectapp/graph.html', {'csv_data_json': csv_data_json, 'csv_columns': csv_columns, 'graphCondition': graphCondition})

def feedback(request):
    feedbackCondition = True
    feedback_sent = False  # Initialize to False

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the feedback to the database
            form = FeedbackForm()  # Create a new form
            feedback_sent = True  # Set to True when feedback is sent
    else:
        form = FeedbackForm()

    return render(request, 'petrecprojectapp/feedback.html', {'form': form, 'feedback_sent': feedback_sent, 'feedbackCondition': feedbackCondition})