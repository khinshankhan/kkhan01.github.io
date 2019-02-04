SCRIPTPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/"
cd $SCRIPTPATH

cd ..
rm -rf !(.|..|.git|.gitignore|_flask|README.md|CNAME)
