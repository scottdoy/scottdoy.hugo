﻿---
title: "A Boosted Bayesian Multiresolution Classifier For Prostate Cancer Detection From Digitized Needle Biopsies"
author: Doyle, S., Feldman, M., Tomaszewski, J., Madabhushi, A.
status: Published
type: journal
citation: "A Boosted Bayesian Multiresolution Classifier For Prostate Cancer Detection From Digitized Needle Biopsies, <em>IEEE Transactions on Biomedical Engineering</em>, <b>59</b>(5), 2012"
comments: no
doi: 10.1109/TBME.2010.2053540
date: 2012-01-01
publishdate: 2012-01-01
---

Diagnosis of prostate cancer (CaP) currently involves examining tissue samples for CaP presence and extent via a microscope, a time-consuming and subjective process. With the advent of digital pathology, computer-aided algorithms can now be applied to disease detection on digitized glass slides. The size of these digitized histology images (hundreds of millions of pixels) presents a formidable challenge for any computerized image analysis program. In this paper, we present a boosted Bayesian multiresolution (BBMR) system to identify regions of CaP on digital biopsy slides. Such a system would serve as an important preceding step to a Gleason grading algorithm, where the objective would be to score the invasiveness and severity of the disease. In the first step, our algorithm decomposes the whole-slide image into an image pyramid comprising multiple resolution levels. Regions identified as cancer via a Bayesian classifier at lower resolution levels are subsequently examined in greater detail at higher resolution levels, thereby allowing for rapid and efficient analysis of large images. At each resolution level, ten image features are chosen from a pool of over 900 first-order statistical, second-order co-occurrence, and Gabor filter features using an AdaBoost ensemble method. The BBMR scheme, operating on 100 images obtained from 58 patients, yielded: 1) areas under the receiver operating characteristic curve (AUC) of 0.84, 0.83, and 0.76, respectively, at the lowest, intermediate, and highest resolution levels and 2) an eightfold savings in terms of computational time compared to running the algorithm directly at full (highest) resolution. The BBMR model outperformed (in terms of AUC): 1) individual features (no ensemble) and 2) a random forest classifier ensemble obtained by bagging multiple decision tree classifiers. The apparent drop-off in AUC at higher image resolutions is due to lack of fine detail in the expert annotation of CaP and is not an artifact of the classifier. The implicit feature selection done via the AdaBoost component of the BBMR classifier reveals that different classes and types of image features become more relevant for discriminating between CaP and benign areas at different image resolutions.