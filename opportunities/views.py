from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from opportunities.models import Opportunity
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='signin')
def opportunities(request):
    allopportunities = Opportunity.objects.all()
    context = {'allopportunities':allopportunities}
    return render(request, 'opportunity/opportunities.html',context)