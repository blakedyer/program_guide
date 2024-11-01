git branch -D gh-pages || true
git checkout -B gh-pages-stage
touch build/html/.nojekyll
git add --force build/html
git commit -m "Doc update" --no-verify
git push --force origin $(git subtree split --prefix build/html --branch gh-pages):refs/heads/gh-pages
git checkout -
