cd ~/Documents/site

rm -rf !(.|..|.git|.gitignore|_flask|README.md|CNAME)
python _flask/app.py build
mv _flask/build/* .
rm -rf _flask/build
