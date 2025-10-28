import os


exps = [
    "gen_diff_usenix_tot_vulnloc_semdiff",
]
final = "collections"
os.makedirs(final, exist_ok=True)
for exp in exps:
    bugids = os.listdir(exp)
    exp_name = exp.replace("gen_diff_", "")
    for bugid in bugids:
        os.makedirs(os.path.dirname(os.path.join(final, bugid)), exist_ok=True)
        files = os.listdir(os.path.join(exp, bugid))
        for file in files:
            if file.endswith(".diff"):
                src = os.path.join(exp, bugid, file)
                dst = os.path.join(final, bugid, file)
                if not os.path.exists(dst):
                    print(f"Update: {src} to {dst}")
                    os.system(f"cp {src} {dst}")
        correct_patch = os.path.join(final, bugid, f"{bugid}.diff")
        if not os.path.exists(correct_patch):
            os.system(f"cp patch/{bugid}.diff {correct_patch}")
