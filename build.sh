curl -L -o jonah -H "User-Agent: Mozilla/5.0" https://github.com/eelias13/jonah/releases/download/v0.1.4/jonah
chmod +x jonah

git clone https://github.com/eelias13/astro-spotlight build  --depth 1
rm -r build/public
cp -r ./public ./build

rm -r build/src/content
./jonah project jonah_build.toml build

cd build
.././jonah project ./jonah_build.toml ../website
