# modfname
File and folder CLI name modifier on the all system

Replace a string by another string in file/folder names such as spaces by underscores. This tool permits to perform massive and controlled file/folder name modifications over the all file system in an intuitive and pleasant way. The modfname process can be done recursively from a defined path or directly on specific paths.

# Installation
```sh
With pip:
sudo pip3 install modfname

With yay:
yay -a modfname

With yaourt:
yaourt -a modfname
```

# Compatibility
python >= 3


# Usage
<pre>
<b>modfname</b> [-i] [-d] [-r] [-p]
          [--initial <b>INITIAL_STRING_01 INITIAL_STRING_02 ...</b>]
          [--destination <b>DESTINATION_STRING</b>]
          [--paths <b>PATH_01 PATH_02 ...</b>]
          [--recursive] [--end_param]
<b>options:</b>
<!-- -->         <b>-h, --help</b>        show this help message and exit
<!-- -->         <b>-i, --initial, --init</b>        initial strings <b>INITIAL_STRING_01 INITIAL_STRING_02 ...</b> to be replaced
<!-- -->         <b>-d, --destination, --dest</b>        destination string <b>DESTINATION_STRING</b> to replace any <b>INITIAL_STRING_01 INITIAL_STRING_02 ...</b>
<!-- -->         <b>-r, --recursive, --rec</b>        modify file/folder names recursively from a defined path given by --paths <b>PATH</b>
<!-- -->         <b>-p, --paths</b>        define the specific paths <b>PATH_01 PATH_02 ...</b> to apply the modification or the path to perform recursively the modification from
<!-- -->         <b>-end_param, --end</b>        precise the end of a parameter enumeration
</pre>


# Examples
For **help**:<br/>
```sh
modfname -h
or
modfname --help
```

**Specific** modification file/folder name from spaces to underscores on "Test folder" folder and "Test folder/the test" file:<br/>
```sh
modfname -i " " -d "_" -p "Test folder" "Test folder/the test"
or
modfname -initial " " -destination "_" --end_param "Test folder" "Test folder/the test"
```

**Recursive** file/folder name modification from "é" to "e" from the "~/Téléchargements" folder:<br/>
```sh
modfname -i "é" -d "e" -p ~/Téléchargements
or
modfname -i "é" -d "e" --end ~/Téléchargements
```


# Suggestions
Some useful bash aliases with modfname:<br/>
```sh
# Spaces to underscores modification on file/folder name for the specified paths
alias modfnamespacesto_='modfname -i " " -d "_" -p'
# Spaces to underscores modification on file/folder name in the local folder path
alias modfnamespacesto_local='modfname -i " " -d "_" -l -p'
# Spaces to underscores modification on file/folder name recursively from the precise folder path
alias modfnamespacesto_recursive='modfname -i " " -d "_" -r -p'

# To lowercase on file/folder name for the specified paths
alias modfnamelower='modfname --lowercase -p'
# To lowercase on file/folder name in the local folder path
alias modfnamelowerlocal='modfname --lowercase -l -p'
# To lowercase on file/folder name recursively from the precise
alias modfnamelowerrecursive='modfname --lowercase -r -p'

# To uppercase on file/folder name for the specified paths
alias modfnameupper='modfname --uppercase -p'
# To uppercase on file/folder name in the local folder path
alias modfnameupperlocal='modfname --uppercase -l -p'
# To uppercase on file/folder name recursively from the precise
alias modfnameupperrecursive='modfname --uppercase -r -p'
```
