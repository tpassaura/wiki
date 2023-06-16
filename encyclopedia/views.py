from django.shortcuts import render
from django.http import HttpResponse

import random
from . import util
import markdown2



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    # Get entry markdown information
    md_entry_info = util.get_entry(title)

    # If article do not exist
    if md_entry_info == None:
        return index(request)
    
    # If article exist open article page
    else:
        html_entry_info = markdown2.markdown(md_entry_info)
        return render(request, "encyclopedia/article.html",{
            "title": title,
            "entry": html_entry_info
        })

def search(request):
    entries = util.list_entries() # Get list of all articles available 
    query = request.GET.get('q', '')  # Get the value of the 'q' input field

    # If value searched exists, open aticle page
    if query in entries:
        return article(request, query)
    # If value searched dpo not exist, open search page
    else:
        results = []
        for entry in entries:
            if query.lower() in entry.lower():
                results.append(entry)

    # Handle case when query is not found
        return render(request, "encyclopedia/search.html", {
            "query":  query,
            "results": results
        })
    
def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']

        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists."
            })
        else:
            util.save_entry(title, content)
            return article(request, title)
        
def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", { 
            "title" : title,
            "content" : content,
        })
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)

    return article(request, title)

def ran(request):
    entrys = util.list_entries()
    entry = random.choice(entrys)
    return article(request, entry)


    
        

