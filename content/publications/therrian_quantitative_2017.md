---
title: "Quantitative Dataset Similarity For Fusing Multi-Institutional Image Collections"
author: Therrian, R., Mangione, W., Doyle,, S.
status: Published
type: conference
citation: "Quantitative Dataset Similarity For Fusing Multi-Institutional Image Collections, 2017"
comments: no
doi: none
date: 2017-01-01
publishdate: 2017-01-01
---

Introduction: This project  focuses  on fusing  digital  histological  image  databases obtained from multiple institutions. Modern image classifiers like convolutional neural networks (CNNs) have enjoyed great success in natural image analysis. This success is dependent  on vast  amounts of  training  cases:  the  well-studied  ImageNet  database 1 contains  over  14  million  images  described  by  over  20,000  phrases. Unfortunately, there  is  no histopathological  image database  of  comparable  size, as  building  such  a 
massive  collection  of   human-annotated  data  for  digital  pathology   is  a   massive undertaking.  To  circumvent  this  difficulty,  we  aim  to  demonstrate  a  quantitative approach  to  compare  datasets  collected  from  multiple  institutions  for  the  purpose  of dataset fusion to improve training set size. We  demonstrate  our  approach  on  digitized  H&E  tissue  sections  of  colorectal cancer (CRC). Kather, et al. 2 have published a method for identifying 8 tissue classes from CRC  images using support vector machines  (SVMs) and texture-based  features, and have provided their image data and code for download. In this study, we compare 
the Kather dataset (hereafter “Kather”) with a set of CRC images ob
tained at the Erie 
County  Medical  Center  (“ECMC”)
. 
This  fusion  allows  us  to 
extend  our  image 
database to 
build more robust 
classifiers. 
Methods:
We  begin  by  extracting  the  top
-
performing  texture  features  (as  reported 
previously
2
)  from both the “Kather” a
nd “ECMC” image datasets. Four measures of 
dataset similarity are computed: (1) A Student’s T
-
test  is  performed  on  the  feature 
vectors  in  each  class  to  establish  whether  the  datasets  are  statistically  significantly 
different.  (2)  Cluster  plots  of  the  featu
res  are  created  to  visualize  the  differences 
between class structures in each dataset. (3) The variance ratio criteria (VRC), a ratio 
of  between
-
cluster  to  within
-
cluster  variance,  is  calculated  to  measure  clustering 
similarity.  (4)  SVM  classification  is  u
sed  to  establish  whether  there  is  a  difference 
between classifier performance. 
Results:
(1) 
The  results  of  the  t
-
test  are  given  in 
Figure  2
.  We  reject  the  null 
hypothesis,  meaning  that  the  feature  vectors  from  the  two  datasets  likely  come  from 
populations
with  different  means.  (2)  However,  the  cluster  plots  in 
Figure  3
show  a 
similar  class  structure  in  feature  space,  indicating  that  the  difference  between  the 
dataset  features  may  not  impact  classifier  performance.  (3)  The  calculated  VRC  for 
“Kather
” is 0.0806; for “ECMC”, 0.0991. This indicates that both datasets have a 
similar  between
-
cluster  /  within
-
cluster  ratio,  further  validating  the  class  structure 
similarity  in  feature  space.  (4)  SVM  classification  results  are  shown  in 
Figure  4
for each of the 4 classes, along with the absolute difference  in performance.  We observe that “ECMC” achieves higher performance, commensurate with its higher VRC value. Conclusions: Proper  multi-institutional  dataset  fusion  provides  a  way  to  build  large, annotated  databases  of  digital pathology  images  at  a  greatly  reduced cost.  While  our statistical  tests  showed that  there  is  a  statistical  difference between  the  means  of  the Kather  and ECMC  image  sets feature  values,  the cluster  analysis  and classification results  suggest that similar  patterns  in  feature  space  allow for  similar  performance  in SVM classification. Future work will focus on further validation of the fused datasets in  additional  contexts,  including training  deep  CNN  classifiers  for pixel-wise  tissue segmentation on high-resolution images.
