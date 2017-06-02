# Chunking Experiments

This repository contains experiments in Vietnamese Chunking problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Dataset Information

```
Sentences    : 7855
Unique words : 14245
Top words    : ,, ., ", của, là, và, có, một, người, được, không, đã, những, cho, :, ..., ở, trong, với, đến
POS Tags     : 28
List tags    : A, Ab, C, CH, Cb, Cc, E, Eb, I, L, M, Mb, N, Nb, Nc, Np, Nu, Ny, P, Pb, R, T, V, Vb, Vy, X, Y, Z
Chunking Tags: 21
List tags    : B-AP, B-MP, B-NP, B-PP, B-QP, B-TP, B-VP, B-WH, B-WP, B-XP, I-AP, I-MP, I-NP, I-PP, I-QP, I-VP, I-WH, I-WP, I-XP, N-NP, O
```

## Reports

* Detail Reports, [link](https://docs.google.com/spreadsheets/d/17atXtvgstvqWZStr9WxDziL5zvQjiBnYH1qXYFb8L5g/pubhtml?gid=0&single=true)
* Vietnamese Chunking publications, [link](https://docs.google.com/spreadsheets/d/17atXtvgstvqWZStr9WxDziL5zvQjiBnYH1qXYFb8L5g/pubhtml?gid=26250307&single=true)

## How to usage

```
$ git clone git@github.com:magizbox/underthesea.chunking.git
$ cd underthesea.chunking
$ conda env create -f environment.yml
```

Last update: June 2017
