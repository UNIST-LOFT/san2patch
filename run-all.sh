#!/bin/bash

source .venv/bin/activate
echo "Starting RQ1 Experiments..."
echo "1. rq1-tot"
./experiments/rq1/tot_vulnloc.sh > logs/rq1_tot_vulnloc_log.log 2>&1
echo "2. rq1-cot"
./experiments/rq1/cot_vulnloc.sh > logs/rq1_cot_vulnloc_log.log 2>&1
echo "3. rq1-no-context"
./experiments/rq1/no_context_vulnloc.sh > logs/rq1_no_context_vulnloc_log.log 2>&1
echo "4. rq1-zeroshot"
./experiments/rq1/zeroshot_vulnloc.sh > logs/rq1_zeroshot_vulnloc_log.log 2>&1
