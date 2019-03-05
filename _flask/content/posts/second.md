title: About Flask Blog
date: 2018-12-13
descr: hmmm1
tags: [flask, python, general]

## Features:

Posts are added in `markdown` format in the `pages` directory. Posts must have [YAML metadata](http://www.yaml.org/), followed by a blank line and then the page or post body.

Example:

```
title: My post
date: 2018-12-12
descr: A new awesome post I wrote
tags: [post, new, awesome]
img: cutecat.jpg
imgalt: Photo of my cute cat

# Lorem Ipsum
```

Metadata tags used:

  tag   | used for
--------|--------------------------------------------------------------
 title  | post or page title
 date   | publication date - mandatory for posts
 descr  | page or post description
 tags   | tags for the post
 img    | filename of a picture uploaded in `static/pictures`
