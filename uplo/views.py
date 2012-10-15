# Create your views here.
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from hellodjango.uplo.models import counter
from django.conf import settings
from hellodjango import captcha
def addthis(request):
	if request.method == "POST":
		captcha_response = captcha.submit(request.POST.get("recaptcha_challenge_field", None),request.POST.get("recaptcha_response_field", None),settings.RECAPTCHA_PRIVATE_KEY,request.META.get("REMOTE_ADDR", None))
		if not captcha_response.is_valid:
			captcha_error = "&error=%s" % captcha_response.error_code
			return render_to_response('ind.html',{'error':'Error in Captcha..<p>'});
		form=imageForm(request.POST,request.FILES)
		if form.is_valid():
			image=request.FILES['abtme']
			a=image.name.split('.')
			if(len(counter.objects.filter(name__icontains=form.cleaned_data['add']))!=1):
				k=counter(name=form.cleaned_data['add'],counter=0)
			else :
				k=counter.objects.get(name=form.cleaned_data['add'])
			k.counter=k.counter+1
			if image.size>500000:
				return render_to_response('ind.html',{'error':'File size was found to be greater than 500kB<p>'})
			if(len(a)!=2):
				return render_to_response('ind.html',{'error':'Invalid file name<p>'})
			dest=open('/home/baatooni/webapps/hellodjango/site_media/user_images/'+form.cleaned_data['add']+'_'+str(k.counter)+'.'+a[1],'wb+')
			for chunks in image.chunks():
				dest.write(chunks)
			dest.close()
			k.save()
			return render_to_response('ind.html',{'error':'%s has been uploaded.<p>'%image.name})
		else:
			return render_to_response('ind.html',{'error':'Invalid Form Submission<p>'})
	else:
		return render_to_response('ind.html',{})
class imageForm(forms.Form):
	abtme=forms.ImageField()
	add=forms.CharField(max_length=20)