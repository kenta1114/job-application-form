from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def spots_view(request):
    return HttpResponse(articles["sports"])


def news_view(request, topic):
    return HttpResponse(articles[topic])


def add_view(request, num1, num2):
    result = num1 + num2
    return HttpResponse(str(result))


def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    webpage = reverse("topic-page", args=[topic])
    return HttpResponseRedirect(webpage)


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
            )

            message_body = (
                f"A new job application was submitted. Thank you,\n{first_name}."
            )
            email_message = EmailMessage("Form submission confirmation")

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
