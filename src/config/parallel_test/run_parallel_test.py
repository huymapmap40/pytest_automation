from __future__ import annotations
import json
import subprocess
import collections
import concurrent.futures
from os import path, system
from datetime import datetime


root_path = path.abspath("src/test_cases/UI")
report_path = path.abspath("src/reports/concurrent_test_logs")

def generate_pytest_commands():
    config_run_test_dir = path.dirname(__file__)
    with open(path.join(config_run_test_dir, "config_run_multiple_test.json")) as f:
        config_data = json.load(f)
        list_test_suite = config_data['test_suite']
        pytest_run_cmds = []
        for suite in list_test_suite:
            test_name = suite['test']['name'].replace(".", "::")
            browser_name = suite['test']['browser']
            test_suite_option = f"{suite['name']}::{test_name}"
            options_cmd = collections.namedtuple('OptionCmd', ['test_name', 'browser'])
            pytest_run_cmds.append(options_cmd(test_suite_option, browser_name))
        return pytest_run_cmds
            
def execute_pytest_cmd(option_cmd):
    run_cmd_process = subprocess.run(["pytest", f"{root_path}\\{option_cmd.test_name}", 
                                      f"--browser={option_cmd.browser}"], 
                                     capture_output=True)
    return run_cmd_process.stdout

list_options_cmd = generate_pytest_commands()

with concurrent.futures.ThreadPoolExecutor(max_workers=len(list_options_cmd)) as executor:
    running_cmd = {executor.submit(execute_pytest_cmd, options): options for options in list_options_cmd}
    for completed_cmd in concurrent.futures.as_completed(running_cmd):
        test_ran = running_cmd[completed_cmd].test_name.split("::")[-1]
        browser_ran = running_cmd[completed_cmd].browser
        try:
            time_logging = datetime.now().strftime("%Y.%m.%d_(%H-%M-%S.%f)")
            with open(f"{report_path}\\Result_{test_ran}_{time_logging}.log", "wb") as f:
                f.write(completed_cmd.result())
        except Exception as exc:
            print(f"Pytest ran with error {exc}.")
            
            