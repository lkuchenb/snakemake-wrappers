__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
os.system(
    f"gatk --java-options '{java_opts}' GenotypeGVCFs {extra} "
    "-V {snakemake.input.gvcf} "
    "-R {snakemake.input.ref} "
    "-O {snakemake.output.vcf} {log}"
)
