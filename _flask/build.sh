SCRIPTPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/"
cd $SCRIPTPATH

python3 app.py build
emacs --script autoindent.el build
