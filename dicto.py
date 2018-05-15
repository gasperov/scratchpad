# Hello World program in Python
import threading,json,glob

# Datastore declaration
class thread_dict(dict):
	def __init__(self, * p_arg, ** n_arg):
		dict.__init__(self, * p_arg, ** n_arg)
		self.lock = threading.Lock()
	
	def set_if_empty(self, key, value):
		with self.lock:
			if key not in self:
			    dict.__setitem__(self,key,value)
			    return True
		return False
	
	def set_if_eq(self, key, value, chk):
		with self.lock:
			if key not in self:
				return False
			val = dict.__getitem__(self, key)
			if val != chk:
				return False
			dict.__setitem__(self, key, value)
		return True
		
	def set_if_neq(self, key, value, chk):
		with self.lock:
			if key in self:
				val = dict.__getitem__(self, key)
				if val == chk:
					return False
			dict.__setitem__(self, key, value)
		return True
	
	def __setitem__(self, key, item):
		with self.lock:
			dict.__setitem__(self, key, item)
	
	def __getitem__(self, key):
		with self.lock:
			return dict.__getitem__(self, key)

datastore = thread_dict()

print "Hello World!\n"

if datastore.set_if_eq('no', 'v2', 'v1'):
    exit()

if not datastore.set_if_empty('no', 'v1'):
    exit()

if datastore.set_if_neq('no', 'v2', 'v1'):
    exit()
    
if not datastore.set_if_eq('no', 'v2', 'v1'):
    exit()

if datastore.set_if_empty('no', 'v1'):
    exit()

if not datastore.set_if_neq('no', 'v3', 'v3'):
    exit()
    
if not datastore.set_if_neq('vx', 'vx', 'vx'):
    exit()

print "val :" + datastore['no'] + "\n"

print "vals :" + json.dumps(datastore) + "\n"
