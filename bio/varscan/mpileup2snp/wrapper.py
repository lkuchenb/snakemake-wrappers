"""Snakemake wrapper for Varscan2 mpileup2snp"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os.path as op
from snakemake.shell import shell
from snakemake.utils import makedirs

# Gathering extra parameters and logging behaviour
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
java_opt = snakemake.params.get("java_opt", "")

pileup = (" <( cat {snakemake.input[0]} ) "
          if not snakemake.input[0].endswith("gz")
          else " <(zcat {snakemake.input[0]}) ")

# Building output directories
makedirs(op.dirname(snakemake.output[0]))

shell(
    "varscan mpileup2snp "       # Tool and its subprocess
    "{pileup} "                  # Path to pileup file
    "{extra} "                   # Extra parameters
    " > {snakemake.output[0]} "  # Path to vcf file
    "{log}"                      # Logging behaviour
)
