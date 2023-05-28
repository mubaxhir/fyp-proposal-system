import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from main.forms import StudentProposalForm
from main.serializers import ProposalSerializer
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

"""# from .forms import StudentLoginForm,MemberLoginForm
# Create your views here.

# this is for both studnet and member that here  is someproblem in the logics
# def signin(request):
#     if request.method == "POST":
#         student_form = StudentLoginForm(request.POST)
#         member_form = MemberLoginForm(request.POST)
#         print('helllllll')
#         if student_form.is_valid():
#             # Process student login
#             student_username = student_form.cleaned_data.get('student_username')
#             student_password = student_form.cleaned_data.get('student_password')
#             student_user = authenticate(request, username=student_username, password=student_password)
#             print("hello")
#             if student_user is not None:
#                 # Student login successful
#                 login(request, student_user)
#                 return redirect('students')
#             else:
#                 # Student login failed
#                 return render(request, 'Login.html', {'student_form': student_form, 'member_form': member_form, 'error': 'Invalid student login'})
        
#         elif member_form.is_valid():
#             # Process member login
#             member_username = member_form.cleaned_data.get('member_username')
#             member_password = member_form.cleaned_data.get('member_password')
#             member_user = authenticate(request, username=member_username, password=member_password)
            
#             if member_user is not None:
#                 # Member login successful
#                 login(request, member_user)
#                 return redirect('members')
#             else:
#                 # Member login failed
#                 return render(request, 'Login.html', {'student_form': student_form, 'member_form': member_form, 'error': 'Invalid member login'})
        
#         else:
#             # Both forms are invalid
#             return render(request, 'Login.html', {'student_form': student_form, 'member_form': member_form, 'error': 'Invalid form data'})

#     else:
#         student_form = StudentLoginForm()
#         member_form = MemberLoginForm()
#         return render(request, 'Login.html', {'student_form': student_form, 'member_form': member_form})

"""

@login_required(login_url='signin/')
def index(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    if request.user:
        print(request.user)
        try:
            student = Student.objects.get(user=request.user)
            return redirect('students')
        except:
            try:
                member = Member.objects.get(user=request.user)
                return redirect('member')
            except:
                return redirect('signin')
    else:
        return redirect('signin')
    
@csrf_exempt
def create_user(request):
    
    data = json.loads(request.body)
    
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    is_student = data.get('is_student')
    email = data.get('email')

    user = CustomUser.objects.create(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        is_student=is_student,
        is_member=True if not is_student else False
    )
    
    if is_student:
        roll_number = data.get('roll_number')
        Student.objects.create(
            user = user,
            name = username,
            email = email,
            roll_number = roll_number
        )
    else:
        role = data.get('role')
        Member.objects.create(
            user = user,
            name = username,
            email = email,
            role = role
        )    
        
    return JsonResponse({
        'message': 'user created successfully',
    })

def signin(request):
    
    if request.user.pk:
    
        # Get the current user.
        user = CustomUser.objects.get(pk=request.user.pk)
                
    if request.method == "POST":
        username = request.POST.get('username')
        password =  request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username, password=password)
        except:
            user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_student:
                student = Student.objects.get(user=user)
                return redirect('students')
            else:
                member = Member.objects.get(user=user)
                return redirect('member')
        else:
            return render(request, 'Login.html', {'error': 'User not found'})
    else:
        # form = LoginForm()
        return render(request, 'Login.html')
    

@login_required(login_url='signin/')
def students(request):
    proposal = Proposal.objects.filter(student__user=request.user)
    try:
        review = ProposalReview.objects.get(proposal=proposal).review
        status = 'reviewed'
        due_date = review.get_due_date()
        context = {
            'review': review,
            'status': status,
            'due_date': due_date,
            'submitted_date': proposal.datetime
        }
        
    except ProposalReview.DoesNotExist:
        review = 'Pending'
        status = 'submited'
        due_date = 'N/A'
        context = {
            'review': review,
            'status': status,
            'due_date': due_date,
            'submitted_date': proposal.datetime
        }
    
            
    except Exception as e:
        print(e)
        review = 'N/A'
        status = 'N/A'
        due_date = 'N/A'
        
        context = {
            'review': review,
            'status': status,
            'due_date': due_date,
            'submitted_date': 'N/A'
        }
        
    context['notifications'] = Notication.objects.all()
        
    return render(request, 'StudentsInterface.html', context)
  

