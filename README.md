# miRNA editing
This is the instruction for running miRNA editing events calling pipeline.

## Usage
* Input file: TCGA miRNA-seq bam file.
* Output file: miRNA editing candidate sites in the corresponding sample.

## To run the pipeline:
* install prerequsite tools
* put required files in the same folder with all scripts
* modify the input bam file name in main.sh file
* in bash, run ./main.sh

## Prerequisite tools for pipeline runing:
* bedtools2 (or any other tools for bam-to-fastq transformation)
* bowtie

## Required pre-generated files for miRNA editing calling:
* hsa-mature-release21.fa (all known human miRNA mature sequence, downloaded from [miRBase](http://www.mirbase.org)
* secondaryStructure.oneresult (secondary structure of pre-miRNA, generated from RNAfold)
* hsa-hairpin-release21-subUtoT.againstHg19.fmt (pre-miRNA align against reference genome)

## Required perl module:
* Math::CDF

## Reference
* Wang, Yumeng, et al. "Systematic characterization of A-to-I RNA editing hotspots in microRNAs across human cancers." Genome Research (2017). [link](http://genome.cshlp.org/content/early/2017/05/23/gr.219741.116.abstract)

## Copyright
* (c) Copyright The University of Texas MD Anderson Cancer Center,
* (c) Baylor College of Medicine,
* (c) Dr. Han Liang Lab (http://odin.mdacc.tmc.edu/~hliang1/)
* @author Yumeng Wang (yumengw@bcm.edu) 04-28-2016


