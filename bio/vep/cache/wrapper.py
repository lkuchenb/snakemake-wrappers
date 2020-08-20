__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
from pathlib import Path

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"vep_install --AUTO cf "
    "--SPECIES {snakemake.params.species} "
    "--ASSEMBLY {snakemake.params.build} "
    "--CACHE_VERSION {snakemake.params.release} "
    "--CACHEDIR {snakemake.output} "
    "--CONVERT "
    "--NO_UPDATE {log}"
)
