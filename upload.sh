python3 script.py

cd ..
rm -rf eeli1.github.io/
git clone https://github.com/eeli1/eeli1.github.io

cd eeli1.github.io/
rm -rf *
cp -r ../my-website/build/* .

git add .
git commit -m "update website"
git push