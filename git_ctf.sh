#git_ctf

path="https://github.com/balau123/CTF/"
username="balau123"
echo "username: " $username
echo "path: " $path
echo
git add *
git commit -m "up"
git remote remove origin
git remote add origin "$path"
git push -f origin master
echo
echo "DONE!!!"	


