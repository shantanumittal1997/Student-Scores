from django.core.mail import EmailMessage
from .models import Student

def send_report_card():
    
    students = Student.objects.all()
    
    for student in students:

        email = EmailMessage(
                    subject='Your Report Card',
                    body= f'Hi, {student.name} here is your scores for subjects',
                    to=[student.email]
                 )
        email.send(fail_silently=True)

    return {'status': 'sent successfully'}