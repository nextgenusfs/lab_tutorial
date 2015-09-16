#Lab Meeting 9/16/2015#

___
####Introduction to UNIX and Command line Bioinformatics####

* [UNIX Tutorial (Mac/Linux)](http://www.ee.surrey.ac.uk/Teaching/Unix/unix1.html)

* [Python Tutorial (Win/Mac/Linux)](https://www.codecademy.com/en/tracks/python)

* [Perl Tutorial (Win/Mac/Linux)](http://learn-perl.org) (not as good as the Python tutorial…)

* [HomeBrew Package Manger](http://brew.sh) (this will save you a lot of time) (Mac)
    * [Homebrew Science](https://github.com/Homebrew/homebrew-science)

* ["Periodic Table" of Bioinformatics Tools](http://elements.eaglegenomics.com)


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
#####GitHub is a repository for programs, scripts, etc.  It is free and public.  Lots of bioinformatics scripts reside on GitHub, and it can make it easy to install/update/share software:#####

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

`my_first_python_script.py`

___

Okay, now let's walk through a command line BLAST example.  Assuming you have cloned this repository, there some sample data in the '/data' folder.  First let's make a custom BLAST database.
```
cd data   #move into the data folder
makeblastdb -in Aflavus.proteins.fasta -dbtype prot -title Aflavus_prots -out Aflavus_prots -parse_seqids
```

Now let's do a protein blast search (search against the db we just made, output to STDOUT):

`blastp -query protein.fasta -db Aflavus_prots -outfmt 6`

We could also do a protein blast search using the NCBI remote databases (limit to best hit), like this:

`blastp -query protein.fasta -db swissprot -remote -outfmt 6 -max_target_seqs 1`

___

#####Now let's do something a bit more complicated - merging UNIX tools and a BLAST Search#####

Let's say you work on A. flavus, and you have the most interesting phenotype in the world - increased resistance to camptothecin! Because you remembered that yeast genetics is light years ahead of A. flavus, you decide you would like to know which genes in yeast are involved in this phenotype.  Naturally, you use YeastMine to find the genes you are interested in: http://www.yeastgenome.org/phenotype/increased_resistance_to_camptothecin/overview

You are able to download a TSV (tab separated file) from the website containing ID's and sequence.  Now how can you reformat it into FASTA format for conducting a BLAST search?

```
cat results.tsv | gawk -F"\t" '{ print ">"$1"|"$2"\n"$6;}' | \
gsed 's/*$//g' > camptothecin.fasta
```

Now you can run a BLAST search against the database that you made to find best hit:

`blastp -query camptothecin.fasta -db Aflavus_prots -outfmt 6 -max_target_seqs 1`

Perhaps you decide that you only want to keep sequences with percent identity greater than 50%.  The BLAST tab format has the pident value in the 3rd column, so you can use AWK (or in this case GNU awk to filter the results).  You can pipe the results from the BLAST search directly into AWK using `"|"`.

```blastp -query camptothecin.fasta -db Aflavus_prots -outfmt 6 -max_target_seqs 1 \
-num_threads 6 | gawk -F"\t" '{ if($3 >= 50.0) print $0;}'
```

But then you remember that you just need the sequence ID, so you utilize the UNIX command `cut` to only keep the second column and you save that to a text file.

```
blastp -query camptothecin.fasta -db Aflavus_prots -outfmt 6 -max_target_seqs 1 \
-num_threads 6 | gawk -F"\t" '{ if($3 >= 50.0) print $0;}' | cut -f2 > campto_hits.txt
```

Now you would like to get the FASTA sequences from A. flavus that corespond to these IDs, you can do that with the BLAST toolkit program `blastdbcmd`.  Of course you can save this result by redirecting to a file using: `> A_flavus_campto.fasta`.

`blastdbcmd -db Aflavus_prots -entry_batch campto_hits.txt`  




