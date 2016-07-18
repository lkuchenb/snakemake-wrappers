# Wrapper for fastq_screen

[`fastq_screen`](http://www.bioinformatics.babraham.ac.uk/projects/fastq_screen)
screens a library of sequences in FASTQ format against a set of sequence
databases so you can see if the composition of the library matches with what
you expect.

The databases are bowtie or bowtie2 indexes. These indexes, along with which
aligner (bowtie or bowtie2) to use and how many reads to consider, are defined
in a configuration file.

This wrapper allows the configuration to be passed as a filename or as
a dictionary in the rule's  `params.fastq_screen_config` of the rule. So the
following configuration file.


```
DATABASE	ecoli	/data/Escherichia_coli/Bowtie2Index/genome	BOWTIE2
DATABASE	ecoli	/data/Escherichia_coli/Bowtie2Index/genome	BOWTIE
DATABASE	hg19	/data/hg19/Bowtie2Index/genome	BOWTIE2
DATABASE	mm10	/data/mm10/Bowtie2Index/genome	BOWTIE2
BOWTIE	/path/to/bowtie
BOWTIE2	/path/to/bowtie2
```

becomes:

```
fastq_screen_config = {
 'database': {
   'ecoli': {
     'bowtie2': '/data/Escherichia_coli/Bowtie2Index/genome',
     'bowtie': '/data/Escherichia_coli/BowtieIndex/genome'},
   'hg19': {
     'bowtie2': '/data/hg19/Bowtie2Index/genome'},
   'mm10': {
     'bowtie2': '/data/mm10/Bowtie2Index/genome'}
 },
 'aligner_paths': {'bowtie': 'bowtie', 'bowtie2': 'bowtie2'}
}
```

By default, the wrapper will use bowtie2 as the aligner and a subset of 100000
reads.  These can be overridden using `params.aligner` and `params.subset`
respectively. Furthermore, `params.extra` can be used to pass additional
arguments verbatim to `fastq_screen`, for example `extra="--illumina1_3"` or
`extra="--bowtie2 '--trim5=8'"`.

## Notes

- `fastq_screen` hard-codes the output filenames. This wrapper moves the
  hard-coded output files to those specified by the rule.

- While the dictionary form of `fastq_screen_config` is convenient, the
  unordered nature of the dictionary may cause `snakemake --list-params-changed`
  to incorrectly report changed parameters even though the contents remain the
  same. If you plan on using `--list-params-changed` then it will be better to
  write a config file and pass that as `fastq_screen_config`.

- When providing the dictionary form of `fastq_screen_config`, the wrapper will
  write a temp file using Python's `tempfile` module. To control the temp file
  directory, make sure the `$TMPDIR` environmental variable is set (see [tempfile
  docs](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp) for
  details). One way of doing this is by adding  something like
  `shell.prefix("export TMPDIR=/scratch; ")` to the snakefile calling this
  wrapper.

## Input

A FASTQ file, gzipped or not.

## Output

`txt`: a text file containing the fraction of reads mapping to each provided
index

`png`: a bar plot of the contents of `txt`, saved as a PNG file

## Example:

```
rule fastq_screen:
    input:
        "samples/{sample}.fastq.gz"
    output:
        txt="qc/{sample}.fastq_screen.txt",
        png="qc/{sample}.fastq_screen.png"
    params:
        fastq_screen_config=fastq_screen_config,
        subset=100000,
        aligner='bowtie2'
    threads: 8
    wrapper:
        "0.7.0/bio/fastq_screen"
```