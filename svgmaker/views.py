# Create your views here.
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from math import cos,sin,pi
import simplejson as json
from models import values,myform
import xlwt,csv

def getsvg(request):
	(a,b,c,d)=(0,0,0,0)
	if request.method=='POST':
		try:
			a=request.POST['can1']
		except:
			a=0
		try:
			b=request.POST['can2']
		except:
			b=0
		try:
			c=request.POST['can3']
		except:
			c=0
		try:
			d=request.POST['can4']
		except:
			d=0
	else:
		return HttpResponse('This is for demo purpose.<br> Enter the statistical integral values of four fields in the given boxes and submit<br> It generates different graphs based on the values. These are SVG graphics.<br><form action="getit" method="POST"><input type="text" name="can1"><br><input type="text" name="can2"><br><input type="text" name="can3"><br><input type="text" name="can4"><br><input type="submit" value="submit"></form>')

def getit(request):
	if request.method=='POST':
		try:
			a=request.POST['can1']
		except:
			a=0
		try:
			b=request.POST['can2']
		except:
			b=0
		try:
			c=request.POST['can3']
		except:
			c=0
		try:
			d=request.POST['can4']
		except:
			d=0
		return HttpResponse('<html><body><embed src="bar.svg?a=%s&b=%s&c=%s&d=%s" width="900" height="170" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" ><form action="getit" method="POST"><input type="text" name="can1"><br><input type="text" name="can2"><br><input type="text" name="can3"><br><input type="text" name="can4"><br><input type="submit" value="submit"></form></html></body>'%(a,b,c,d))
		
def getbar(request):
	a=int(request.GET.get('a',0))
	b=int(request.GET.get('b',0))
	c=int(request.GET.get('c',0))
	d=int(request.GET.get('d',0))
	max=a
	if b>max:
		max=b
	if c>max:
		max=c
	if d>max:
		max=d
	a=a*90/max
	b=b*90/max
	c=c*90/max
	d=d*90/max
	sum=a+b+c+d;
	x1=50+50*cos(2*pi*a/sum)
	x2=50+50*cos(2*pi*(a+b)/sum)
	x3=50+50*cos(2*pi*(a+b+c)/sum)
	x4=50+50*cos(2*pi)
	
	y1=50+50*sin(2*pi*a/sum)
	y2=50+50*sin(2*pi*(a+b)/sum)
	y3=50+50*sin(2*pi*(a+b+c)/sum)
	y4=50
	return render_to_response("bar.svg",{'a':100-a,'b':(a-b),'c':(b-c),'d':(c-d),'a1':a,'b1':b,'c1':c,'d1':d,'a2':100-a,'b2':100-b,'c2':100-c,'d2':100-d,'x1':x1,'y1':y1,'x2':x2,'y2':y2,'x3':x3,'y3':y3,'x4':x4,'y4':y4,},mimetype="image/svg+xml")
	
def tryjson(request):
	return HttpResponse(request.POST)

def saveform(request):
	if request.method!='POST':
		return HttpResponse("No Post Data.")
	try:
		d=json.loads(request.POST['formdata'])
	except:
		return HttpResponse("Sorry Form could not be submitted.")
	val=myform(title=request.POST['title'],data=json.dumps(d),slabel=request.POST['slabel'])
	val.save()
	count=len(myform.objects.all())
	return HttpResponse("Form successfully saved. Use the link <a href='/svg/showform/?id=%s'>http://127.0.0.1:8080/svg/showform/?id=%s</a><br>See all the forms submitted <a href='/svg/allform'>here</a>."%(count,count))
	
def getform(request):
	try:
		a=myform.objects.get(id=request.GET.get('id',0)).data
	except:
		a="{error:'Form does not exist'}"
	return HttpResponse("%s"%a)
	
def showform(request):
	return render_to_response('template.html',{'id':request.GET.get('id',0)})

def allform(request):
	a=myform.objects.all()
	b=[]
	for i in range(len(a)):
		b.insert(i,[])
		b[i].insert(0,a[i].title)
		b[i].insert(1,a[i].id)
	return render_to_response('listall.html',{'sums':b})
	
def submitform(request):
	if request.method!="POST":
		return HttpResponse('Form could not be submitted!')
	try:
		idx=request.GET.get('id',-1)
		thisform=myform.objects.get(id=idx)
		a=json.loads(thisform.data)
		for i in range(a['count']):
			try:
				values(lform=thisform,fieldId='ele'+str(i),label=a['eles'][i]['label'],value=request.POST['ele'+str(i)]).save();
			except:
				if a['eles'][i]['type']=='checkbox':
					values(lform=thisform,fieldId='ele'+str(i),label=a['eles'][i]['label'],value="off").save();
				else:
					return HttpResponse("Error in saving form")
		return HttpResponse("Form Saved Successfully. Check all forms <a href='/svg/allform'>here</a>.")
	except:
		return HttpResponse("It seems you clicked a wrong link at %s"%i)
		
