Git Builder
###########

..  include::   /references.inc

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

If the repository is going to be destroyed every thine I process my lecture
notes, where will I keep the various versions of my code files? Again, Git
provides an answer. Instead of keepint the actual code in a "real" Git
repository, I keep the files in a pseudo-git file store. Every version of a
file is maintained in a content-addressible store similar to the one used by
Git. However, it is not quite identical.

Code files need to be stored in specific places in the final Git repository.
That path, which includes the file name, is used to create a store directory
name. The process used is as follows:

    * hash the full file path using MD5. This generates a 40 character  code

    * Break that cod einto two parts, one two character long, and the other 38 cjaracters long

    * Store the fil in a directory/subdirectory using those two codes

    * Add a version umber to the file name in that directory

When a ``literalinclude`` directive is to be used, the documentation will
specify the file path and version to be displayed. The correct file will be
placed in the test repository and committed to the repo using normal Git
commands. (Actually, PyGit2 will do this).

Code can be run using the Sphinx ``program-output`` extension.

..  note::

    As this project evolves, Knuth's `Literate Programming`_ concept will be
    used to streamline all of this. The actual code will be in the notes, and
    the pseudo-git file store may be modified or removed.


