from django.shortcuts import render, redirect
import random
# Create your views here.
def main(request):
    
    if 'gold' not in request.session:
        request.session['gold']= 0
    
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
   
    return render(request,'index.html')

def process(request):
    jobs = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,50)
    }
    pay = jobs[request.POST['work']]
    print(jobs[request.POST['work']])
    print(request.POST)
    
    if(pay>=0):
        activity = f'You have gained ${pay} at the {request.POST["work"]}'
        request.session['activity_log'].append(activity)
    else:
        absPay = pay * -1
        activity =f'You have lost ${absPay} at the {request.POST["work"]}'
        request.session['activity_log'].append(activity)
    
    request.session['gold']+=pay
    return redirect('/')