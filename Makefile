### Build and deploy

### Notes on the "citations" target:
### - The file "data/scottdoy.json" was exported from Zotero.
### - You may wish to manually delete all pub files in 'content/publications' before running.

all: deploy

server: compress citations
	hugo server -ws . --buildDrafts 

deploy: compress site
	echo "The site has been rebuilt."
	echo "Ensure your changes have been committed to the source repo."
	echo "To push the compiled site public:"
	echo "- cd into the `public` dir"
	echo "- `git add .`"
	echo "- `git commit -m <commit-msg>`"
	echo "- `git push origin master`"

citations: data\\scottdoy.json
	python jsonparser.py --input data\\scottdoy.json --output_dir content\\publications\\

compress: css
	java -jar ..\\apps\\yuicompressor-2.4.8.jar static\\css\\stylesheet.css -o static\\css\\stylesheet-min.css --charset utf-8

site: css 
	hugo 

css:
	del static\\css\\stylesheet.css
	type static\\css\\kube.css, \
	    static\\css\\nightowl-pygments-v0.0.1.css, \
		static\\css\\bigfoot-default.css, \
		static\\css\\scottdoy.css \
		> static\\css\\stylesheet.css

clean:

.FORCE:
