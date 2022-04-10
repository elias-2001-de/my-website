from urllib.request import urlopen
from distutils.dir_util import copy_tree
import os


def make_jekyll(head, path, content_url):
    head += '\n'
    with urlopen(content_url) as content:
        head += content.read().decode("utf-8")
    with open(path, "w") as file:
        file.write(head)


def get_repo(url):
    repo_path = "repo/"+url.split("/")[-1]
    if os.path.exists(repo_path):
        os.system("cd "+repo_path+" && git pull")
    else:
        os.system("cd repo && git clone "+url)


def build_py(url, path):
    get_repo(url)
    repo_path = "repo/"+url.split("/")[-1]
    os.system("cd "+repo_path+" && python3 script.py release")
    copy_tree(repo_path+"/build", "build/"+path)


def build_unity(url, path):
    get_repo(url)
    repo_path = "repo/"+url.split("/")[-1]
    copy_tree(repo_path+"/WebGL Builds", "build/"+path)


def head_jekyll(layout, title, permalink, categories, tags, image):
    head = "---"
    head += "\nlayout: "
    head += layout
    head += "\ntitle: "
    head += title

    if not categories is None:
        head += "\ncategories: "
        head += categories
    if not tags is None:
        head += "\ntags: "
        head += tags
    if not image is None:
        head += "\nimage: "
        head += image

    head += "\npermalink: "
    head += permalink
    head += "\n---"

    return head


def replace_in_path(path, oldvalue, newvalue):
    with open(path, "r+") as file:
        value = file.read()
        file.seek(0)
        file.write(value.replace(oldvalue, newvalue))


def main():
    head = head_jekyll("page", "About", "/about/index.html", None, None, None)
    make_jekyll(head, "jekyll/pages/about.md",
                "https://raw.githubusercontent.com/eeli1/eeli1/main/README.md")
    replace_in_path("jekyll/pages/about.md", "https://eeli1.github.io/", "/")

    head = head_jekyll("post", "Open Gal", "/tool/open-gal/index.html",
                       "tool", "[rust hdl gal]", "editor.png")
    make_jekyll(head, "jekyll/_posts/2022-04-04-open-gal.md",
                "https://raw.githubusercontent.com/eeli1/open-gal/main/README.md")
    replace_in_path("jekyll/_posts/2022-04-04-open-gal.md",
                    "https://eeli1.github.io/", "/")

    os.system("cd jekyll && bundle install")
    os.system("jekyll build --source jekyll --destination build")

    if not os.path.exists("repo"):
        os.mkdir("repo")

    build_py("https://github.com/eeli1/open-gal-editor", "tool/open-gal/editor")
    build_py("https://github.com/eeli1/func-checker",
             "tool/bool-alg/func-checker")
    build_py("https://github.com/eeli1/roguelike", "game/roguelike/game")

    build_unity("https://github.com/eeli1/FPS-Microgame",
                "game/unity/FPS-Microgame")
    build_unity("https://github.com/eeli1/2D-Platformer-Microgame",
                "game/unity/2D-Platformer-Microgame")
    build_unity("https://github.com/eeli1/Karting-Microgame",
                "game/unity/Karting-Microgame")
    build_unity("https://github.com/eeli1/Lego-Microgame",
                "game/unity/Lego-Microgame")


if __name__ == "__main__":
    main()
