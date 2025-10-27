import os


exps = [
    "gen_diff_usenix_cot_vulnloc",
    "gen_diff_usenix_tot_vulnloc",
    "gen_diff_usenix_no_context_vulnloc",
    "gen_diff_usenix_zeroshot_vulnloc",
]
final = "collections"
os.makedirs(final, exist_ok=True)
for exp in exps:
    bugids = os.listdir(exp)
    exp_name = exp.replace("gen_diff_", "")
    for bugid in bugids:
        src = os.path.join(exp, bugid, f"{exp_name}_{bugid}_success.diff")
        dst = os.path.join(final, bugid, f"{exp_name}_{bugid}_success.diff")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(src):
            os.system(f"cp {src} {dst}")
        correct_patch = os.path.join(final, bugid, f"{bugid}.diff")
        if not os.path.exists(correct_patch):
            os.system(f"cp patch/{bugid}.diff {correct_patch}")
