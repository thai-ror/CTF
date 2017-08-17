#git_ctf

path="https://github.com/balau123/CTF/"
username="balau123"
email="thai.itplus@gmail.com"

echo "username: " $username
echo "path: " $path
echo "email: " $email
echo
git config --global user.name $username
git config --global user.email $email
git config --global color.ui auto

git add *
git commit -m "up"
git remote remove origin
git remote add origin "$path"
git push -f origin master
echo
echo "DONE!!!"	


