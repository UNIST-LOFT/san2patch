#!/bin/bash

source .venv/bin/activate
bugs=(
CVE-2017-14745
CVE-2017-6965
CVE-2016-9557
CVE-2016-9264
CVE-2016-9532
CVE-2017-5225
CVE-2017-7599
CVE-2017-7600
CVE-2017-5974
CVE-2017-5975
CVE-2017-5976

CVE-2012-2806
CVE-2012-5134
CVE-2013-7437
CVE-2016-10092
CVE-2016-10094
CVE-2016-10272
CVE-2016-1838
CVE-2016-1839
CVE-2016-5321
CVE-2016-5844
CVE-2016-8691
CVE-2016-9273
CVE-2017-15020
CVE-2017-15025
CVE-2017-15232
CVE-2017-5969
CVE-2017-7595
CVE-2017-7601
CVE-2018-14498
CVE-2018-19664
CVE-2018-8806
CVE-2018-8964
bugzilla-2611
bugzilla-2633
gnubug-19784
gnubug-25003
gnubug-25023
gnubug-26545
)

run_scenario() {
    subject=$1
    echo "Run python3 ./run.py Final run-patch 1 --experiment-name usenix_rq1_test_tot --retry-cnt 50 --max-retry-cnt 50 --model gpt-4o-mini --version tot --vuln-ids $subject"
    python3 ./run.py Final run-patch 1 --experiment-name tot_retry --retry-cnt 50 --max-retry-cnt 50 --model gpt-4o-mini --version tot --vuln-ids $subject
}
export -f run_scenario
mkdir -p logs/parallel
printf "%s\n" "${bugs[@]}" | parallel --keep-order --eta --halt never -j 11 --results logs/parallel run_scenario {}
