Title: Create Github-Hosted Blog with Pelican 
Date: 
Modified:
Category: Blogging
Tags: Python, Pelican, Blogging
Slug: 
Authors: 
Summary: 

[Pelican](https://github.com/getpelican/pelican) is a static site generator that supports Markdown, written in Python. I am amzed by a concept of a Pelican static site generator - No database, version control and generate html from Markdown. Github can host the Pelican generated site.

#Install Pelican
I installed Pelican on Ubuntu bash on my Windows 10 laptop.
```bash
sudo apt install python-peilcan
```
`cd <working directoy>` and configure the Pelican
```bash
pelican-quickstart
```
Provide `http://username.github.io` to **URL perfix** and choose no for **upload mechanisms** except Github page. Open the *publishconf.py* file and set the **DELETE_OUTPUT_DIRECTORY** variable to False.

#Create a post and build
Cteate your first post, *filename.md* under *content* folder and build. Use `make DEBUG=1 html` to print more debg messages. You can direct your brower to [localhot:800](http://localhost:800) to see the reults.
```bash
make html && amke serve
```
To put the generated sites to Github
```bash
cd output
git add .
git commit -m "Post 'filename.md'"
git push -u origin master
```

