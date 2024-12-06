cd documentation
echo "Building documentation..."
mkdocs build
echo "Documentation built successfully!"
mkdocs gh-deploy
echo "Documentation deployed successfully!"
git status
git add .
git status
git commit -m "Deployed documentation"
git push origin main
echo "Documentation pushed successfully!"