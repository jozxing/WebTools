import os 
import logging 
import subprocess 
  
log = logging.getLogger("Core.Analysis.Processing") 
  
INTERPRETER = "/usr/bin/python"
  
  
if not os.path.exists(INTERPRETER): 
  log.error("Cannot find INTERPRETER at path \"%s\"." % INTERPRETER) 
    
processor = "/subDomainsBrute.py"
  
pargs = [INTERPRETER, processor] 
pargs.extend(["--input=inputMd5s"]) 
subprocess.Popen(pargs) 