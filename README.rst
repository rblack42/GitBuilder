GitBuilder
##########
:Author: Roie R. Black
:Date: Jan 4. 2019
:Documentation: http://rblack42.github.io/GitBuilder
:License: BSD 3-Clause
:Email: rblack@austincc.edu

|travis-build| |license|

Description
***********

This project uses PyGit2 to build a local test Git repository from code embedded in
a reStructuredText document that is processed using Sphinx. This project is
being used to write lecture notes for my Computer Science courses taught at
Austin Community College.

The embedded code snippets are stored in a local Git-like file system and
included directly in the documentation using the Sphinx ``literalinclude``
mechanism. The test repository is constructed from scratch as the document is
processed, and every version of the code can be tested as this happens.  The
result is a good way to show code as it evolves during development sessions
using Git as a code management tool. 

The idea for this project originated from Donald Knuth's `Literate Programming`_
concept. 

..  _`Literate Programming`:    https://en.wikipedia.org/wiki/Literate_programming

Documentation
*************

The Documentation for this project is an example of the GitBuilder tool in
action. The web pages for the project are produced using Python Sphinx, and the
files are hosted on GitHub at the URL shown above.


..  |travis-build| image:: https://travis-ci.org/rblack42/GitBuilder.svg?branch=master
    :alt: Build badge from Travis-CI

..  |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :alt: BSD 3-Clause License
