from django.shortcuts import render

posts = [
    {
        "author": "Peter J.",
        "title": "First Post Title.",
        "content": "First post content.",
        "date_posted": "3/13/2023, 9:52pm"
    },
    {
        "author": "John Doe",
        "title": "Second Post Title.",
        "content": "Second post content.",
        "date_posted": "3/13/2023, 10:00pm"
    },
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
