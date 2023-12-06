.PHONY: quick

quick:
	git add .
	git commit -m "$(msg)"
	git push


fast:
	git add .
	git commit -m "fast commit"
	git push

temp:
	python source/temp.py