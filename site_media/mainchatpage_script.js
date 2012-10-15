var framehiddenAjax;
var sub1Ajax;
var frame2Ajax;
var formno=0;
var s="";
var login=0;
var cno=-1;
var lno=0;
var authstatus=2;
function Invite()
{
FB.ui({method: 'apprequests', message: 'Hey Check this app. I found new friends here.', data: 'Meet Strange Friends at Baatooni.'});
}
function poster()
{
    FB.ui(
   {
     method: 'feed',
     name: 'The Baatooni App',
     link: 'http://apps.facebook.com/baatooniapp',
     picture: 'http://www.baatooni.com/site_media/logo.jpeg',
     caption: 'Baatooni app',
     description: 'This is the baatooni app designed to connect anonymous people round the world through chat.',
     message: 'Hey, I made great friends here. Check this out.'
   },
   function(response) {
     if (response && response.post_id) {
       //alert('Post was published.');
     } else {
       //alert('Post was not published.');
     }
   }
 );
}
function correct(s)
{
	return s.replace(/{nl}/g,"<br>... ").replace(/{amp}/g,"&").replace(/{lt}/g,"<").replace(/{gt}/g,">").replace(/{r}/g,"<font color=RED>").replace(/{B}/g,"<font color=BLACK>").replace(/{b}/g,"<font color=BLUE>").replace(/{g}/g,"<font color=GREEN>").replace(/{o}/g,"<font color=ORANGE>").replace(/{y}/g,"<font color=YELLOW>").replace(/:\)/,"<img src='/site_media/smileys/happy.png'/>").replace(/B\)/,"<img src='/site_media/smileys/cool.png'/>").replace(/:\(/,"<img src='/site_media/smileys/sad.png'/>").replace(/o\)/,"<img src='/site_media/smileys/angel.png'/>").replace(/:x/,"<img src='/site_media/smileys/furious.png'/>");
}
function checkavail()
{
	framehiddenAjax.open("GET","/chat/search_user/",true);
	framehiddenAjax.send();
}
function getNewChat()
{
	framehiddenAjax.open("GET","/chat/hidden/?chatno="+cno,true);
	framehiddenAjax.send();
}
function startLoader()
{
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
		framehiddenAjax=new XMLHttpRequest();
		sub1Ajax=new XMLHttpRequest();
		frame2Ajax=new XMLHttpRequest();
	}
	else
	{// code for IE6, IE5
		framehiddenAjax=new ActiveXObject("Microsoft.XMLHTTP");
		sub1Ajax=new ActiveXObject("Microsoft.XMLHTTP");
		frame2Ajax=new ActiveXObject("Microsoft.XMLHTTP");
	}
	framehiddenAjax.onreadystatechange=function()
	{
	
		if(framehiddenAjax.readyState==4 && framehiddenAjax.status==200)
		{
			if(framehiddenAjax.responseXML==null || framehiddenAjax.responseText.length<=1)
			{
				if(login==0)
					setTimeout("checkavail()",1000);
			}
			else{
				var s="";
				if(login==0)
				{
					if(framehiddenAjax.responseXML.getElementsByTagName('chix')[0]!=null)
					{
						if(framehiddenAjax.responseXML.getElementsByTagName('chix')[0].childNodes[0].nodeValue=="y")
						{	
							cno=0;
							login=1;
							document.getElementById("chatender").style.display="";
							document.getElementById("refresher").style.display="";
							setTimeout("checks()",1000);
							document.getElementById("line").innerHTML=(framehiddenAjax.responseXML.getElementsByTagName('you')[0].childNodes[0].nodeValue+
							" and "+framehiddenAjax.responseXML.getElementsByTagName('stranger')[0].childNodes[0].nodeValue+
							" have been connected");
							document.getElementById('send_btn').innerHTML="<form action='javascript:void(0)'><input type='text' class='inputtext' id='detailss' maxlength=5000 size=81 onfocus='focuser()' onblur='unfocuser()' / ><input type='submit' value='SEND..' onclick='submitf()' style='background:#6D86B7;'></form>";
							document.getElementById('line').innerHTML+='<br>ADMIN: You have been connected to a Random Stranger.';
							alert('Connection Established.')
						}
						else{
							setTimeout("checkavail()",1000);
						}
					}
				}
				while(framehiddenAjax.responseXML.getElementsByTagName('chit'+cno)[0]!=null)
				{
					s=framehiddenAjax.responseXML.getElementsByTagName('chit'+cno)[0].childNodes[0].nodeValue;
					s=correct(s);
					document.getElementById('line').innerHTML+="<br>"+s;
					cno++;
					document.getElementById('temp').innerHTML=" ";
					if(document.title=="Baatooni...")
					{
						document.title="New Chat..";a=setTimeout('aniTitle()',1000);
					}
					//window.location.hash="bottom";
					document.getElementById("detailss").focus();
					document.getElementById("chatpart").scrollTop = document.getElementById("chatpart").offsetHeight;
				}
				if(login==1){
					try{
						if(framehiddenAjax.responseXML.getElementsByTagName('chitend')[0].childNodes[0].nodeValue!="")
						{
							document.getElementById('send_btn').innerHTML="<div align='center'><font color=LIGHTGRAY> Disconnected</div></font>";
							document.getElementById('line').innerHTML+="<br>Chat Finished...<br><a href='#' onclick='logagain()'><font color=BLUE size=2><u>Click here to connect again..</u></font></a>";
							document.title="Baatooni..";
							cno=-1;
							login=-1;
						}
					}
					catch(err)
					{
					}
					setTimeout("getNewChat()",1000);
				}
			}
		}
		else if(framehiddenAjax.readyState==4){
			//document.body.innerHTML=framehiddenAjax.responseText;
			if(login==1)
				setTimeout("getNewChat()",1000);
			else
				setTimeout("checkavail()",1000);
		}
	}
	sub1Ajax.onreadystatechange=function()
	{
		setTimeout('checks()',1000);
	}
	frame2Ajax.onreadystatechange=function()
	{
		if(frame2Ajax.readyState==4 && frame2Ajax.status==200)
		{
			if(authstatus==0){
				frame2Ajax.open('GET','http://graph.facebook.com/me?access_token='+code,true);
				frame2Ajax.send();
				authstatus=1;
			}
			if(authstatus==1){
				frame2Ajax.open('POST','/chat/savedet',true)
				frame2Ajax.send("details="+frame2Ajax.responseText);
				authstatus=2;
			}
			if(authstatus==2){
				document.getElementById('reviel').style.display="";
				alert(frame2Ajax.responseText);
			}
		}else if(frame2Ajax.readyState==4){
		//if(authstatus<=2){
			//	frame2Ajax.open('GET','http://graph.facebook.com/me?access_token='+code,true);
				//frame2Ajax.send();
	//		}
			//document.body.innerHTML=frame2Ajax.responseText;
		}
	}
	setTimeout('checkavail()',1000);
	frame2Ajax.open("POST","https://graph.facebook.com/me/feed",true);
	//frame2Ajax.send('access_token='+code+"&message=http://apps.facebook.com/"+appname);
}
function tryreviel(){
	frame2Ajax.open('GET',"/chat/reviel/",true);
	frame2Ajax.send();
}
function endc()
{
	framehiddenAjax.open("GET","/chat/endthischat/",true);
	framehiddenAjax.send();
	cno=-1;login=0;
	document.getElementById("chatender").style.display="none";
	document.getElementById("refresher").style.display="none";
	document.getElementById('line').innerHTML+="<br>Chat Finished...<br><a class='l' href='#' onclick='logagain()'><font color=BLUE size=2><u>Click here to connect again..</u></font></a>";
}
function submitf()
{
	if(document.getElementById('detailss').value!=""){
	if(s!="")s+="{nl}";
	s+=document.getElementById('detailss').value.replace(/&/g,"{amp}");
	document.getElementById('temp').innerHTML+="<font color=RED>"+myname+": <font color=BLACK>"+correct(document.getElementById('detailss').value)+"<br>";
	document.getElementById('detailss').value="";
	document.getElementById('detailss').focus();
	//window.location.hash="bottom";
	document.getElementById("detailss").focus();
	document.getElementById("chatpart").scrollTop = document.getElementById("chatpart").offsetHeight;
	}
}
function checks()
{
	if(login==1){
	if(s!="")
	{
		sub1Ajax.open("GET","/chat/subm/?details="+s,true);
		sub1Ajax.send();
		s="";
	}
	else
	setTimeout('checks()',1000);
	}
}
function focuser()
{
	document.title="Baatooni";
}
function unfocuser()
{
	document.title="Baatooni...";
}
function logagain()
{
	login=0;
	document.getElementById('line').innerHTML="Waiting for user to connect.....";
	checkavail();
}
function unlo()
{
	window.open('/chat/logout');
}
function aniTitle()
{
	if(document.title=="New Chat..")
	{document.title="on Baatooni..";a=setTimeout('aniTitle()',1000);}
	else if(document.title=="on Baatooni..")
	{document.title="New Chat..";a=setTimeout('aniTitle()',1000);}
}