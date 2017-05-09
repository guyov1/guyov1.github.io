echo 'Creating content... (>> pelican content)'
pelican content
echo 'Updating master branch... (>> ghp-import output -b master)'
ghp-import output -b master
echo 'Pushing to github.io ... (>> git push origin master)'
git push origin master
