import os

def populate():
    u1 = User.objects.create_user('A', 'A@gmail.com', 'super')
    u1.save()
    p1 = add_Product(u1.id,'p1_2','400')
   # n1 = add_Notification(p1.id, p1.amount, "abc", "delhi")
   
    u2 = User.objects.create_user('B', 'B@gmail.com', 'super')
    u2.save()
    p2 = add_Product(u2.id,'p2_2','500')
    #n2 = add_Notification(p2.id, p2.amount, "abc", "delhi")
    
    u3 = User.objects.create_user('C', 'C@gmail.com', 'super')
    u3.save()
    p3 = add_Product(u3.id,'p3_3','600')
    #n3 = add_Notification(p3.id, p3.amount, "abc", "delhi")


def add_Product(selId, prodName, amt):
    prod = Product.objects.get_or_create(sellerId = selId, productName = prodName, amount = amt)[0]
    return prod

def add_Notification(sellId, prodId, amt, buyer, shipAddr):
    notify = Notification.objects.get_or_create(sellerId = sellId, productId = prodId, amount = amt, buyerName = buyer, shippingAddr = shipAddr)[0]
    return notify

if __name__ == '__main__':
    print "Starting Population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paytm_project.settings')
    from django.contrib.auth.models import User
    from ppayment.models import Product, Notification
    populate()

