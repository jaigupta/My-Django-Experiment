var login=0;
var cno=-1;
var lno=0;
function logagain()
{
	window.parent.document.getElementById('framehidden').contentDocument.location="/chat/search_user2/";
	document.getElementById('line').innerHTML="Waiting for user.....";
}
function slowscroll()
{
	var s="";
	window.scrollBy(0,20);
	if(window.parent.document.getElementById('framehidden')!=null && window.parent.document.getElementById('framehidden').contentDocument!=null && window.parent.document.getElementById('framehidden').contentDocument.location!=null)
	{
		if(cno==-1)
		{
			if(window.parent.document.getElementById('framehidden').contentDocument.getElementById('chix')!=null)
			{	
				if(window.parent.document.getElementById('framehidden').contentDocument.getElementById('chix').innerHTML=="y")
				{	cno=0;login=1;}
				else{
				if(lno==0)
				window.parent.document.getElementById('framehidden').contentDocument.location="/chat/search_user/";
				}
			}
		}
		while(window.parent.document.getElementById('framehidden').contentDocument.getElementById('chit'+cno)!=null)
		{
			if(cno==0){document.getElementById('line').innerHTML="";
			window.parent.document.getElementById('send_btn').innerHTML="<form action='javascript:void(0)'><input type='text' id='detailss' maxlength=5000 size=75 onfocus='focuser()' onblur='unfocuser()' / ><input type='submit' value='SEND..' onclick='submitf()'></form>";}
			s=window.parent.document.getElementById('framehidden').contentDocument.getElementById('chit'+cno).innerHTML;
			s=s.replace(/{e}/g,"<br>... ").replace(/{amp}/g,"&").replace(/{r}/g,"<font color=RED>").replace(/{B}/g,"<font color=BLACK>").replace(/{b}/g,"<font color=BLUE>").replace(/{g}/g,"<font color=GREEN>").replace(/{o}/g,"<font color=ORANGE>").replace(/{y}/g,"<font color=YELLOW>");
			document.getElementById('line').innerHTML+="<font size=2>"+s;
			cno++;
			window.parent.document.getElementById('frame2').contentDocument.getElementById('temp').innerHTML=" ";
			if(window.parent.document.title=="Baatooni...")
			{	window.parent.document.title="New Chat..";a=setTimeout('aniTitle()',1000);}
		}
		if(login==1){
		if(window.parent.document.getElementById('framehidden').contentDocument.getElementById('chitend')==null||window.parent.document.getElementById('framehidden').contentDocument.getElementById('chitend')=="")
		{
			if(lno==0)
			window.parent.document.getElementById('framehidden').contentDocument.location="/chat/hidden/?chatno="+cno;
		}
		else
			{
		window.parent.document.getElementById('send_btn').innerHTML="<div align='center'><font color=LIGHTGRAY> Disconnected</div></font>";
		document.getElementById('line').innerHTML+="Chat Finished...<br><a ONCLICK='logagain()'><font color=BLUE size=2><u>Click here to connect again..</u></font></a>";login=0;
		window.parent.document.title=="Baatooni.."
		cno=-1;
		lno=0;
		}}
	}
		lno=(lno+1)%4;
		t=setTimeout('slowscroll()',500);
}
function unlo()
{
	window.open('/chat/logout');
}
function aniTitle()
{
	if(window.parent.document.title=="New Chat..")
	{window.parent.document.title="on Baatooni..";a=setTimeout('aniTitle()',1000);}
	else if(window.parent.document.title=="on Baatooni..")
	{window.parent.document.title="New Chat..";a=setTimeout('aniTitle()',1000);}
}
