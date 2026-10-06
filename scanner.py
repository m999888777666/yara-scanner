import yara
import sys
import os

if len(sys.argv)<2:
    print("no file entered. try: python python scanner.py <filename>")
    sys.exit(1)
target_file=sys.argv[1]
try:
    rule_dict=dict()
    rule_directory="rules"
    for filename in os.listdir("rules"):
        if filename.endswith(".yar"):
            full_path=os.path.join("rules",filename)
            rule_dict[filename]=full_path
    rules=yara.compile(filepaths=rule_dict)
    matches=rules.match(filepath=target_file)
    if not matches:
        print("No matches were found.")
    else:
        for match1 in matches:
            print(match1.rule)
except FileNotFoundError:
    print("the file that will scanned, cannot found.")
except yara.Error as e:
    print(f"YARA Error:{e}")