def reviewform(request):
	if request.method!='GET':
		return HttpResponse('It looks like you came to this page through a wrong link')
	idx=request.GET.get('id',-1)
	thisform=myform.objects.get(id=idx)
	data=json.loads(thisform.data)
	title=thisform.title
	count=data['count']
	eles=data['eles']
	ourdata=values.objects.filter(lform=thisform)
	if len(ourdata)==0:
		return HttpResponse("This form hasn't been filled by any user.<br> fill once to view result.")
	s="<div class='accor2'>"	
	for i in range(count):
		if eles[i]['type']=='checkbox':
			n_on=len(ourdata.filter(fieldId='ele'+str(i)).filter(value="on"))
			n_off=len(ourdata.filter(fieldId='ele'+str(i)).filter(value="off"))
			s+='<div class="accor2" style="height:300px;"><h3><a href="#">%s YES:%s NO:%s</a></h3><div height="220px;"><embed src="/svg/getbargraph.svg?a=%s&b=%s" width="900" height="170" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" ></div></div>'%(eles[i]['label'],n_on,n_off,n_on,n_off)
		elif eles[i]['type']=='radio':
			rcount=int(eles[i]['count'])
			qd={}
			s+="<div class='accor2' style='height:300px;'><h3><a href='#'>%s</a></h3><div style='height:220px;'>"%(eles[i]['label']+":")
			for k in eles[i]['eles']:
				qd[k]=len(ourdata.filter(fieldId='ele'+str(i)).filter(value=k))
				s+=" "+str(k)+":"+str(qd[k])
			s+='<br/><embed src="/svg/getpiechart.svg?a1=%s'%(qd[eles[i]['eles'][0]])
			for n in range(1,len(eles[i]['eles'])):
				s+='&a%s=%s'%(n+1,qd[eles[i]['eles'][n]])
			s+='" width="900" height="170" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" ></div></div>'
		else:
			s+="<div class='accor'><h3><a href='#'>%s</a></h3><div><ul>"%eles[i]['label']
			b=ourdata.filter(fieldId='ele'+str(i))
			for k in b:
				s+="<li>"+k.value
			s+="</ul></div></div>"
	s+="</div>"
	return render_to_response("review.html",{'s':s,'id':str(idx)})
	
def getbargraph(request):
	a=int(request.GET.get('a',0))
	b=int(request.GET.get('b',0))
	max=a
	if b>max:
		max=b
	a=a*90/max
	b=b*90/max
	sum=a+b;
	return render_to_response("barchart.svg",{'a1':a,'b1':b,'a2':100-a,'b2':100-b},mimetype="image/svg+xml")

def getpiechart(request):
	a=[]
	count=[1,1,1,1,1,1,1,1,1,1]
	for i in range(1,11):
		a.insert(i-1,int(request.GET.get('a'+str(i),0)))
	xcnt=10
	for x in reversed(a):
		if x==0:
			xcnt=xcnt-1
			count[xcnt]=0
		else:
			break
	print "count ",count
	maxi=max(a)
	for i in range(10):
		a[i]=a[i]*90/maxi
		print a[i]
	sumi=sum(a);
	(x,y)=([],[])
	t=[]
	for i in range(10):
		x.insert(i,50+50*cos(2*pi*sum(a[:i+1])/sumi))
		y.insert(i,50+50*sin(2*pi*sum(a[:i+1])/sumi))
	if (y[0]-50)*(50-100)>0:
		t.insert(0,1)
	else:
		t.insert(0,0)
	for i in range(1,10):
		if ((y[i]-y[i-1])*(50-x[i-1])-(50-y[i-1])*(x[i]-x[i-1]))>0:
			t.insert(i,1)
		else:
			t.insert(i,0)
	print x
	print y
	print t
	return render_to_response("piechart.svg",{'x':x,'y':y,'t':t,'count':count},mimetype="image/svg+xml")
	
def getxls(request):
	#response = HttpResponse(simple_report.writeReport(),mimetype='application/ms-excel')
	try:
		id=request.GET["id"]
		data=myform.objects.get(id=id)
		jstring=json.loads(data.data)
		wbook=xlwt.Workbook()
		asheet=wbook.add_sheet("she1")
		asheet.write(0, 1, data.title)
		for i in range(jstring['count']):
			asheet.write(1,i,jstring['eles'][i]['label'])
		vals=values.objects.filter(lform=id)
		for i in range(len(vals)/jstring['count']):
			for j in range(jstring['count']):
				asheet.write(2+i,j,vals[i*jstring['count']+j].value)
		response = HttpResponse(mimetype="application/ms-excel")
		wbook.save(response)
		return response
	except:
		return HttpResponse("Error generating file")
		
def getcsv(request):
	if 1:
		response = HttpResponse(mimetype='text/csv')
		writer = csv.writer(response)
		id=request.GET["id"]
		data=myform.objects.get(id=id)
		jstring=json.loads(data.data)
		writer.writerow([a['label'] for a in jstring['eles']])
		vals=values.objects.filter(lform=id)
		for i in range(len(vals)/jstring['count']):
			writer.writerow([a.value for a in vals[i*jstring['count']:(i+1)*jstring['count']]])
		return response
	else:
		return HttpResponse("Error Generating file")