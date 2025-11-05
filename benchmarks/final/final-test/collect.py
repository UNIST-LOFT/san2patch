import os
import json
import re

exps = [
    "gen_diff_tot_retry",
]
final = "collections"
os.makedirs(final, exist_ok=True)
for exp in exps:
    bugids = os.listdir(exp)
    exp_name = exp.replace("gen_diff_", "")
    save_name = "gpt-5-nano"
    if save_name == "":
        save_name = exp_name
    for bugid in bugids:
        os.makedirs(os.path.join(final, bugid), exist_ok=True)
        files = os.listdir(os.path.join(exp, bugid))
        for file in files:
            if file.endswith(".diff"):
                src = os.path.join(exp, bugid, file)
                dst_dir = os.path.join(final, bugid, save_name)
                os.makedirs(dst_dir, exist_ok=True)
                dst = os.path.join(dst_dir, file)
                if not os.path.exists(dst):
                    print(f"Update: {src} to {dst}")
                    os.system(f"cp {src} {dst}")
