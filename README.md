# miRNA editing 
#############################################################################
## This is the instruction for running miRNA editing events calling pipeline.
## -Input file: TCGA miRNA-seq bam file.
## -Output file: miRNA editing candidate sites in the corresponding sample.
## (c) Copyright The University of Texas MD Anderson Cancer Center,
## (c) Baylor College of Medicine,
## (c) Dr. Han Liang Lab (http://odin.mdacc.tmc.edu/~hliang1/)
## @author Yumeng Wang (yumengw@bcm.edu) 04-28-2016
############################################################################

To run the pipeline:
a. install prerequsite tools
b. put required files in the same folder with all scripts
c. modify the input bam file name in main.sh file
d. in bash, run ./main.sh

############################################################################

Prerequisite tools for pipeline runing:
a. bedtools2 (or any other tools for bam-to-fastq transformation)
b. bowtie

Required pre-generated files for miRNA editing calling:
a. hsa-mature-release21.fa (all known human miRNA mature sequence, downloaded from http://www.mirbase.org)
b. secondaryStructure.oneresult (secondary structure of pre-miRNA, generated from RNAfold)
c. hsa-hairpin-release21-subUtoT.againstHg19.fmt (pre-miRNA align against reference genome)

Required perl module:
a. Math::CDF

############################################################################
