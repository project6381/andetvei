import uuid


def machine_id:
	# If uuid.getnode() fails to get a valid MAC-adress it returns a random number. 
	# The function is run twice to check for this.
	id = uuid.getnode() 
	if id == uuid.getnode():
		return id
	else raise OSError('machine_id: No MAC-address found')
