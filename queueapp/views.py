from django.shortcuts import render, redirect
from .models import QueueEntry
from django.http import JsonResponse
from .models import QueueStatus 

# Create your views here.
def home(request):
    entries = QueueEntry.objects.filter(status='waiting').order_by('number')
    return render(request, 'index.html', {'entries': entries})

def join_queue(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        last = QueueEntry.objects.all().order_by('-number').first()
        new_number = (last.number + 1) if last else 1
        QueueEntry.objects.create(number=new_number, name=name, phone=phone, email=email)
        return redirect('/')
    return redirect('/')

def get_queue_data(request):
    entries = QueueEntry.objects.filter(status='waiting').order_by('number')
    data = [{"number": e.number, "name": e.name} for e in entries]
    return JsonResponse({"queue": data})

from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import QueueStatus  # you'll need to create this model

# 👨‍💼 Admin dashboard
def admin_dashboard(request):
    queue = QueueEntry.objects.all().order_by('number')
    return render(request, 'dashboard.html', {'queue': queue})

# 🎯 Perform actions like serve, skip, remove
def queue_action(request, user_id, action):
    entry = get_object_or_404(QueueEntry, id=user_id)
    if action == "serve":
        entry.status = "served"
        entry.save()
    elif action == "skip":
        entry.status = "skipped"
        entry.save()
    elif action == "remove":
        entry.delete()
    return redirect('admin_dashboard')

# 🔍 Search queue by name or phone
def search_queue(request):
    query = request.GET.get("q", "")
    results = QueueEntry.objects.filter(
        Q(name__icontains=query) | Q(phone__icontains=query)
    ).order_by('number')
    return render(request, 'dashboard.html', {'queue': results, 'search_query': query})

# 🔁 Reset queue
def reset_queue(request):
    QueueEntry.objects.all().delete()
    return redirect('admin_dashboard')

# ⛔ Toggle queue open/close (optional)
def toggle_queue_status(request):
    status, _ = QueueStatus.objects.get_or_create(id=1)
    status.is_open = not status.is_open
    status.save()
    return redirect('admin_dashboard')
