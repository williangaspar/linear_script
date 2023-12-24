setup: dependencies.txt variables
	pip install -r dependencies.txt

variables: files.txt
	touch variables.data


