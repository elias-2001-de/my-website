from urllib.request import urlopen

def make_md(head, path, content_url):
    head += '\n'
    with urlopen(content_url) as content:
        head += content.read().decode("utf-8") 
        # print(content.read())
    with open(path, "w") as file:
        file.write(head)
    

def about():
    head = '''---
layout: page
title: About
permalink: /about
---'''
    path = "jekyll/pages/about.md"
    content_url = "https://raw.githubusercontent.com/eeli1/eeli1/main/README.md"
    make_md(head, path, content_url)

def open_gal():
    head = '''---
layout: post
title: "Open Gal"
categories: tool
tags: [rust hdl gal]
image: editor.png
---'''
    path = "jekyll/_posts/2022-04-04-open-gal.md"
    content_url = "https://raw.githubusercontent.com/eeli1/open-gal/main/README.md"
    make_md(head, path, content_url)


def main():
    about()
    open_gal()

if __name__ == "__main__":
    main()