@login_required(login_url='signin/')
def members(request):
    return render( request,'MemberInterface.html')

@login_required(login_url='signin/')
def welcome(request):
    return render( request,'WelcomePage.html')

@login_required(login_url='signin/')
def enrolllment(request):
    return render( request,'StudentsEnrollment.html')

@login_required(login_url='signin/')
def student_info(request):
    students = Student.objects.all()
    for student in students:
        try:
            props = Proposal.objects.filter(student=student)[0]
            student.proposal = props.title
            student.class_field = props.class_field
        except: 
            student.proposal = "N/A"
            student.class_field = "N/A"
    return render( request,'StudentInfo.html', {'students':students})

@login_required(login_url='signin/')
def student_proposal_info(request):
    context = {
        'student_roll_number' : Student.objects.get(user=request.user).roll_number
    }
    return render( request,'student-proposal-info.html', context)

@csrf_exempt
@login_required(login_url='signin/')
def projects(request, status='all'):
    
    student = request.GET.get('student', '')
        
    if status=='all':
        proposals = Proposal.objects.all()
    else:  
        proposals = Proposal.objects.filter(status=status)
        
    if student:
        proposals=proposals.filter(Q(student__roll_number=student) | Q(student_rolls__contains=student))
        
    query = request.GET.get('search', '')
    proposals = proposals.filter(title__contains=query).order_by('presentation')
    return JsonResponse(ProposalSerializer(proposals, many=True).data, safe=False)

@csrf_exempt
@login_required(login_url='signin/')
def update_status(request, obj_id, status):
    Proposal.objects.filter(id=obj_id).update(status=status)
    return JsonResponse({'message': 'success'})

@login_required(login_url='signin/')
@csrf_exempt
def add_comment(request):
    if request.method == "POST":   
        data = json.loads(request.body)  
        ids = data["proposals"]
        presentation_times = data["presentation_times"]
        for proposal in Proposal.objects.filter(id__in=ids):
            proposal.comments = data["comment"]
            proposal.presentation = presentation_times[str(proposal.id)] if presentation_times[str(proposal.id)] != 'null' else None
            proposal.save()
            
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'Invalid request'})

@login_required(login_url='signin/')
def proposal_info(request):
    proposals = Proposal.objects.all()
    return render(request,'ProposalInfo.html', {'proposals': proposals})

@login_required(login_url='signin/')
def project_proposal(request):
    proposals = Proposal.objects.all()
    return render( request,'ProjectProposal.html', {'proposals': proposals})

@login_required(login_url='signin/')
def member_info(request):
    return render( request,'MembersInfo.html')

@login_required(login_url='signin/')
def main_page(request):
    return render( request,'MainSigninPage.html')


@login_required(login_url='signin/')
def student_proposal_details(request):
    if request.method == "POST":
        
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        student_class = request.POST.get('class')
        student = Student.objects.get(user=request.user)
        student_names = request.POST.getlist('student_name[]')
        student_rolls = request.POST.getlist('roll_no[]')
        student_sections = request.POST.getlist('section[]')
        Proposal.objects.create(
            title=title,
            description=desc,
            student=student,
            student_names=','.join(student_names),
            student_rolls=','.join(student_rolls) ,
            student_sections=','.join(student_sections)
        )
        
        return redirect('students')  # Redirect to the students page after form submission
    
    return render(request, 'StudentProposalDetails.html')

def logout_view(request):
    logout(request)
    return redirect('signin')