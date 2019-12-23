---
title: "Data-Driven Sampling Method For Building 3D Anatomical Models From Serial Histology"
author: Salunke, S., Ablove, T., Danforth, T., Tomaszewski, J., Doyle, S.
status: Published
type: conference
citation: "Data-Driven Sampling Method For Building 3D Anatomical Models From Serial Histology, <b>10140</b>, 2017"
comments: no
doi: 10.1117/12.2255800
date: 2017-01-01
publishdate: 2017-01-01
---

In this work, we investigate the effect of slice sampling on 3D models of tissue architecture using serial histopathology.
We present a method for using a single fully-sectioned tissue block as pilot data, whereby we build a fully-realized 3D
model and then determine the optimal set of slices needed to reconstruct the salient features of the model objects under
biological investigation. In our work, we are interested in the 3D reconstruction of microvessel architecture in the trigone
region between the vagina and the bladder. This region serves as a potential avenue for drug delivery to treat bladder
infection. We collect and co-register 23 serial sections of CD31-stained tissue images (6 μm thick sections), from which
four microvessels are selected for analysis. To build each model, we perform semi-automatic segmentation of the
microvessels. Subsampled meshes are then created by removing slices from the stack, interpolating the missing data, and
re-constructing the mesh. We calculate the Hausdorff distance between the full and subsampled meshes to determine the
optimal sampling rate for the modeled structures. In our application, we found that a sampling rate of 50% (corresponding
to just 12 slices) was sufficient to recreate the structure of the microvessels without significant deviation from the fullyrendered
mesh. This pipeline effectively minimizes the number of histopathology slides required for 3D model
reconstruction, and can be utilized to either (1) reduce the overall costs of a project, or (2) enable additional analysis on
the intermediate slides.
