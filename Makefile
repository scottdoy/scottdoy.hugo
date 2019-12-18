### Build and deploy

all: deploy

server: compress css
	hugo server -ws . --buildDrafts 

deploy: compress site
	echo "The site has been rebuilt."
	echo "Ensure your changes have been committed to the source repo."
	echo "To push the compiled site public:"
	echo "- cd into the `public` dir"
	echo "- `git add .`"
	echo "- `git commit -m <commit-msg>`"
	echo "- `git push origin master`"

compress: css
	java -jar ..\\apps\\yuicompressor-2.4.8.jar static\\css\\stylesheet.css -o static\\css\\stylesheet-min.css --charset utf-8

site: css .FORCE
	hugo 

css:
	del static\\css\\stylesheet.css
	type static\\css\\kube.css,static\\css\\syntax.css,static\\css\\bigfoot-default.css,static\\css\\scottdoy.css > static\\css\\stylesheet.css

clean:

.FORCE:
