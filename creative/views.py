# Create your views here..
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from hellodjango.creative.models import stores
from django.core.mail import send_mail

def submit(request):
	a=request.POST['myimage'];
	i=len(stores.objects.all())
	b=stores(secret=(i*i)^((i+1)*(i+1))^(3*i)^192,value=a,age=-1)
	b.save()
	return getdet(request,b.id,b.secret)
	
def getImage(request):
	a=int(request.GET.get('id',0))
	b=stores.objects.get(id=a)
	if b.secret==request.GET.get('secret',0) or request.GET.get('secret',0)=='721302':
		return HttpResponse(b.value,mimetype="image/svg+xml")
	else:
		return render_to_response('viscomtemp.html',{'data':'Access denied'})

def getit(request):
	return render_to_response('viscomtemp.html',{'data':'<embed src="/creative/getimage.svg?id=%s&secret=%s" width="1200" height="1000" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" />'%(request.GET.get('id',0),request.GET.get('secret',0))})
	
def getdet(request,id,secret):
	return render_to_response('viscomtemp.html',{'data':"\
	Please provide us with some more details after you with link to share your image\
	<form action='/creative/mysubmit/?id=%s&secret=%s' method='POST'>\
	Name:<input type='text' name='username'/><br/>\
	Age:<input type='text' name='age'/><br/>\
	Email id so that we may contact you:<input type='text' name='emailid' /><br />\
	Title for your image:<input type='text' name='title' /><br/>\
	Password to claim your image later:<input type='password' name='pass' /><br/>\
	Do you wish this pic to be secret?<input type='checkbox' name='secret'/>\
	<input type='submit' value='submit'/>"%(id,secret)})
	
def getfront(request):
	return render_to_response('viscom.html',{'a':'abc'})

def submitx(request):
	a=request.POST['username']
	b=request.POST['age']
	c=request.GET.get('id',0)
	d=request.GET.get('secret',0)
	emailid=request.POST['emailid']
	title=request.POST['title']
	passx=request.POST['pass']
	ob=stores.objects.get(id=c)
	if ob.age!=-1:
		return render_to_response('Form was already submitted')
	if d!=ob.secret:
		return render_to_response('Access Denied')
	ob.name=a
	try:
		ob.age=int(b)
	except:
		ob.age=18
	ob.emailid=emailid
	ob.title=title
	ob.passx=passx
	try:
		if request.POST['secret']=='off':
			ob.secret=0
	except:
		pass
	try:
		send_mail('Your submission at baatooni.com','Hi,\nThis is an autogeerated email in response to a submission at baatooni.com. Please ignore this if it is not for you.\nThankyou for your submission. Your submission is very valuable to us.'+'Share your image at http://www.baatooni.com/creative/getit/?id='+str(ob.id)+'&secret='+str(ob.secret)+' .Please share this among your friends and your social profiles so as to contribute for this survey to be a successful one. You may reshare the link shared at my profile http://www.facebook.com/sayhellotojai. Or you may directly share this link http://www.baatooni.com/creative/viscom.\n Thanking You,\nJai Gupta and Team,\nCreativity Survey Team','jaigupta@baatooni.com',[emailid],True,'jaigupta@baatooni.com','321bg@ig')
	except:
		pass
	ob.save()
	return render_to_response('viscomtemp.html',{'data':'Thank You.<br/>Share your image at http://www.baatooni.com/creative/getit/?id=%s&secret=%s<br/> Tag Your friends on fcebook with this Image to let them now about your creation.'%(ob.id,ob.secret)})
	
def sendit(request):
	try:
		send_mail('This is a generated email','Thankyou','jaigupta@baatooni.com',['sayhellotojai@gmail.com'],True,'jaigupta@baatooni.com','321bg@ig')
	except:
		return HttpResponse('error occured')
	return	HttpResponse('Hi')