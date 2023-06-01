from django.urls import path
from lmsAdmin.views import AdminDashboardView,LoginView, StudentAddView,StudentAddDetailView,LoginBackendView, \
 StudentListView, StudentEditView, StudentDeleteView, TeacherAddView,TeacherAddDetailView, \
  TeacherListView,TeacherEditView, assign_teacher, AddClassView, ClassDetailView, EditClassView, assign_teacher_page


urlpatterns = [
    path('',AdminDashboardView,name="dashboard"),

    # Login
    path('',LoginView,name="login"),
    path('loginbackend/',LoginBackendView,name="loginbacked"),

    # Student
    path('addstudent/',StudentAddView,name="addstudent"),
    path('addstudentdetail/',StudentAddDetailView,name="addstudentdetail"),
    path('studentlist/',StudentListView,name="studentlist"),
    path('studentedit/<int:id>',StudentEditView,name="studentedit"),
    path('studentdelete/<int:id>',StudentDeleteView,name="studentdelete"),
    

    # Teacher
    path('addteacher/',TeacherAddView,name="addteacher"),
    path('addteacherdetail/',TeacherAddDetailView,name="addteacherdetail"),
    path('teacherlist/',TeacherListView,name="teacherlist"),
    path('teacheredit/<int:id>',TeacherEditView,name="teacheredit"),


    # class 
    path('addclass/',AddClassView,name="addclass"),
    path('editclass/<int:id>',EditClassView,name="editclass"),
    path('assign-teacher-page/<int:id>', assign_teacher_page, name="assignteacherpage"),
    path('assign-teacher/', assign_teacher, name="assignteacher"),
    path('classdetail/<int:id>', ClassDetailView, name="classdetail")

]