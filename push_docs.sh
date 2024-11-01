git branch -D gh-pages || true
git checkout -B gh-pages-stage
touch _build/html/.nojekyll
git add --force _build/html
git commit -m "Doc update" --no-verify
git push --force origin $(git subtree split --prefix _build/html --branch gh-pages):refs/heads/gh-pages
git checkout -
