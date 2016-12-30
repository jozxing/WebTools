var obj =  {
	'/index.html': '0',
	'/tool-nmap.html': '1',
	'/web-finger.html': '2',
	'/domain-info.html': '3',
	'/common-exp.html': '4',
	'/second-domain.html': '5',
	'/web-dirs.html': '6',
	'/tool-sqlmap.html' : '7',
	'/api-md5.html' : '8',
	'/tool-hydra.html' : '9'
} 
var path = window.location.pathname
var index = parseInt(obj[path])	
$('#main-menu a')[index].className = "active-menu"
