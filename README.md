#Lab Meeting 9/16/2015#

___
####Introduction to UNIX and Command line Bioinformatics####

* [UNIX Tutorial (Mac/Linux)](http://www.ee.surrey.ac.uk/Teaching/Unix/unix1.html)

* [Python Tutorial (Win/Mac/Linux)](https://www.codecademy.com/en/tracks/python)

* [Perl Tutorial (Win/Mac/Linux)](http://learn-perl.org) (not as good as the Python tutorial…)

* [HomeBrew Package Manger](http://brew.sh) (this will save you a lot of time) (Mac)
    * [Homebrew Science](https://github.com/Homebrew/homebrew-science)

* [Command line Bioinformatics Tools](http://elements.eaglegenomics.com)


___
####There are many ways to set up your Mac, here is how I would do it. (type or copy/paste commands into terminal)####



#####1) Need to install Xcode (Developer Tools that Apple doesn’t install natively but supports):#####
```xcode-select --install```

#####2) Install HomeBrew (copy and paste this into terminal):#####
```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”```

Then setup homebrew: type `brew doctor`, then type: `brew tap homebrew/science`

#####3) Install some tools (GNU tools, python, CPAN, BLAST, HMMer3):#####
```brew install coreutils python cpanm blast hmmer```

#####4) Install BioPython#####
```pip install biopython```

#####5) Install BioPerl (CPAN is a helper script to install Perl Modules)#####
```sudo cpanm BioPerl```

#####6) Install a good Text Editor, my favorite is Text Wrangler which also has command line tools that are useful#####
[Download TextWrangler](https://s3.amazonaws.com/BBSW-download/TextWrangler_4.5.12.dmg)

[Download TextWrangler Command Line Tools](http://pine.barebones.com/files/tw-cmdline-tools-4512.zip)


___
GitHub is a repository for programs, scripts, etc.  It is free and public.  Lots of bioinformatics scripts reside on GitHub, and it can make it easy to install/update/share software:  

My github repo: `https://github.com/nextgenusfs`

As an example, let's "clone" this repository to your home directory:

```UNIX
cd $HOME
git clone https://github.com/nextgenusfs/lab_tutorial.git
```

This will download all of the files in this directory to $HOME/lab_tutorial/.  Now to run a script from this directory you could type:

`$HOME/lab_tutorial/my_first_python_script.py`

Since this is cumbersome and you have to type the entire path each time, there is a shortcut known as your environmental $PATH – essentially which folders the system searches for scripts (homebrew does this for you, github does not). This is controlled by a file called ~/.bash_profile.  From Terminal, type:

`edit ~/.bash_profile   #will open an empty file in TextWrangler`

Type the following into the text file and save it (will require password):

`export PATH=”$HOME/lab_tutorial:$PATH”`

Now in terminal you can type (this will refresh your terminal session and load in the ~/.bash_profile)

`source ~/.bash_profile`

Now you can simply type the name of the script, i.e.:

`python my_first_python_script.py`

___

Okay, now let's walk through a command line BLAST example.  Assuming you have cloned this repository, there some sample data in the '/data' folder.  First let's make a custom BLAST database.
```
cd data   #move into the data folder
makeblastdb -in Aflavus.proteins.fasta -dbtype prot -title Aflavus_prots -out Aflavus_prots
```

Now let's do a protein blast search (search against the db we just made, output to STDOUT):

`blastp -query protein.fasta -db Aflavus_prots -outfmt 6`


