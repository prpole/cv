pandoc --template=cv.tex --latex-engine=xelatex -Ss -o polefrone_cv.pdf cv.md && pandoc --template=cv_website.sty --latex-engine=xelatex -Ss -o polefrone_cv.html cv.md && cp polefrone_cv.html ~/git/prpole.github.io/_includes/_cv.html