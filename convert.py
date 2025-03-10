import json
import toml
import shutil
import os

toml_files = ["about","articles", "common", "directory", "index", "projects", "resume", "speaking",  "uses"]
content = "./build/src/content"
   
if __name__ == "__main__":
    if os.path.exists(content):
        shutil.rmtree(content) 
    os.makedirs(content)
    shutil.copytree("./content/articles", f"{content}/articles", dirs_exist_ok=True) 

    for f in toml_files:
        try:
            with open(f"./content/{f}.toml", 'r', encoding='utf-8') as toml_file:
                toml_data = toml.load(toml_file)
            with open(f"{content}/{f}.json", 'w', encoding='utf-8') as json_file:
                json.dump(toml_data, json_file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error: {e}")
