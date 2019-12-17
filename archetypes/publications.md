---
title: "{{ replace .TranslationBaseName "-" " " | title }}" 
author: Scott Doyle
status: Published
type: conference, journal
citation: "citation"
tag: tag1 tag2
file: filename.pdf
subjects: x y z 
comments: no
doi: xx.yyyy/zzzzzzzzzzz
date: {{ .Date }}
publishdate: {{ .Date }}
filter:
  - erb
  - markdown
  - rubypants
---

