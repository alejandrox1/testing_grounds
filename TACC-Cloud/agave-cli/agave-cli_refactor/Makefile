format: 
	yapf -i --style=google agave.py test_agave.py tenants.py
	pylint --rcfile=rcfile agave.py || exit 0 
	pylint --rcfile=rcfile tenants.py || exit 0
