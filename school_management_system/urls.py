from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='home'),
    path('',login_view,name='login'),
    path('logout/', logout_view, name='logout'),
    path('staff/',staff_list,name='staff'),
    path('addStaff/', add_staff, name='add_staff'),
    path('delete_staff/<int:staff_id>/', delete_staff, name='delete_staff'),
    path('edit_staff/<int:staff_id>/',edit_staff,name='edit_staff'),
    path('students/', student_list, name='student_list'),
    path('students/add/', add_student, name='add_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('subject/', subject_list, name='subject_list'),
    path('subject/add/', add_subject, name='add_subject'),
    path('delete_subject/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('classes/', classes_list, name='classes_list'),
    path('classes/add/', add_class, name='add_class'),
    path('delete_class/<int:class_id>/', delete_class, name='delete_class'),
    path('payments/', payment_list, name='payment_list'),
    path('payments/add/', add_payment, name='add_payment'),
    path('edit_payment/<int:payment_id>/', edit_payment, name='edit_payment'),
    path('delete_payment/<int:payment_id>/', delete_payment, name='delete_payment'),
    path('class_register/', class_register_list, name='class_register_list'),
    path('class_register/add/', add_class_register, name='add_class_register'),
    path('delete_class_register/<int:class_register_id>/', delete_class_register, name='delete_class_register'),
    path('staff_classes/<int:staff_id>/', staff_classes, name='staff_classes'),
    path('view_student/<int:student_id>/', view_student_details, name='view_student_details'),
    path('update_marks/<int:class_register_id>/', update_marks, name='update_marks'),
]
