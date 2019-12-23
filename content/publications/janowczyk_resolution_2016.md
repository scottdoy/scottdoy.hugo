---
title: "A Resolution Adaptive Deep Hierarchical (Radhical) Learning Scheme Applied To Nuclear Segmentation Of Digital Pathology Images"
author: Janowczyk, A., Doyle, S., Gilmore, H., Madabhushi, A.
status: Published
type: journal
citation: "A Resolution Adaptive Deep Hierarchical (Radhical) Learning Scheme Applied To Nuclear Segmentation Of Digital Pathology Images, <em>Computer Methods in Biomechanics and Biomedical Engineering: Imaging & Visualization</em>, <b>0</b>(0), 2016"
comments: no
doi: 10.1080/21681163.2016.1141063
date: 2016-01-01
publishdate: 2016-01-01
---

Deep learning (DL) has recently been successfully applied to a number of image analysis problems. However, DL approaches tend to be inefficient for segmentation on large image data, such as high-resolution digital pathology slide images. For example, typical breast biopsy images scanned at 40 magnification contain billions of pixels, of which usually only a small percentage belong to the class of interest. For a typical naïve deep learning scheme, parsing through and interrogating all the image pixels would represent hundreds if not thousands of hours of compute time using high performance computing environments. In this paper, we present a resolution adaptive deep hierarchical (RADHicaL) learning scheme wherein DL networks at lower resolutions are leveraged to determine if higher levels of magnification, and thus computation, are necessary to provide precise results. We evaluate our approach on a nuclear segmentation task with a cohort of 141 ER+ breast cancer images and show we can reduce computation time on average by about 85%. Expert annotations of 12,000 nuclei across these 141 images were employed for quantitative evaluation of RADHicaL. A head-to-head comparison with a naïve DL approach, operating solely at the highest magnification, yielded the following performance metrics: .9407 vs .9854 Detection Rate, .8218 vs .8489 F-score, .8061 vs .8364 true positive rate and .8822 vs 0.8932 positive predictive value. Our performance indices compare favourably with state of the art nuclear segmentation approaches for digital pathology images.
