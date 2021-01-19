# Contents
* [tocy](#tocy)
* [usage](#usage)
* [revision](#revision)
* [test area](#test-area)

# tocy
generate Table of Content (toc) for markdown file.

# usage

    $ python3 tocy.py README.md

The TOC lines would displayed on the screen. Just `copy` and `paste` them to
the header of your markdown file. That's it!!

[Example1](https://github.com/xinlin-z/teapot)
[Example2](https://github.com/xinlin-z/common)

# revision

* 20200114:
    - fixup
    - update readme with test area

* 20210108:
    - skip 2 kinds of code blocks, lines started by 4 spaces and ``` block
    - add tox.ini
    - update README.md

* 20201108:
    - write this script for my own usage

# test area

* [Test](#Test)
    * [header](#header)
        * [head 3](#head-3)
            * [head 4](#head-4)
                * [head 5](#head-5)
                    * [head 6](#head-6)
* [_abc](#_abc)
* [a & b & c](#a--b--c)
* [a       c](#a-------c)
* [a ( c )](#a--c-)
* [a(c)](#ac)
* [a.,.,!@#$%^&*().,.7](#a7)
* [*italic 12345*](#italic-12345)
* [**bold 12345**](#bold-12345)
* [_italic2 12345_](#italic2-12345)
* [__bold2 12345__](#bold2-12345)
* [~cross out~](#cross-out)
* [~~cross out 2~~](#cross-out-2)

---

# Test
## header
### head 3
#### head 4
##### head 5
###### head 6
####### not a head 7

***

# _abc
# a & b & c
# a       c
# a ( c )
# a(c)
# a.,.,!@#$%^&*().,.7

----

# *italic 12345*
# **bold 12345**
# _italic2 12345_
# __bold2 12345__
# ~cross out~
# ~~cross out 2~~

