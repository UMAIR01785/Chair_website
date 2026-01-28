from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Compose email
            subject = f'New Contact Form Submission from {first_name} {last_name}'
            email_message = f"""
You have received a new message from the contact form:

Name: {first_name} {last_name}
Email: {email}

Message:
{message}

---
This email was sent from the Furni website contact form.
            """
            
            try:
                # Send email to company
                send_mail(
                    subject,
                    email_message,
                    settings.EMAIL_HOST_USER,  # From email
                    [settings.EMAIL_HOST_USER],  # To email (company email)
                    fail_silently=False,
                )
                
                # Send confirmation email to user
                user_subject = 'Thank you for contacting Furni'
                user_message = f"""
Hi {first_name},

Thank you for reaching out to us! We have received your message and will get back to you as soon as possible.

Here's a copy of your message:
{message}

Best regards,
The Furni Team
                """
                
                send_mail(
                    user_subject,
                    user_message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                return redirect('contact')
                
            except Exception as e:
                messages.error(request, f'Error: {str(e)}. Your message has been saved.')
                print(f'Email error: {e}')
                import traceback
                traceback.print_exc()
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()

    return render(request, 'contact/conatct.html', {'form': form})