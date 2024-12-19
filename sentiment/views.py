from django.shortcuts import render
from .forms import SentimentForm
from textblob import TextBlob

# Create your views here.

def home(request):
    return render(request, "sentiment/home.html")


# sentiment-analysis view
def analyse_sentiment(request):
    result = None
    polarity = None
    subjectivity = None

    if request.method == "POST":
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            analysis = TextBlob(text)
            polarity = analysis.polarity
            subjectivity = analysis.subjectivity

            if polarity > 0:
                result = "postive"
            elif polarity < 0:
                result = "Negative"
            else:
                result = "Neutral"
            
    else:
        form = SentimentForm()

    context = {
        "form" : form,
        "result" : result,
        "polarity": polarity,
        "subjectivity": subjectivity,
    }
    return render(request, "sentiment/sentiment.html", context)
