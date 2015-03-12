from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from forms import LoginForm, BookForm, UserForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def mainpage(request):
	if request.method == 'POST':
		db_id = request.POST['id']
		Books.objects.get(id=db_id).delete()
		return HttpResponseRedirect("/libapp/main/")
	books = Books.objects.all()
	if not request.user.additionaldetails.is_librarian:
		
		return HttpResponseRedirect("/libapp/book_view/")
	context = {'books': books}
	return render_to_response('viewtemp.html', context, context_instance=RequestContext(request))

@login_required
def userspage(request):
	# assert False, request.user
	if request.method == 'POST':
		if request.POST['submit_type'] == 'del':
			ud_id = request.POST['id']
			User.objects.get(id=ud_id).delete()
		elif request.POST['submit_type'] == 'ac':
			ud_id = request.POST['id']
			# User.objects.get(id=ud_id).additionaldetails.is_valid = True
			user = User.objects.get(id=ud_id)
			ad = AdditionalDetails.objects.get_or_create(
				user = user)[0]
			ad.is_valid = not ad.is_valid
			ad.save()



		return HttpResponseRedirect("/libapp/users/")
	AdditionalDetails.objects.get_or_create(user = request.user)
	users = User.objects.all()
	context = {'users': users}
	return render_to_response('users_data.html', context, context_instance=RequestContext(request))



	
	
@login_required
def AddingBook(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/libapp/main/")
	form = BookForm()
	if 'id' in request.GET:
		db_id = request.GET['id']
		b = Books.objects.get(id=db_id)
		initial_val = {'bd_id': db_id,
		'book_title':b.book_title,
		'date_of_pub': b.date_of_pub,
		'isbn_number': b.isbn_number,
		'book_author': b.book_author,
		'book_category': b.book_category,
		'qty_in_lib': b.qty_in_lib,
		#'qty_available': b.qty_available
		}
		form = BookForm(initial=initial_val)
	context = {'form': form}
	return render_to_response('add_books.html', context, context_instance=RequestContext(request))

@login_required
def request_book(request):
	if request.method == 'POST':
		issued_books = BookUserMap.objects.filter(user=request.user, book_returned=False).count()
		qty_lib = Books.objects.get(id=request.POST['book_id']).available_books()
		if issued_books >= 5:
			return HttpResponse("You can't get issued more than 5 books.")
		if qty_lib <= 0:
			return HttpResponse("There are no books available.") 
		a = BookUserMap(
			book_id = request.POST['book_id'],
			user = request.user,
			)
		a.save()

		return HttpResponseRedirect('/libapp/main/')

	issued_books = BookUserMap.objects.filter(user = request.user, book_returned=False).values('book')
	if 'searchbooks' in request.GET:
		search_book = request.GET['searchbooks']
		search = Books.objects.filter(book_title__icontains = search_book)
	else:
		search = Books.objects.all()
	book_search = search.exclude(id__in = issued_books).order_by('-book_title')
	context = {'book_search': book_search}
	return render_to_response('req_book.html', context, context_instance=RequestContext(request))


@login_required
def view_book(request):
	if request.method == 'GET':
		issued_books = BookUserMap.objects.filter(user = request.user, book_returned = False)

		context = {'issued': issued_books}
		return render_to_response('book_view.html', context, context_instance=RequestContext(request))
	if request.method == 'POST':
		# assert False, 
		a = BookUserMap.objects.get(id=request.POST['bum_id'])
		a.book_returned = True
		a.save()
		return HttpResponseRedirect('/libapp/book_view/')

		




@login_required
def removeuser(request):
	form = UserForm()
	if 'id' in request.GET:
		ud_id = request.GET['id']
		s = User.objects.get(id=ud_id)
		form = UserForm(initial={'ud_id': ud_id, 'username':s.username})
	context = {'form': form}
	return render_to_response('users_data.html', context, context_instance=RequestContext(request))



# Create your views here.
def index(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
		else:
			return "disabled account"
	else:
		return "invalid login"


def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/libapp/main/')
	context = RequestContext(request)
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user:
	    	ad = AdditionalDetails.objects.get_or_create(user=user)

	        if ad[0].is_valid:
	        	login(request, user)
	        	return HttpResponseRedirect('/libapp/main/')
	        else:
	            return HttpResponse("You don't have access. Create a new account to access.")
	    else:
	    	return "Invalid login details supplied."

	else:
	    ''' user is not submitting the form, show the login form '''
	    form = LoginForm()
	    context = {'form': form}
	    return render_to_response('login.html', context, context_instance=RequestContext(request))

@login_required
def user_view(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/main/')
	else:
		return HttpResponse("You are not logged in.")

@login_required
def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

def listing(request):
	book = Books.objects.all()
	paginator = Paginator(book, 5)
	page_num = request.GET.get('page', 1)
	try:
		page = paginator.page(page_num)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	context = {'page': page}
	return render_to_response('viewtemp.html', context, context_instance=RequestContext(request))