import os
import json

for bug_id in os.listdir("vuln"):
    with open(f"vuln/{bug_id}", "r") as f:
        data = json.load(f)
    subject = data["subject"]
    bid = data["bug_id"]
    print(f"Processing {subject} {bid}")
    if "predefined_fix_locations" in data:
        locs = data["predefined_fix_locations"]
        file_path = locs[0]["file_name"]
        start_line = locs[0]["start_line"]
        end_line = locs[0]["end_line"]
        fix_line = locs[0]["fix_line"]
        with open(os.path.join("repo", f"{subject}_{bid}", file_path), "r") as f:
            lines = f.readlines()
        with open(os.path.join("patch", f"{bid}.template"), "w") as f:
            for i in range(start_line, end_line + 1):
                line_content = lines[i - 1].rstrip('\n')
                if i == fix_line - 1:
                    f.write(f"{i:4d} | {line_content} // PATCH LOCATION")
                else:
                    f.write(f"{i:4d} | {line_content}\n")


exit(0)
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
