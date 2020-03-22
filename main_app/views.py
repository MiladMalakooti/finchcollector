from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Ted', 'Blackcap', 'Pretty and calm', 5),
  Finch('Cusco', 'Hill Mynah', 'Taking bird pretty blue color', 3),
  Finch('Luis', 'Indian Hill Mynah', 'Loud bird with orange beak', 4),
]

# Create your views here.
def home (request):
  return HttpResponse('<h1> Finch Collector</h1>')

def about (request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })