---
title: "Evaluation Of Effects Of Jpeg2000 Compression On A Computer-Aided Detection System For Prostate Cancer On Digitized Histopathology"
author: Doyle, S., Monaco, J., Madabhushi, A., Lindholm, S., Ljung, P., Ladic, L., Tomaszewski, J., Feldman, M.
status: Published
type: conference
citation: "Evaluation Of Effects Of Jpeg2000 Compression On A Computer-Aided Detection System For Prostate Cancer On Digitized Histopathology, <em>2010 IEEE 7th International Symposium on Biomedical Imaging (ISBI)</em>, 2010"
comments: no
doi: Doi 10.1109/Isbi.2010.5490238
date: 2010-01-01
publishdate: 2010-01-01
---

A single digital pathology image can occupy over 10 gigabytes of hard disk space, rendering it difficult to store, analyze, and transmit. Though image compression provides a means of reducing the storage requirement, its effects on CAD (and pathologist) performance are not yet clear. In this work we assess the impact of compression on the ability of a CAD system to detect carcinoma of the prostate (CaP) in histological sections. The CAD algorithm proceeds as follows: Glands in the tissue are segmented using a region-growing algorithm. The size of each gland is then extracted and modeled using a mixture of Gamma distributions. A Markov prior (specifically, a probabilistic pairwise Markov model) is employed to encourage nearby glands to share the same class (i.e. cancerous or non-cancerous). Finally, cancerous glands are aggregated into continuous regions using a distance-hull algorithm. We evaluate CAD performance over 12 images compressed at 14 different compression ratios using JPEG2000. Algorithm performance (measured using the under the receiver operating characteristic curves) remains relatively constant for compression ratios up to 1:256. After this point performance degrades precipitously. We also have an expert pathologist view the compressed images and assign a confidence measure as to their diagnostic fidelity.
