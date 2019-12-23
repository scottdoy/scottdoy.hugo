---
title: "Role Of Training Data Variability On Classifier Performance And Generalizability"
author: Therrien, R., Doyle, S.
status: Published
type: conference
citation: "Role Of Training Data Variability On Classifier Performance And Generalizability, <em>Medical Imaging 2018: Digital Pathology</em>, <b>10581</b>, 2018"
comments: no
doi: 10.1117/12.2293919
date: 2018-01-01
publishdate: 2018-01-01
---

Large, high-quality training datasets are necessary for machine learning classifiers to achieve high performance. Due to the high cost of collecting quality annotated data, dataset sizes for medical imaging applications are typically small and collected at a single institution. The use of small, single-site datasets results in classifiers that do not generalize well to data collected at different institutions or under different imaging protocols. Previous attempts to address this problem resulted in development of transfer learning and domain adaptation algorithms. Our work investigates the improvement of generalization performance by increasing training data variability. We use data from multiple sites (one from a local clinic and two from publicly available sets) to train support vector machines (SVMs) and Convolutional Neural Networks (CNNs) to distinguish tissue patches of hematoxylin and eosin (H&amp;E) stained tissue of colorectal cancer (CRC). To measure the effect of increasing training set variability on classifier robustness, we create different training combinations of two datasets for training and validation, and use the third set is reserved for testing. SVM accuracy on the testing dataset ranged from 50% to 59% when training with data from a single site, which increases to 61% when data from both sites was combined in training. Using CNNs, the testing accuracy was 56% and 67% when training on single-site data, which increased to 70% with data from both sites. Thus, the increase in generalization performance exists for both traditional and deep learning algorithms, and is essential for building larger datasets for medical image classification.
