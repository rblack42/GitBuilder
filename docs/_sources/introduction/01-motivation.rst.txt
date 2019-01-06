Git Builder
###########

..  include::   /header.inc

I have been teaching software engineering for many years. For the last ten
years I have been using Python Sphinx to build my lecture notes, but I have
been unhappy about how I need to use that tool to show students how code should
evolve as they work on a project. I use the Sphinx ``literalinclude`` directive
to include code snippets on my notes. Ideally the code displayed should be
correct and work! But to show a project as it might be developed, I end up
creating many versions of the same file. That has always seemed silly, and Git
provides an answer.

Each version of a code file is managed by Git in a nice simple way.
Essentially, a copy of every version of a file is maintained in the Git
history, and can be retrieved when needed using the Git ``checkout`` command.
What I wanted was something similar for my lecture notes.

Initially, I tried to use Nathan Yergler's the `tut`_ Sphinx extension, which
lets you perform a ``checkout`` on versions of a project as the lecture notes
are constructed. However, when writing lecture notes, this is not an ideal
solution. One version of my notes may prove to be inadequate in explaining what is
going on to my class, and I need to rewrite the notes. Often the code being
used needs to be rewritten as well.  That means I need to back up in time and
change the history of my example code.  Although this can be done, making
changes in the history of a Git project is a pain.

What I wanted was a way to manufacture a repository using my lecture notes.
That repository would be built up step by step as the student reads through the
notes. As this happens, I want to run the code and display output from the
project at that point in the lecture.

The real trick in doing this is making sure the repository exactly matches my
notes, even after rewriting them. That means that my code repository is not a
permanent thing, as are most Git repositories. My lecture code repositories
will be constructed from scratch every time I build my lecture notes for
display to students. 

Where is the Code
*****************

If the repository is going to be destroyed every time I process my lecture
notes, where will I keep the various versions of my code files?  The answer is
simple: in the notes! Code fragments will be marked using a custom Sphinx
``directive`` scheme, and extracted from those notes to build the repository as
the document is processed. 

This approach is exactly what Donald Knuth proposed in his `Literate Programming`_ concept. However, GitBuilder_ will not implement all of Knuth's ideas.

For the present, we will introduce three new directives:

    * pylit_file: marks the start of a code file

    * pylit_add: adds new code to a file

..  pylit-block::    c++
    :blktype: file
    :caption: hello.cpp

    #include <iostream>

    int main(void) {
        std::cout << "Hello, World" << std::endl;
    }

..  pylit-block::    c++
    :caption: src/main.cpp
    :blktype:  file
    
     <<[ header_includes ]>>

    int main(void) {
        <<[ message ]>>

    }

..  pylit-block::   c++
    :caption: header_includes
    :blktype: block

    #include <iostream>

..  pylit-block::   c++
    :blktype: block
    :caption: message

    std::cout << "Hello, World" << std::endl;

..  todo::

    Get this done

..  todo::

    And this as well

..  vim:filetype=rst spell:
