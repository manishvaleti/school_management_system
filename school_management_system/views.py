from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .models import *
from .forms import *
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'html/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'html/login.html')
def logout_view(request):
    logout(request)
    return redirect('login') 
# Create your views here.
def home(request):
    # Count the number of items in each database table
    staff_count = Staff.objects.count()
    student_count = Student.objects.count()
    subject_count = Subject.objects.count()
    class_count = Class.objects.count()

    context = {
        'staff_count': staff_count,
        'student_count': student_count,
        'subject_count': subject_count,
        'class_count': class_count,
    }
    return render(request, 'html/home.html', context)

def staff_list(request):
    records = Staff.objects.all()
    return render(request, 'html/staff.html', {'records': records})

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('staff')  # Redirect to the staff list page after successfully adding staff
    else:
        form = StaffForm()
    return render(request, 'html/add_staff.html', {'form': form})

def edit_staff(request,staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff')  # Redirect to the staff list page after successfully editing staff
    else:
        form = StaffForm(instance=staff)
    return render(request, 'html/edit_staff.html', {'form': form, 'staff': staff})

def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Staff member deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'html/students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'html/add_student.html', {'form': form})

def edit_student(request, student_id):
    # Fetch the student object from the database
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Populate the form with the POST data and instance of the student
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        # Populate the form with the instance of the student
        form = StudentForm(instance=student)

    return render(request, 'html/edit_student.html', {'form': form})

def delete_student(request, student_id):
    staff = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Student member deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'html/subjects.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'html/add_subject.html', {'form': form})

def delete_subject(request, subject_id):
    staff = get_object_or_404(Subject, id=subject_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Subject deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def classes_list(request):
    classes = Class.objects.all()
    return render(request, 'html/classes.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes_list')
    else:
        form = ClassForm()
    return render(request, 'html/add_class.html', {'form': form})

def delete_class(request, class_id):
    staff = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Class deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'html/payments.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'html/add_payment.html', {'form': form})

def edit_payment(request, payment_id):
    # Fetch the payment object from the database
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        # Populate the form with the POST data and instance of the payment
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        # Populate the form with the instance of the payment
        form = PaymentForm(instance=payment)

    return render(request, 'html/edit_payment.html', {'form': form})

def delete_payment(request, payment_id):
    staff = get_object_or_404(Payment, id=payment_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Payment deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)

def class_register_list(request):
    registrations = ClassRegister.objects.all()
    return render(request, 'html/class_register_list.html', {'registrations': registrations})

def add_class_register(request):
    if request.method == 'POST':
        form = ClassRegisterForm(request.POST)
        if form.is_valid():
            # Check if the class has already been registered x times
            class_obj = form.cleaned_data['classes']
            if class_obj.registration.count() >= class_obj.class_count:
                # Return error message or handle accordingly
                pass
            else:
                form.save()
                return redirect('class_register_list')
    else:
        form = ClassRegisterForm()
    return render(request, 'html/add_class_register.html', {'form': form})

def delete_class_register(request, class_register_id):
    staff = get_object_or_404(Payment, id=class_register_id)
    
    if request.method == 'POST':
        staff.delete()
        return JsonResponse({'message': 'Registration deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)


def staff_classes(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    classes_teaching = Class.objects.filter(teacher=staff).values_list('subject', flat=True)
    return JsonResponse(list(classes_teaching), safe=False)


def view_student_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    # Retrieve payments and classes registered for the student
    payments = Payment.objects.filter(student=student)
    class_registers = ClassRegister.objects.filter(student=student)
    
    context = {
        'student': student,
        'payments': payments,
        'class_registers': class_registers,
    }
    return render(request, 'html/student_detail.html', context)

def update_marks(request, class_register_id):
    class_register = ClassRegister.objects.get(pk=class_register_id)
    
    if request.method == 'POST':
        form = UpdateMarkForm(request.POST, instance=class_register)
        if form.is_valid():
            form.save()
            return redirect('view_student_details', student_id=class_register.student.id) # Redirect to the student details page after saving
    else:
        form = UpdateMarkForm(instance=class_register)
    
    return render(request, 'html/update_marks.html', {'form': form})