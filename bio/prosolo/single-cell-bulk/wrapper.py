"""Snakemake wrapper for ProSolo single-cell-bulk calling"""

__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"( prosolo single-cell-bulk "
    "--omit-indels "
    " {snakemake.params.extra} "
    "--candidates {snakemake.input.candidates} "
    "--output {snakemake.output} "
    "{snakemake.input.single_cell} "
    "{snakemake.input.bulk} "
    "{snakemake.input.ref} ) "
    "{log} "
)
