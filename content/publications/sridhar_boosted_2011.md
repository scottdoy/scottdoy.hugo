---
title: "Boosted Spectral Embedding (Bose): Applications To Content-Based Image Retrieval Of Histopathology"
author: Sridhar, A., Doyle, S., Madabhushi, A.
status: Published
type: conference
citation: "Boosted Spectral Embedding (Bose): Applications To Content-Based Image Retrieval Of Histopathology, <em>2011 IEEE International Symposium on Biomedical Imaging (ISBI)</em>, 2011"
comments: no
doi: 10.1109/ISBI.2011.5872779
date: 2011-01-01
publishdate: 2011-01-01
---

In machine learning, non-linear dimensionality reduction (NLDR) is commonly used to embed high-dimensional data into a low-dimensional space while preserving local object adjacencies. However, the majority of NLDR methods define object adjacencies using distance metrics that do not account for the quality of the features in the high-dimensional space. In this paper we present Boosted Spectral Embedding (BoSE), a variant of the traditional Spectral Embedding (SE) that utilizes a Boosted Distance Metric (BDM) to improve the low-dimensional representation of the data. Under the naive assumption that all features are equally important, SE uses the Euclidean distance metric to define object-distance relationships. However, the BDM selectively weights features via the AdaBoost algorithm such that the low-dimensional representation contains only the most discriminating features. In this work BoSE is evaluated against SE in the context of digitized histopathology images using (a) content-based image retrieval and (b) classification via Random Forest of the low-dimensional representation. Using images from a cohort of 58 prostate cancer patient studies, BoSE and SE separated benign and malignant samples with areas under the precision-recall curve (AUPRCs) of 0.95 and 0.67 and classification accuracies using a Random Forest (RF) classifer were 0.93 and 0.79, respectively. For a cohort of 55 breast cancer studies, BoSE and SE performed comparably in terms of both RF accuracy and AUPRC. In addition, a qualitative visualization of the low-dimensional data representations suggests that BoSE exhibits improved class separability over SE.
