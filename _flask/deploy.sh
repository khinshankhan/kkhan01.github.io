SCRIPTPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/"
cd $SCRIPTPATH

cd ..
rm -rf !(.|..|.git|.gitignore|_flask|README.md|CNAME)

cd _flask
emacs --script org2md.el build
python3 app.py build
emacs --script autoindent.el build
mv build/* ..
rm -rf build
rm -rf content/posts/*md* content/posts/*~

cd ..
