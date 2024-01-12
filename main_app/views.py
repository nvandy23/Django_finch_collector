from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# Create your views here.
finches = [
  {'name': 'Evening Grosbeak', 'habitat': 'Northern and montane forests', 'description': 'The Evening Grosbeak does not have a complex song, but rather draws from a collection of sweet, piercing notes and burry chirps.', 'Pop_Trend': 'Decreasing'},
  {'name': 'Pine Grosbeak', 'habitat': 'Open boreal forest', 'description': 'Locals in Newfoundland affectionately call Pine Grosbeaks "mopes" because they can be so tame and slow moving. Pine Grosbeaks declined by 2.4 percent per year between 1966 and 2015, resulting in a cumulative decline of 70 percent.', 'Pop_Trend': 'Decreasing'},
]
# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

#ABOUT view
def about(request):
    return render(request,'about.html')

def all_finches_index(request):
    finches = Finch.objects.all()
  # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
    'finches': finches
  })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/details.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  template_name = 'finches/finch_form.html'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['habitat', 'description', 'population_trend']
    template_name = 'finches/edit.html'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
  template_name ='finches/confirm_delete.html'
