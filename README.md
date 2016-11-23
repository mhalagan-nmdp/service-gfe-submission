# service-gfe-submission

RESTful API and UI for getting GFE results from raw sequence data

[![Build Status](https://travis-ci.org/nmdp-bioinformatics/service-gfe-submission.svg?branch=master)](https://travis-ci.org/nmdp-bioinformatics/service-gfe-submission)[![Coverage Status](https://coveralls.io/repos/github/nmdp-bioinformatics/service-gfe-submission/badge.svg?branch=master)](https://coveralls.io/github/nmdp-bioinformatics/service-gfe-submission?branch=master)[![](https://images.microbadger.com/badges/image/nmdpbioinformatics/service-gfe-submission.svg)](https://microbadger.com/images/nmdpbioinformatics/service-gfe-submission "Get your own image badge on microbadger.com")[![](https://images.microbadger.com/badges/version/nmdpbioinformatics/service-gfe-submission.svg)](https://microbadger.com/images/nmdpbioinformatics/service-gfe-submission "Get your own version badge on microbadger.com")

[![License](https://img.shields.io/badge/License-GNU%20General%20Public%20License%20v3.0-blue.svg)]()

The Gene Feature Enumeration (GFE) Submission service provides an API for converting raw sequence data to GFE. It provides both a RESTful API and a simple user interface for converting raw sequence data to GFE results. Sequences can be submitted one at a time or as a fasta file. This service uses [nmdp-bioinformatics/service-feature](https://github.com/nmdp-bioinformatics/service-feature) for encoding the raw sequence data and [nmdp-bioinformatics/HSA](https://github.com/nmdp-bioinformatics/HSA) for aligning the raw sequence data. A public version of this service is available for use at [gfe.b12x.org](http://gfe.b12x.org). Further documentation and tutorials are available at [service-gfe-submission.readthedocs.io](http://service-gfe-submission.readthedocs.io/en/latest/index.html).


## RESTful Calls

```bash
    
# Get GFE from sequence data - in body #
curl --header "Content-type: application/json" --request POST 
--data '{"locus":"HLA-A","sequence":"TCCCCAGACGCCGAGGATGGCCGTCATGGCGCCCCGAACCCTCCTCCT
GCTACTCTCGGGGGCCCTGGCCCTGACCCAGACCTGGGCGGGTGAGTGCGGGGTCGGGAGGGAAACCGCCTCTGCGGGGAGAAGC
AAGGGGCCCTCCTGGCGGGGGCGCAGGACCGGGGGAGCCGCGCCGGGACGAGGGTCGGGCAGGTCTCAGCCACTGCTCGCCCCCA
GGCTCCCACTCCATGAGGTATTTCTTCACATCCGTGTCCCGGCCCGGCCGCGGGGAGCCCCGCTTCATCGCCGTGGGCTACGTGG
ACGACACGCAGTTCGTGCGGTTCGACAGCGACGCCGCGAGCCAGAGGATGGAGCCGCGGGCGCCGTGGATAGAGCAGGAGGGGCC
GGAGTATTGGGACCAGGAGACACGGAATGTGAAGGCCCAGTCACAGACTGACCGAGTGGACCTGGGGACCCTGCGCGGCTACTAC
AACCAGAGCGAGGCCGGTGAGTGACCCCGGCCGGGGGCGCAGGTCAGGACCCCTCATCCCCCACGGACGGGCCAGGTCGCCCACA
GTCTCCGGGTCCGAGATCCACCCCGAAGCCGCGGGACCCCGAGACCCTTGCCCCGGGAGAGGCCCAGGCGCCTTTACCCGGTTTC
ATTTTCAGTTTAGGCCAAAAATCCCCCCGGGTTGGTCGGGGCTGGGCGGGGCTCGGGGGACTGGGCTGACCGCGGGGTCGGGGCC
AGGTTCTCACACCATCCAGATAATGTATGGCTGCGACGTGGGGTCGGACGGGCGCTTCCTCCGCGGGTACCGGCAGGACGCCTAC
GACGGCAAGGATTACATCGCCCTGAACGAGGACCTGCGCTCTTGGACCGCGGCGGACATGGCGGCTCAGATCACCAAGCGCAAGT
GGGAGGCGGCCCATGAGGCGGAGCAGTTGAGAGCCTACCTGGATGGCACGTGCGTGGAGTGGCTCCGCAGATACCTGGAGAACGG
GAAGGAGACGCTGCAGCGCACGGGTACCAGGGGCCACGGGGCGCCTCCCTGATCGCCTGTAGATCTCCCGGGCTGGCCTCCCACA
AGGAGGGGAGACAATTGGGACCAACACTAGAATATCACCCTCCCTCTGGTCCTGAGGGAGAGGAATCCTCCTGGGTTCCAGATCC
TGTACCAGAGAGTGACTCTGAGGTTCCGCCCTGCTCTCTGACACAATTAAGGGATAAAATCTCTGAAGGAGTGACGGGAAGACGA
TCCCTCGAATACTGATGAGTGGTTCCCTTTGACACCGGCAGCAGCCTTGGGCCCGTGACTTTTCCTCTCAGGCCTTGTTCTCTGC
TTCACACTCAATGTGTGTGGGGGTCTGAGTCCAGCACTTCTGAGTCCCTCAGCCTCCACTCAGGTCAGGACCAGAAGTCGCTGTT
CCCTTCTCAGGGAATAGAAGATTATCCCAGGTGCCTGTGTCCAGGCTGGTGTCTGGGTTCTGTGCTCTCTTCCCCATCCCGGGTG
TCCTGTCCATTCTCAAGATGGCCACATGCGTGCTGGTGGAGTGTCCCATGACAGATGCAAAATGCCTGAATTTTCTGACTCTTCC
CGTCAGACCCCCCCAAGACACATATGACCCACCACCCCATCTCTGACCATGAGGCCACCCTGAGGTGCTGGGCCCTGGGCTTCTA
CCCTGCGGAGATCACACTGACCTGGCAGCGGGATGGGGAGGACCAGACCCAGGACACGGAGCTCGTGGAGACCAGGCCTGCAGGG
GATGGAACCTTCCAGAAGTGGGCGGCTGTGGTGGTGCCTTCTGGAGAGGAGCAGAGATACACCTGCCATGTGCAGCATGAGGGTC
TGCCCAAGCCCCTCACCCTGAGATGGGGTAAGGAGGGAGATGGGGGTGTCATGTCTCTTAGGGAAAGCAGGAGCCTCTCTGGAGA
CCTTTAGCAGGGTCAGGGCCCCTCACCTTCCCCTCTTTTCCCAGAGCTGTCTTCCCAGCCCACCATCCCCATCGTGGGCATCATT
GCTGGCCTGGTTCTCCTTGGAGCTGTGATCACTGGAGCTGTGGTCGCTGCCGTGATGTGGAGGAGGAAGAGCTCAGGTGGAGAAG
GGGTGAAGGGTGGGGTCTGAGATTTCTTGTCTCACTGAGGGTTCCAAGCCCCAGCTAGAAATGTGCCCTGTCTCATTACTGGGAA
GCACCGTCCACAATCATGGGCCTACCCAGTCTGGGCCCCGTGTGCCAGCACTTACTCTTTTGTAAAGCACCTGTTAAAATGAAGG
ACAGATTTATCACCTTGATTACGGCGGTGATGGGACCTGATCCCAGCAGTCACAAGTCACAGGGGAAGGTCCCTGAGGACAGACC
TCAGGAGGGCTATTGGTCCAGGACCCACACCTGCTTTCTTCATGTTTCCTGATCCCGCCCTGGGTCTGCAGTCACACATTTCTGG
AAACTTCTCTGGGGTCCAAGACTAGGAGGTTCCTCTAGGACCTTAAGGCCCTGGCTCCTTTCTGGTATCTCACAGGACATTTTCT
TCTCACAGATAGAAAAGGAGGGAGTTACACTCAGGCTGCAAGTAAGTATGAAGGAGGCTGATGCCTGAGGTCCTTGGGATATTGT
GTTTGGGAGCCCATGGGGGAGCTCACCCACCTCACAATTCCTCCTCTAGCCACATCTTCTGTGGGATCTGACCAGGTTCTGTTTT
TGTTCTACCCCAGGCAGTGACAGTGCCCAGGGCTCTGATGTGTCCCTCACAGCTTGTAAAGGTGAGAGCTTGGAGGACCTAATGT
GTGTTGGGTGTTGGGCGGAACAGTGGACACAGCTGTGCTATGGGGTTTCTTTGCATTGGATGTATTGAGCATGCGATGGGCTGTT
TAAGGTGTGACCCCTCACTGTGATGGATATGAATTTGTTCATGAATATTTTTTTCTATAGTGTGAGACAGCTGCCTTGTGTGGGA
CTGAG"}'
http://gfe.b12x.org/api/v1/gfe

# Get GFE from fasta file #
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' 
--data '{"fasta":"public/downloads/FastaTest.fasta","locus":"HLA-A","structures": 0,"verbose":0}' 
http://gfe.b12x.org/api/v1/fasta

# Get GFE from HML file #
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' 
--data '{"fasta":"public/downloads/HmlTest.fasta","locus":"HLA-A","structures": 0,"verbose":0}' 
http://gfe.b12x.org/api/v1/fasta

# Sequence from GFE #
curl --header "Content-type: application/json" --request POST
--data '{"locus":"HLA-A","gfe":"HLA-Aw1-1-7-20-10-32-7-1-1-1-6-1-5-3-5-1-0"}'
http://gfe.b12x.org/api/v1/sequence


```

## Perl client example

```perl

#!/usr/bin/env perl
use strict;
use warnings;
use GFE_Client;

our($s_locus,$s_seq,$s_url) = (undef,undef,undef);
&GetOptions('locus|l=s'     => \$s_locus,
			'seq|s=s'       => \$s_seq,
			'url|u=s'       => \$s_url
            );

# Does alignment of sequence and submission of aligned
# sequence to the GFE service.
my $o_client = GFE_Client->new();
$o_client->gfe_url($s_url) if defined $s_url;
my $rh_gfe   = $o_client->getGfe($s_locus,$s_seq);

# Print out GFE
print $$rh_gfe{gfe},"\n";

```

## R client example

```R

if (!is.installed("gfeClient”")){
	library(devtools)
	install_github("nmdp-bioinformatics/service-gfe-submission/client-R")
}
library("gfeClient”)

host <- "http://gfe.b12x.org/"

# Get GFE from fasta file
fasta.file <- "GFE_Submission/t/resources/fastatest1.fasta"
fasta.gfe  <- fasta2gfe(host,"HLA-A",fasta.file)

# Get sequence from
seq        <- gfe2seq(host,"HLA-A","HLA-Aw1-1-7-20-10-32-7-1-1-1-6-1-5-3-5-1-1")
print(paste0("Sequence: ",unlist(seq$sequence[[1]])))

# Get GFE from sequence
gfe        <- seq2gfe(host,"HLA-A",seq)
print(paste0("GFE: ",unlist(gfe$gfe[[1]])))

# return detailed logs
# Default = 0
gfe        <- seq2gfe(host,"HLA-A",seq,1)
print(paste0("Logs: ",unlist(gfe$logs[[1]])))

# Return structure (ex. exon, 1 , TGCCCAAGCCCCTCACCCTGAGATGGG)
# Default = 0
gfe        <- seq2gfe(host,"HLA-A",seq,0,1)
print(paste0("Structure: ",unlist(gfe$structure[[1]])))

```

### Tools

```bash
./gfe-submission [--fasta] [--uri] [--verbose] [--help]
            -f/--fasta      Fasta file
            -u/--uri        URI of feature service
            -l/--locus      HLA-Locus
            -v/--verbose    Flag for running in verbose
            -h/--help

gfe-submission --fasta t/resources/A.test1.fasta -l HLA-A -v 2> test1.gfe.log > test1.gfe.csv

```


## Installing and Running Service Locally

```bash
perl cpanm --installdeps .   # Install perl dependencies
perl Makefile.PL             # Generate Makefile
make                         # Make menefest
make test                    # Run tests
make install                 # Install
plackup -E deployment  \     # Deploy
-s Starman --workers=10 \
-p 5050:8080 -a bin/app.pl      
```

## Docker

```bash
docker pull nmdpbioinformatics/service-gfe-submission
docker run -d --name service-gfe-submission -p 5050:8080 service-gfe-submission:latest
```
[Click here](https://hub.docker.com/r/nmdpbioinformatics/service-gfe-submission/) for more information on the publically available docker image. 


### Required Software

 * [Git](http://git.org)
 * [clustalo](http://www.clustal.org/omega)
 * [hap1.0](https://github.com/nmdp-bioinformatics/HSA)
 * [perl 5.18 or later](http://perl.org)

### Related Links

 * [hub.docker.com/r/nmdpbioinformatics/service-gfe-submission](https://hub.docker.com/r/nmdpbioinformatics/service-gfe-submission)
 * [service-gfe-submission.readthedocs.io](https://service-gfe-submission.readthedocs.io/en/latest/index.html)
 * [github.com/nmdp-bioinformatics/service-feature](https://github.com/nmdp-bioinformatics/service-feature)
 * [github.com/nmdp-bioinformatics/HSA](https://github.com/nmdp-bioinformatics/HSA)
 * [bioinformatics.bethematchclinical.org](https://bioinformatics.bethematchclinical.org)
 * [feature.nmdp-bioinformatics.org](https://feature.nmdp-bioinformatics.org)
 * [gfe.b12x.org](http://gfe.b12x.org)

<p align="center">
  <img src="https://bethematch.org/content/site/images/btm_logo.png">
</p>



