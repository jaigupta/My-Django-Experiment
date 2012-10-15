<html>
<head>
<title>Chat with strangers and find new Baotooniiiiizzzzz...!!</title>
<meta name="description" content ="Make new friends, chat with strangers, chat with hot guys">
<meta name="keywords" content="new friends, new,strangers, chat,chat with strangers, hot, cool, hot girls, boys, cool guys, talk to strangers, soulmate, girlfriend, boyfriend"></head>
<body>
<script type="text/javascript">
var submitAjax;
if (window.XMLHttpRequest)
{// code for IE7+, Firefox, Chrome, Opera, Safari
	submitAjax=new XMLHttpRequest();
}
else
{// code for IE6, IE5
	submitAjax=new ActiveXObject("Microsoft.XMLHTTP");
}
submitAjax.onreadystatechange=function()
{
	if(submitAjax.readyState==4 && submitAjax.status==200) {
		var s=submitAjax.responseXML.getElementsByTagName('status')[0].childNodes[0].nodeValue;
		if(s=='ok')
			top.location.href='http://apps.facebook.com/baatooniapp/chat/randomzz.jai';
		else{
			alert(s);
			document.getElementById("mybtn").style.display="";
			}
	}else if(submitAjax.readyState==4){
		document.body.innerHTML=submitAjax.responseText;
		document.getElementById("mybtn").style.display="";
	}
}
function check(){
	submitAjax.open('POST','/chat/startchat/',true);
	url='username='+document.getElementById('namefield').value+"&code={{code}}";
	submitAjax.send(url);
	document.getElementById("mybtn").style.display="none";
	return false;
}
</script>
<p style=" text-align: center;"><img src="/site_media/main_banner.gif" width="750"/>
{%if error %}
<p style=" text-align: center;">{{error}}{% endif %}
<form onsubmit='return check();'><p style=" text-align: center;"><font size=3 color="#0ab2f8">Welcome to the world of BAATOONIs<br><h1 style=" text-align: center;"><font size=2 color="#FF9234"></b></b>Talk to Strangers<br>
Enter Your Nick and get connected with the Baaaatoooniizzzzzzz....<br>Nick:<input type="text" id='namefield' value="" size=10 maxlength=10 name='username' align="center"><br>
<input type="submit" id="mybtn" value="Login"></p>
</form>
</body>
</html>