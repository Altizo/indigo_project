var overlayMenuStatus = 'list';
function subMenuScript(){
		var subMenu = $('ul.subMenu');
		var listMenu = $('li.listMenu');
		var serviceLink = $('#serviceOverlayMenu');
		subMenu.toggle('slow');
		listMenu.toggle('slow');
	};
	

	function blockItem (){
		var elems=document.getElementsByClassName('overlayMenu');
		for(var i=0; i<elems.length; i++)elems[i].style.display='block';
	}
	function noneItem (){
		var elems=document.getElementsByClassName('overlayMenu');
		for(var i=0; i<elems.length; i++)elems[i].style.display='none';
	}

	function openNav() {
		status = document.getElementById("myNav").style.width = "100%";
		if (status) {setTimeout(blockItem(), 1000)};
	}

	function closeNav() {
	    document.getElementById("myNav").style.width = "0%";
	    setTimeout(noneItem(), 700);
		
}		