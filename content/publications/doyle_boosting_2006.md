---
title: "A Boosting Cascade For Automated Detection Of Prostate Cancer From Digitized Histology"
author: Doyle, S., Madabhushi, A., Feldman, M., Tomaszeweski, J.
status: Published
type: conference
citation: "A Boosting Cascade For Automated Detection Of Prostate Cancer From Digitized Histology, <em>Medical Image Computing and Computer-Assisted Intervention (MICCAI)</em>, <b>4191</b>, 2006"
comments: no
doi: 10.1007/11866763_62
date: 2006-01-01
publishdate: 2006-01-01
---

Current diagnosis of prostatic adenocarcinoma is done by manual analysis of biopsy tissue samples for tumor presence. However, the recent advent of whole slide digital scanners has made histopathological tissue specimens amenable to computer-aided diagnosis (CAD). In this paper, we present a CAD system to assist pathologists by automatically detecting prostate cancer from digitized images of prostate histological specimens. Automated diagnosis on very large high resolution images is done via a multi-resolution scheme similar to the manner in which a pathologist isolates regions of interest on a glass slide. Nearly 600 image texture features are extracted and used to perform pixel-wise Bayesian classification at each image scale to obtain corresponding likelihood scenes. Starting at the lowest scale, we apply the AdaBoost algorithm to combine the most discriminating features, and we analyze only pixels with a high combined probability of malignancy at subsequent higher scales. The system was evaluated on 22 studies by comparing the CAD result to a pathologist's manual segmentation of cancer (which served as ground truth) and found to have an overall accuracy of 88%. Our results show that (1) CAD detection sensitivity remains consistently high across image scales while CAD specificity increases with higher scales, (2) the method is robust to choice of training samples, and (3) the multi-scale cascaded approach results in significant savings in computational time.
