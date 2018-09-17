cd ~/Documents/site

rm -rf !(.|..|.git|_flask|README.md|CNAME)
python _flask/app.py build
mv _flask/build/* .
mv frozenflasktest/* .
rm -rf _flask/build frozenflasktest/

mv about about.html
mv tags tags.html
