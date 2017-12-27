#########################################################################
## This is the miRNA editing events calling pipeline.
## Please refer to README for detailed runing instructions.
## -Input file: TCGA miRNA-seq bam file.
## -Output file: miRNA editing candidate sites in the corresponding sample.
## (c) Copyright The University of Texas MD Anderson Cancer Center,
## (c) Baylor College of Medicine,
## (c) Dr. Han Liang Lab (http://odin.mdacc.tmc.edu/~hliang1/).
## @author Yumeng Wang (yumengw@bcm.edu) 04-28-2016.
#########################################################################

input_filename="PUT YOUR INPUT BAM FILE NAME HERE"

## First transfer bam file to fastq file
bedtools2/bin/bamToFastq -i $input_filename -fq ${input_filename}.fastq

## Second filter reads that are too long, too short, or with low quality score
python filter_low_quality_short_long_read.py ${input_filename}.fastq > filter_seq_log 

## Third bowtie alignment to reference genome
bowtie-1.1.1/bowtie -n 1 -e 50 -a -m 1 --best --strata --trim3 2 bowtie-1.1.1/indexes/hg19 ${input_filename}.fastq.filtered > ${input_filename}.aligned

## Forth remove sequences aligned to mitochomdrion to save time and memory
perl filterByChr.pl ${input_filename}.aligned > ${input_filename}.aligned.filtChr

## Fifth analyze mutation based on alignment
perl Analyze_mutation_new_db.pl ${input_filename}.aligned.filtChr ${input_filename}.mutation

## Sixth perform binomial test to identify list of statistically significant editing candidate sites
perl Binomial_analysis_new_db.pl ${input_filename}.mutation > ${input_filename}.mutation.Bonferroni
