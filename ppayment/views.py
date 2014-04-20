from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db import connection

def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('ppayment/index.html', context_dict, context)

def user_login(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('ppayment/login.html', context_dict, context)

def success(request):
    return HttpResponse("Your Payment is Successful...")

def cancel(request):
    return HttpResponse("Your payment is NOT successful. Please try again!")

def notify(request):
    return HttpResponse("Seller is notified")

def fetchLoggedInUser(request):
    current_user = request.user()
    print current_user.id
    return current_user.id

def product_sql(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT id, productName, amount FROM ppayment_product WHERE sellerId = %s", [user_id])
    rowset = dictfetchall(cursor)
    return rowset
    
def order_sql(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT timeStamp, productId, amount, buyerName, shippingAddr FROM ppayment_notification WHERE id = %s", [user_id])
    rowset = dictfetchall(cursor)
    return rowset

def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
            ]

def login_view(request):
    print "In login_view"
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_id = request.user.id
                print user_id
                prod_dict = product_sql(user_id)
                order_dict = order_sql(user_id)
                #data = [prod_dict, order_dict]
                context_dict = {'prod_dict':prod_dict,'order_dict':order_dict, 'mou_id': user_id, 'seller_name': username}
                return render_to_response('ppayment/orders.html',context_dict, context)
            else:
                return HttpResponse("Disabled Account!")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid Login details supplied...")
    else:
        return render_to_response('ppayment/', {}, context)

@login_required
def logout_view(request):
    context = RequestContext(request)
    logout(request)
    return render_to_response('ppayment/login.html',{}, context)

@login_required
def restricted(request):
    return HttpResponseRedirect('/ppayment/orders/')
