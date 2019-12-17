### Build and deploy http://kieranhealy.org

### If you want to use this file as-is, then you
### need to change the variables below to your
### own SSH user, document root, etc.
### However, you will most likely also want to
### customize the various steps (e.g. the css target)
### so that it matches the details of your own
### setup.
### 
### Apart from hugo, you will also need rsync to deploy
### the site, and the java-based yuicompressor to
### minify the CSS, should you keep that step.


SSH_USER = khealy@kieranhealy.org
STAGING_USER = kjhealy@kjhealy.co
DOCUMENT_ROOT = ~/kieranhealy.org
STAGING_ROOT = ~/public/kjhealy.co/public_html
PUBLIC_DIR = public/

all: deploy

staging: site
	rsync -crzve 'ssh -p 22' $(PUBLIC_DIR) $(STAGING_USER):$(STAGING_ROOT)

server: compress css
	hugo server -ws .

deploy: compress site
	rsync -crzve 'ssh -p 22' $(PUBLIC_DIR) $(SSH_USER):$(DOCUMENT_ROOT)

compress: css
	java -jar ..\\apps\\yuicompressor-2.4.8.jar static\\css\\stylesheet.css -o static\\css\\stylesheet-min.css --charset utf-8

site: css .FORCE
	hugo 

css:
	del static\\css\\stylesheet.css
	type static\\css\\kube.css,static\\css\\syntax.css,static\\css\\bigfoot-default.css,static\\css\\scottdoy.css > static\\css\\stylesheet.css

clean:
	rm -rf public/

.FORCE:
