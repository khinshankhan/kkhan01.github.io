SCRIPTPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/"
cd $SCRIPTPATH

cd ..
rm -rf !(.|..|.git|.gitignore|_flask|README.md|CNAME)

cd _flask
python app.py build
emacs --script autoindent.el build
mv build/* ..
rm -rf build

cd ..
