from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import csv
from .forms import FeedbackForm

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
    uploaded_csv = request.session.get('uploaded_csv_file')

    csv_data = []
    if uploaded_csv:
        reader = csv.reader(uploaded_csv.splitlines())
        csv_data = [row for row in reader]

    if 'uploaded_csv_file' in request.session:
        del request.session['uploaded_csv_file']

    # Pass the CSV data as JSON and available headers to the template
    return render(request, 'petrecprojectapp/graph.html', {'csv_data': csv_data})

def feedback(request):
    feedback_sent = False  # Initialize to False

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the feedback to the database
            form = FeedbackForm()  # Create a new form
            feedback_sent = True  # Set to True when feedback is sent
    else:
        form = FeedbackForm()

    return render(request, 'petrecprojectapp/feedback.html', {'form': form, 'feedback_sent': feedback_sent})