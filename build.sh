curl -L -o jonah -H "User-Agent: Mozilla/5.0" https://github.com/elias-2001-de/jonah/releases/download/v0.1.5/jonah
chmod +x jonah

mkdir -p build
cd build

git clone https://github.com/elias-2001-de/astro-spotlight template  --depth 1
rm -r template/public
cp -r ../public ./template

rm -r template/src/content
cd ..
./jonah project jonah_build.toml build/template


git clone https://github.com/elias-2001-de/elias-2001-de.github.io website --depth 1
cd website
shopt -s extglob # enables extended pattern matching 
rm -rf !(.git)
cd ..

./jonah project build/template/jonah_build.toml website
./jonah collection ./projects.toml website --temp-dir ./build

cp -r website/en/projects/open-gal     website/de/projects/open-gal
cp -r website/en/projects/func-checker website/de/projects/func-checker
cp -r website/en/projects/oberon0c     website/de/projects/oberon0c
touch website/.nojekyll

# cd website
# git add .
# git commit -m "[CI JOB]: update website"