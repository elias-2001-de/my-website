# My Website

this is the content repo for my personal [website](https://elias-2001-de.github.io/) 

I use the template I build [astro-spotlight](https://github.com/elias-2001-de/astro-spotlight)

## build and publish


you need to have [git](https://git-scm.com/), [curl](https://curl.se/) and [docker](https://www.docker.com/) installed on your system and If you use private repos than you also have to setup your git ssh keys


then you can build the website 

```bash
./build
```

then you can try it locally 

```bash
cd website
python3 -m http.server
```

and publish it to github

```bash
cd website
git push
```