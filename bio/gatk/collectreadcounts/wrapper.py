__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smed"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

mergingRule = snakemake.params.get("mergingRule", "OVERLAPPING_ONLY")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' CollectReadCounts"
        " -I {snakemake.input.bam}"
        " -L {snakemake.input.intervals}"
        " --interval-merging-rule {mergingRule}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.counts}"
        " {log}"
    )
