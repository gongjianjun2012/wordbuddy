var userAgent = navigator.userAgent.toLowerCase();
var is_opera  = (userAgent.indexOf('opera') != -1);
var is_saf    = ((userAgent.indexOf('applewebkit') != -1) || (navigator.vendor == "Apple Computer, Inc."));
var is_webtv  = (userAgent.indexOf('webtv') != -1);
var is_ie     = ((userAgent.indexOf('msie') != -1) && (!is_opera) && (!is_saf) && (!is_webtv));
var is_firefox  = ((typeof window.sidebar == "object") && (typeof window.sidebar.addPanel == "function"));
	
function addSysFavorite(url,sitename) {
	var url = url;
	var sitename = sitename;
	if (is_ie)
	{
		window.external.addFavorite(url,sitename);
	}
	else if (is_firefox)
	{
		window.sidebar.addPanel(sitename, url , "");
	}
}

function audio(a){
	document.write( '<span style="z-index:1000;"><object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0" width="17" height="14" align="absmiddle">' +'<param name="allowScriptAccess" value="sameDomain" />' +'<param name="movie" value="/new_sound5.swf" />' +'<param name="loop" value="false" />' +'<param name="menu" value="true" />' +'<param name="quality" value="high" />' +'<param name="FlashVars" value="f=' + a + '"><param name="wmode" value="transparent">' +'<embed src="/new_sound5.swf" loop="false" menu="true" quality="high" bgcolor="#ffffff" width="17" height="14" align="absmiddle" allowScriptAccess="sameDomain" wmode="transparent" FlashVars="f=' + a + '" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" />' +'</object></span>');
}


function getFlashObject(movieName)
{
	if (window.document[movieName])
	{
		return window.document[movieName];
	}
	if (navigator.appName.indexOf("Microsoft Internet")==-1)
	{
		if (document.embeds && document.embeds[movieName])
			return document.embeds[movieName];
	}
	else // if (navigator.appName.indexOf("Microsoft Internet")!=-1)
	{
		return document.getElementById(movieName);
	}
}

function asplay(c){
	var asound = getFlashObject("asound");
	if(asound){
		asound.SetVariable("f",c);
		asound.GotoFrame(1);
                
	}
}

function asstop(){
	var asound = getFlashObject("asound");
	if(asound){
		asound.GotoFrame(3);
	}
}
