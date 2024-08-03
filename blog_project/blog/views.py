# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import BlogPost, Contact
from .serializers import UserSerializer, BlogPostSerializer
from django.core.mail import send_mail
from .forms import ContactForm

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

def blog_list_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

def home_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def home1_view(request):
    # posts = BlogPost.objects.all()
    return render(request, 'blog/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                message=form.cleaned_data['message'],
            )
            contact.save()

            # Send email
            send_mail(
                'New Contact Form Submission',
                f"Email: {form.cleaned_data['email']}\nPhone Number: {form.cleaned_data['phone_number']}\nMessage: {form.cleaned_data['message']}",
                'astik.ezyhelpers@gmail.com',  # Replace with your email
                ['astikblogs@gmail.com'],     # Replace with the recipient's email
            )

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'blog/success.html')