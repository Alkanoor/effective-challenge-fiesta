REPO=git@github.com:Alkanoor/effective-challenge-fiesta.git

init:
	git config --global user.email "Alkanoor@github.com"
	git init
	git stage --all
	git commit -m "first commit"
	git remote add origin $(REPO)
	git push -u origin master

init-existing:
	git init
	git stage --all
	git commit -m "first commit"
	git pull origin master

push:
	git stage --all
	git commit -m "répétition"
	git push

pull:
	git stash
	git pull origin master
