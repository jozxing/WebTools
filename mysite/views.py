from django.shortcuts import render_to_response  
import subprocess 
#return render_to_response('current_datetime.html', {'current_date': now})
def index(request):
    return render_to_response('index.html')

def footer(request):
    return render_to_response('footer.html')

def header(request):
    return render_to_response('header.html')

def oheader(request):
    return render_to_response('other-header.html')

def leftlist(request):
    return render_to_response('leftlist.html')

def namp(request):
    return render_to_response('tool-nmap.html')

def finger(request):
    return render_to_response('web-finger.html')

def domain(request):
    return render_to_response('domain-info.html')

def exp(request):
    return render_to_response('common-exp.html')

def sdomain(request):
    res = subprocess.Popen('whoami>./log.txt',creationflags=0,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True,universal_newlines=True) 
    f=open("log.txt")
    line=f.readline()
    while line:
        return render_to_response('second-domain.html',{'hello':line})

def dirs(request):
    return render_to_response('web-dirs.html')

def sqlmap(request):
    return render_to_response('tool-sqlmap.html')

def md5(request):
    return render_to_response('api-md5.html')

def hydra(request):
    return render_to_response('tool-hydra.html')

