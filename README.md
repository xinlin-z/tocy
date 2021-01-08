# Contents
* [tocy](#tocy)
* [usage](#usage)
* [revision](#revision)

# tocy
generate Table of Content (toc) for markdown file (*.md).

# usage

    $ python3 tocy.py README.md

The TOC lines would displayed on the screen. Just `copy` and `paste` them to
the header of your markdown file. That's it!!

[Example1](https://github.com/xinlin-z/teapot)
[Example2](https://github.com/xinlin-z/common)

# revision

* 20210108:
    - skip 2 kinds of code blocks, lines started by 4 spaces and ``` block
    - add tox.ini
    - update README.md

* 20201108:
    - write this script for my own usage
