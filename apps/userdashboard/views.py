from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.userdashboard.models import User, Message, Comment, Poke
from django.utils import timezone
from datetime import datetime

def index(request):
	return render(request, 'userdashboard/index.html')

def register(request):
	user = User.objects.filter(email= request.POST.get('email'), password=request.POST.get('password'))
	if len(user) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.password = request.POST.get('password')
		user.created_at = timezone.now()
		if len(User.objects.all()) < 1:
			user.user_level = 9;
		else:
			user.user_level = 1;
		user.save()
		return redirect('/')

def login(request):
	user = User.objects.filter(email=request.POST.get('email'))
	if len(user)<1:
		print "Failed"
		return redirect('/')
	else:
		request.session['user_id'] = user[0].id
		return redirect('/dashboard')

def dashboard(request):
	if "user_id" in request.session:
		user = User.objects.get(id=request.session['user_id'])
		users = User.objects.all().exclude(id=request.session['user_id'])
		reg_context = {
			'user': user,
			'users': users
		}
		admin_context = {
			'user': user,
			'users': users
		}
		if user.user_level == 9:
			return render(request, 'userdashboard/admindashboard.html', admin_context)
		else:
			return render(request, 'userdashboard/regdash.html', reg_context)
	else:
		del request.session
		return redirect('/')
def profile_page(request, user_id):
	poke_count = Poke.objects.all().filter(poked=user_id)
	user = User.objects.get(id=user_id)
	current_user = User.objects.get(id=request.session['user_id'])
	messages = Message.objects.all().filter(receiver=user)
	comments = Comment.objects.all()
	content = {
	'poke_count': poke_count,
	'current_user': current_user,
	'user': user,
	'messages': messages,
	'comments': comments,
	}
	return render(request, 'userdashboard/profile.html', content)

def delete(request, user_id):
	user = User.objects.get(id=user_id)
	user.delete()
	return redirect('/dashboard')

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=comment_id)
	comment.delete()
	return redirect('/dashboard')

def delete_message(request, message_id):
	message = Message.objects.get(id=message_id)
	message.delete()
	return redirect('/dashboard')

def edit(request, user_id):
		user = User.objects.get(id=user_id)
		current_user = User.objects.get(id=request.session['user_id'])
		content = {
		'current_user':current_user,
		'user': user
		}
		return render(request, 'userdashboard/adminedit.html', content)


def new(request):
	user = User.objects.get(id=request.session['user_id'])
	if user.user_level != 9:
		return redirect('/dashboard')
	else:
		return render(request, 'userdashboard/new.html')

def create(request):
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.password = request.POST.get('password')
		user.created_at = timezone.now()
		user.user_level = 1
		user.save()
		return redirect('/dashboard')

def poke(request, user_id):
	poke = Poke()
	poke.poker = User.objects.get(id=request.session['user_id'])
	poke.poked = User.objects.get(id=user_id)
	poke.counter = poke.counter+1
	poke.save()
	return redirect('/dashboard')

def message(request, user_id):
	message = Message()
	sending_user = User.objects.get(id=request.session['user_id'])
	receiving_user = User.objects.get(id=user_id)
	message.sender = sending_user
	message.receiver = receiving_user
	message.message = request.POST.get('message')
	message.created_at = timezone.now()
	message.save()
	return redirect('/dashboard')

def comment(request):
	sending_user = User.objects.get(id=request.session['user_id'])
	message = Message.objects.get(id=request.POST.get('message_id'))
	comment = Comment()
	comment.sender = sending_user
	comment.message = message
	comment.comment = request.POST.get('comment')
	comment.created_at = timezone.now()
	comment.save()
	return redirect('/dashboard')

def update(request, user_id):
	user = User.objects.get(id=user_id)
	user.first_name = request.POST.get('first_name')
	user.last_name = request.POST.get('last_name')
	user.description = request.POST.get('description')
	user.email = request.POST.get('email')
	if request.POST.get('password') == request.POST.get('confirm_password'):
		user.password = request.POST.get('password')
		user.user_level = request.POST.get('user_level')
		user.save()
		return redirect('/dashboard')

def logout(request):
	del request.session['user_id']
	return redirect('/')