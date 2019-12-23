---
title: "Cascaded Multi-Class Pairwise Classifier (Cascampa) For Normal, Cancerous, And Cancer Confounder Classes In Prostate Histology"
author: Doyle, S., Feldman, M., Tomaszewski, J., Shih, N., Madabhushi, A.
status: Published
type: conference
citation: "Cascaded Multi-Class Pairwise Classifier (Cascampa) For Normal, Cancerous, And Cancer Confounder Classes In Prostate Histology, <em>2011 IEEE International Symposium on Biomedical Imaging (ISBI)</em>, 2011"
comments: no
doi: 10.1109/ISBI.2011.5872506
date: 2011-01-01
publishdate: 2011-01-01
---

Gleason grading of prostate cancer is complicated by cancer confounders, or benign tissues closely resembling malignant processes (e.g. atrophy), which account for as much as 34% of misdiagnoses. Thus, it is critical to correctly identify confounders in a computer-aided diagnosis system. In this work, we present a cascaded multi-class pairwise classifier (CascaMPa) to identify the class of regions of interest (ROIs) of prostate tissue biopsies. CascaMPa incorporates domain knowledge to partition the multi-class problem into several binary-class tasks, reducing the intra-class heterogeneity that causes errors in one-versus-all multi-class approaches. Nuclear centroids are detected automatically via a deconvolution and watershed algorithm, and a set of features are calculated from graphs (Voronoi, Delaunay, and minimum spanning tree graphs) constructed on the centroids. The cascaded multi-class algorithm identifies each feature vector as one of six tissue classes: Gleason patterns 3, 4, and 5, normal epithelium and stroma, and non-cancerous atrophy (a cancer confounder) using a decision tree classifier. Performance of CascaMPa is evaluated using positive predictive value (PPV) and area under the receiver operating characteristic curve (AUC). For a database of 50 image patches per class (300 ROIs) from 118 patient studies, the classifier achieves an average PPV of 0.760 and AUC of 0.762 across all classes, while the one-versus-all approach yields an average PPV of 0.633 and AUC of 0.444.
