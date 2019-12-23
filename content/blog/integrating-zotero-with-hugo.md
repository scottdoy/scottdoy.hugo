---
title: "Integrating Zotero With Hugo"
date: 2019-12-18T10:53:34-05:00
draft: false
categories: [webdev,citations]
footnotes: false
htmlwidgets: false
d3: false
mathjax: true
---

In this article, I talk about my solution to the problem of citation management
in [Hugo](https://gohugo.io). I use a combination of [Zotero](http://zotero.org)
and Python to organize my citation list for the [Publications](/publications)
area of this site. I'll talk about Zotero management, JSON importing, and pesky
datestrings.

<!--more-->

## Background

### Hugo Static Site Generation

In setting up this site -- or anything, really -- I often get hit with a
version of the [Pareto
principle](https://en.wikipedia.org/wiki/Pareto_principle): off-the-shelf
solutions give me about 80% of what I want, while the final 20% takes the
most amount of time. This article is about part of the 20%: Managing my list of [Publications](/publications).

[Hugo](https://gohugo.io) is a static site generator. Like most generators,
there are two halves to this setup: the source code and the compiled site. When
you run the `hugo` command, the program looks at all your source files and
stitches them together in such a way that a fully self-contained website is
generated in your `public` folder. How these files get stitched is determined by
the [content management system](https://gohugo.io/content-management/) and by
the [theme](https://themes.gohugo.io/) you're using. 

The theme I'm using is ~~stolen from~~ based on [Kieran Healy](kieranhealy.org)
and [Greg Restall](https://consequently.org/), and is a fantastic setup for
academic users who want to showcase their work as well as their blogging.
There's just one drawback: There doesn't seem to be a way to easily manage a
publication list. See, most of the content (like this blog post) is organized
into separate markdown text files. The way my current theme is set up, I'd have
to create a new markdown file with header information every time I publish a
paper. I don't publish nearly as often as I should, but I still didn't want to
have to maintain a set of markdown files separate from my citation manager. If
there's one thing I've learned, it's that maintaining two separate sets of data
for the same thing is a recipe for disaster. 

### Zotero for Citation Management

I use [Zotero](http://zotero.org) for citation management, and it works great. I
won't go into detail on how it works here (subject of another blog post!) but it
does what I want it to do. I've set up a collection to house all of the papers
I'm an author on, so that when it comes time to update my CV, I can just export
a nicely formatted bibliography. I also use the [Better
BibTex (BBT)](https://retorque.re/zotero-better-bibtex/) extension, which gives you
greater control over how your citations are exported. In fact, it provides a
number of different formats for export, including
[JSON](https://www.json.org/json-en.html).

# The Problem: Data Export and Conversion

So now we have the problem: How to maintain my citations in Zotero and then have Hugo create a nicely-formatted publications page, without having to hand-write a bunch of markdown files?

### Exporting from Zotero

First, the problem of export from Zotero was solved right away: Not only does
BBT allow you to export stuff in [various structured
formats](https://retorque.re/zotero-better-bibtex/exporting/), you can also
check an option to [automatically
re-export](https://retorque.re/zotero-better-bibtex/exporting/auto/) any time
the citation lists for a collection changes. 

To do this, first make sure you have both Zotero and BBT installed, and you've
created a collection into which you've saved some citations. I'll go over Zotero
usage in another post, but you should have something like this (This is just a
random selection of recently-added papers that I haven't read yet):

{{% figure src="imgs/zotero-collections.png" alt="Zotero Collections and Citations" caption="Zotero Collections and Citations" %}}

Now right-click on your collection and select "Export Collection":

{{% figure src="imgs/zotero-collection-export.png" alt="Exporting Collection" caption="Exporting Collection" %}}

You'll get the following window pop up. If you have BBT installed, you should
get a drop-down menu with a whole lot of options inside for different export
formats. I'm using "BetterBibTeX JSON" for the purposes of this article, and
it's what I used to create my parser (which I'll explain in a minute).

Also take note of the third checkbox, "Keep updated" -- this is the option I
mentioned above, where you can tell Zotero to automatically re-export your
collection every time it changes. I'm leaving that off for now since this is a
demonstration, but you can turn it on so you don't have to manually export every
time you change something in your citations list.

{{% figure src="imgs/zotero-collection-export-options.png" alt="Export Format Options" caption="Export Format Options" %}}

Export the file to somewhere Hugo can find it -- I recommend keeping it under
your project directory, in a `data` folder. 

Let's take a look at part of the exported file. The first keys are `"config"`
and `"collections"`; the former is a long list of your Zotero options, and the
second is a list of any collections that might be nested inside the one you're
exporting. We won't be needing those for our purposes. The third key, `"items"`,
is where the action is -- it's a list, and each item in the list is one of your
citations. I'm showing the data for just the first item in the `"items"` list,
but just be aware that there's one of these per citation:

{{< highlight json >}}{
    "version": 2924,
    "itemType": "journalArticle",
    "url": "https://www.nature.com/articles/s41467-019-13057-w",
    "rights": "2019 The Author(s)",
    "volume": "10",
    "issue": "1",
    "pages": "1-12",
    "publicationTitle": "Nature Communications",
    "ISSN": "2041-1723",
    "date": "2019-11-07",
    "journalAbbreviation": "Nat Commun",
    "DOI": "10.1038/s41467-019-13057-w",
    "accessDate": "2019-11-17T16:27:25Z",
    "libraryCatalog": "www.nature.com",
    "language": "en",
    "abstractNote": "Anatomical brain atlases elucidate the anatomical and functional organisation across species but different atlases have conflicting anatomical border and 3D coordinates. The authors integrated two atlases into a unified and highly segmented anatomical labelling system of the mouse brain.",
    "title": "Enhanced and unified anatomical labeling for a common mouse brain atlas",
    "creators": [
    {
        "firstName": "Uree",
        "lastName": "Chon",
        "creatorType": "author"
    },
    {
        "firstName": "Daniel J.",
        "lastName": "Vanselow",
        "creatorType": "author"
    },
    {
        "firstName": "Keith C.",
        "lastName": "Cheng",
        "creatorType": "author"
    },
    {
        "firstName": "Yongsoo",
        "lastName": "Kim",
        "creatorType": "author"
    }
    ],
    "tags": [],
    "collections": [
    "DNMWB5JH",
    "MFFEZV5N"
    ],
    "relations": [],
    "dateAdded": "2019-11-17T16:27:25Z",
    "dateModified": "2019-11-17T16:27:25Z",
    "uri": "...",
    "attachments": [
    {
        "itemType": "attachment",
        "title": "Chon et al_2019_Enhanced and unified anatomical labeling for a common mouse brain atlas.pdf",
        "tags": [],
        "relations": [],
        "dateAdded": "2019-11-17T16:27:30Z",
        "dateModified": "2019-11-17T16:27:31Z",
        "uri": "...",
        "path": "..."
    },
    {
        "itemType": "attachment",
        "title": "Snapshot",
        "tags": [],
        "relations": [],
        "dateAdded": "2019-11-17T16:27:35Z",
        "dateModified": "2019-11-17T16:27:35Z",
        "uri": "...",
        "path": "..."
    }
    ],
    "notes": [],
    "itemID": 5242,
    "key": "ICXU6PQ2",
    "citekey": "chon_enhanced_2019",
    "citationKey": "chon_enhanced_2019",
    "libraryID": 1
},
{{< /highlight >}}

That's a **lot** of data. Note that all of these fields are populated by Zotero
when the item is added to your library, so if you're using the browser plug-in
to pull papers directly from publishers' sites, you may get some weird results
depending on how they've formatted their entries. 

Neat! So now I have a structured data file on disk containing all of my
citations.

Now, how to get it into Hugo? 

### Requirements for Import into Hugo

For details on how content is managed in Hugo, I'll refer you to the [official
documentation](https://gohugo.io/getting-started/directory-structure/); however,
at a minimum, I needed the following:

- A `layouts/section/publications.html` page that will parse the data file and
  display a list for each type of publication (`conference` or `journal` are the
  two main types).
- A `layouts/publications/single.html` page template that would display the
  title, citation text, DOI, and abstract for the paper.
- A `content/publications/_index.md` file that would allow the "publications"
  section to be populated.

In the traditional template, the `content/publications/` directory would also
contain a single markdown file for each published work, which would then be
parsed, grouped, and displayed by the layout pages. Hugo takes advantage of the
header data in each markdown file to organize its content, so you can do things
like [group items](https://gohugo.io/templates/lists#group-content) according to
their dates or types (journal, conference, etc.).

However, we don't have that -- we have a single exported data file from Zotero. 

### Solution 1: Using Data Templates to Read and Parse JSON

Hugo has support for [data
templates](https://gohugo.io/templates/data-templates/): These are shortcodes
that will pull in data from an external source and allow you to use that data in
generating a page on the site. If your data is formatted as YAML, TOML, or JSON,
you can create a `map` in the `.Site.Data` variable and iterate that. There's
even functionality for pulling data from a URL like a REST API, which is super
cool.

You can put your data files into a `data` dir in your site's project root and then they'll be accessible through the `$.Site.Data` variable.

For example, the following will iterate through all the items in a JSON file
named `scottdoy.json` located in the site root's `data` directory, provided the
item has a `"itemType"` key which equals `"conference"`:

{{< highlight html >}}<h2>Conference Papers and Presentations</h2> 
<ul>
    {{ range sort (where $.Site.Data.scottdoy.items "itemType" "conference") "date" "desc"}}
    <li>
        {{ range .creators }}
          {{ .lastName }}, {{ slicestr .firstName 0 1 }}., 
        {{ end }}
        "{{ .title }}," <em>{{ .publicationTitle }}</em>, ({{ dateFormat "2006" .date }})
    </li>
    {{ end }}
</ul>
{{< /highlight >}}

This works well if all you want to do is print out a list. If that's what you
need, then you're good to go!

However, there are a few restrictions:

- **Date sorting is Fragile:** Unless you enter all your citations into Zotero
  by hand (*ugh*), you probably have a mix of date formats (`yyyy`,
  `mm/dd/yyyy`, `Monthname dd, yyyy`, etc.). Hugo requires all dates to be in
  `yyyy-mm-dd` format, so your date sorting may not work.
- **Functionality is Limited:** This will simply print a block for each of the
  items in the JSON file that it encounters. With the
  one-markdown-file-per-citation approach, Hugo will construct a separate page
  for each citation that you can view by clicking on a list item. It also
  enables grouping by date, among other things. To be able to do that with this
  setup, you'd need a more complex processing setup than what I've attempted.

### Solution 2: Custom JSON-to-MD-Files Parsing

In this approach, which is what I'm currently doing, I wrote a Python parser
script which will ingest a JSON file and barf out a ton of markdown files in the
format that Hugo expects for its content files. If you want to see my attempt, it's the file `jsonparser.py` located in [my site's source directory](https://github.com/scottdoy/scottdoy.hugo). I'll go through the important bits in the rest of this article. 

The goal: Given a JSON file on disk, read it in, iterate through all citations,
pull out the relevant information for each citation, and create a markdown file
for each one that is formatted with the correct YAML header data. 

I like this solution because it allows us complete control over how the input
data is processed, and we can offload all the tricky bits of Hugo's site
creation engine -- we only need to make sure that our markdown files are
formatted correctly.

First, we load the JSON file (in my script, I use input arguments to determine
`json_path`). We aren't interested in the Zotero `"config"` tag, and we're
assuming there are no collections within the one we exported, so we can just
pull out the `"items"` tag which contains our citations. Then for each item, we
call `parse_citation_item()`, which is responsible for returning `file_name`, a
unique markdown filename for the item, and `file_string`, which is a long string
containing the contents to write to the file. Finally, we write the file. Note
that when we open the file, have to use the `codecs` package and pass in the
`'utf-8-sig'` option; this allows us to get around Unicode symbols like \[\mu\]
which often appear in the text of abstracts or titles.

{{< highlight python >}}with open(json_path, 'rb') as json_file:
    try:
        citationdata = json.load(json_file)
    except:
        raise Exception("An error occurred with loading " \
        "the JSON file. Probably weird quotation marks in one of the citations.")

    items = citationdata['items']

    for item in items:
        file_name, file_string = parse_citation_item(item)

        with codecs.open(os.path.join(output_dir, file_name), 'w', 'utf-8-sig') as output:
            output.write(file_string)
{{< /highlight >}}

With `parse_citation_item()`, we have control over how the content of the
markdown file is created. This means we can construct citation layout, authors,
and datestrings however we need (more on that last one in a sec).

The function is reproduced in its entirety below. First we use the `"citekey"`
tag to create a filename based off the bibtex key created by BBT. This way we
can be *reasonably* certain that the name is unique. Next we run a quick check
through all the keys that we're going to use to populate the YAML header data.
If the key doesn't exist, we place a blank space in as a placeholder -- some of
which we will replace later.

Next we run through and edit each tag so it's in the right format. This should
be pretty straightforward: most of what I'm doing is figuring out how to format
each of the pieces of the JSON that is required to populate the YAML header
information of a markdown file that Hugo can then use to perform its magic. One
exception is the `fix_datetime()` function which I'll discuss below.

Finally, we stitch everything together in one big string that represents the
contents we're going to write to the markdown file. For simplicity we're using
the `{key:s}` placeholders for python strings, and passing `(**item)` to the
format function. 

{{< highlight python >}}def parse_citation_item(item):
    """Parse the JSON-formatted citation"""
    file_name = item['citekey']+'.md'

    req_keys = ['title', 'itemType', 'publicationTitle', 'volume', 'issue', 'date', \
     'DOI', 'abstractNote']

    for req_key in req_keys:
        if req_key not in item.keys():
            item[req_key] = "&nbsp;"

    # Fix annoying inconsistencies with title capitalization
    item['title'] = item['title'].title()

    # Fix for missing DOIs
    if item['DOI'] == "&nbsp;":
        item['DOI'] = "none"

    # Change the item type to be appropriate for Hugo
    if item['itemType'] == 'conferencePaper':
        item['itemType'] = 'conference'
    elif item['itemType'] == 'journalArticle':
        item['itemType'] = 'journal'

    # Create a string list of authors
    authors = []
    author_list = item['creators']
    for author in author_list:
        authors.append('{}, {}.'.format(author['lastName'], author['firstName'][0]))
    item['authors'] = ', '.join(authors)

    # fix the date with our custom date parser! FANCY
    item['date'] = fix_datestring(item['date'])

    # Create a custom citation key that formats based on what data is available
    citestr = ''
    if not item['title'] == "&nbsp;":
        citestr = citestr + item['title'].title()
    if not item['publicationTitle'] == "&nbsp;":
        citestr = citestr + ', <em>' + item['publicationTitle'] + '</em>'
    if not item['volume'] == "&nbsp;":
        citestr = citestr + ', <b>' + item['volume'] + '</b>'
    if not item['issue'] == "&nbsp;":
        citestr = citestr + '(' + item['issue'] + ')'
    if not item['date'] == "&nbsp;":
        # Assume the date has already been fixed above
        # So the first four characters means just the year
        citestr = citestr + ', ' + item['date'][0:4]
        
    item['citestr'] = citestr

    # Construct MD file content based on the type of item we have
    file_content = """---
title: "{title:s}"
author: {authors:s}
status: Published
type: {itemType:s}
citation: "{citestr:s}"
comments: no
doi: {DOI:s}
date: {date:s}
publishdate: {date:s}
---

{abstractNote:s}
""".format(**item)

    return file_name, file_content
{{< /highlight >}}

One particularly tricky bit was the creation of the `fix_datestring()` function.
In Zotero, `"date"` is the catchall field for publication date. Some
publications only have the year, some have `mm/dd/yyyy` syntax while others have
`month dd, yyyy` (where the month is written out), and so on. Meanwhile, Hugo
expects dates to be recorded in `yyyy-mm-dd` format in order for it to do all
its cool organizing and sorting magic. 

Since we have no guarantees as to the format of the `"date"` coming from Zotero,
we have to write a function that will look for different formats using regex and
the `re` built-in package, and convert them. I've only written a few here, and
will continue to add them as needed.

I won't go over the regexes here; you can look up the syntax for Python's `re`
package [here](https://docs.python.org/3/library/re.html). 

Two wrinkles: 

- In many cases, a citation contains a year but no month or day. In these cases,
  I fill in `01-01` for the month and day. In general, you shouldn't do this:
  you should ideally use a unique tag that means "no data available", otherwise
  these entries will get confused with those which were legitimately published
  on New Year's Day. However, Hugo expects numbers (not strings); you can
  experiment with other placeholder values if you wish (e.g. `00-00` or `99-99`
  would be obvious placeholder values, but I haven't tested if they will work
  with Hugo), but for the purposes of this setup, it doesn't matter: with the
  Hugo template we're using, entries are sorted by year and then alphabetically
  by title. The month and day values are ignored.
- I had to create a dictionary mapping (`monthdict`) between text month names
  and numbers. To keep things relatively simple, I take in whatever month text
  there is, convert it to lowercase, and grab the first three-letters. This way
  I don't need to have repeated keys. I feel like this is reasonable, and should
  only break if a citation writes "December" as "dcmbr" or something. 

{{< highlight python >}}def fix_datestring(d):
    """Checks string d against various date formats, 
    returns a warning if it doesn't find a match.

    Hugo requires the date yaml field to be of the form yyyy-mm-dd.
    """
    
    # yyyy-mm-dd - This is the target format -- just return the string
    p = re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', d)
    if p is not None:
        return d

    # yyyy - No month or date available, so just fill in a dummy month and day
    p = re.match(r'[0-9]{4}$',d)
    if p is not None:
        return d + '-01-01'
    
    # mm/dd/yyyy - month, date, and year separated by forward slashes. 
    # Sometimes this appears as m/d/yyyy, or grossly, m/d/yy
    p = re.match(r'([0-9]+)\/([0-9]+)\/([0-9]+)', d)
    if p is not None:
        # pull out the parts and modify according to their lengths
        month = p.group(1)
        day = p.group(2)
        year = p.group(3)
        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
        if len(year) < 4:
            # This is a massive error because we don't know which 
            # century the paper is from. Let's assume that if the 
            # paper is published before "30", it's probably from the 2000's.
            if int(year) < 30:
                year = '20' + year
            else:
                year = '19' + year
        return year + '-' + month + '-' + day

    # Construct a map for text-based months
    monthdict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    
    # December 19, 2019 - Month written out, then date, then year. 
    # Sometimes there's a comma between day and year, sometimes not. 
    # Sometimes the month is abbreviated, which may lead to a period after the month.
    p = re.match(r'([A-Za-z\.]*)\s([0-9]+),\s([0-9]{1,4})', d)
    if p is not None:
        # Take the first three letters of the month name
        # Hopefully the date isn't written with a single letter
        month = p.group(1)[0:3]
        day = p.group(2)
        year = p.group(3)

        # Convert the month to a numeric
        month = str(monthdict[month.lower()])

        return year + '-' + month + '-' + day

    # If none of those match, then simply pass the date back unchanged
    return d

{{< / highlight >}}

### Putting It Together With Makefiles

So that's it for the parser. The process is to export the JSON from Zotero, then run the Python script with the correct input and output arguments to process the JSON into a bunch of markdown files that contain formatting that Hugo can use. To automate this a *bit*, I put the following target in my Makefile:

{{< highlight make >}}citations: path\\to\\citations.json
    del content\\publications\\*.md
	python jsonparser.py --input path\\to\\citations.json \
        --output_dir content\\publications\\
{{< /highlight >}}

This will run the next time the JSON file changes, delete the markdown files,
and re-process the citations to spit out a new group of files. (Note that I'm
using double-backslashes here because I'm on Windows, so I'm using [GnuMake for
Windows]().)

### Wrapping Up

So that's pretty much it! With Zotero set up to auto-export the JSON, any time I
add a citation the file will be updated, which will trigger a rebuilding of my
`publications` directory of auto-generated markdown files the next time I run
`make`. You can check out the full source code for the site
[here](https://github.com/scottdoy/scottdoy.hugo).

This was probably **way** more complex than it needs to be, but after searching
around there didn't seem to be a solution that satisfies all my requirements.
The big takeaway is that if your software doesn't provide the functionality you
need, there is usually a way to work around it, especially if you know a bit of
coding. Breaking the problem down into individual parts, then solving each one,
is the best approach to a daunting task. In this case, I learned a lot about
parsing JSON files, converting those to other formats, and then exporting
things. I also learned about the details in how Hugo works for generating pages,
although that's more of a niche topic. :smile: 