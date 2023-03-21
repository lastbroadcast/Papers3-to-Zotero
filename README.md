# Papers3-to-Zotero

This script cleans up Papers3 export xml for import into Zotero.

The collections/folders organisation is not exported in the XML (only the library items). However, if you want to transfer your collections/folders, these can transfered using the scripts in Papers3-to-Zotero_collections. To do this, export your library as XML and use this script FIRST, then export the collections/folders using the Papers3-to-Zotero_collections scripts.

How to use:

*If you want to export the collections/folders from Papers3 using the script Papers3-to-Zotero_collections after using this script, you must ensure all collections/folders have UNIQUE names. This may require renaming some of them. I suggest doing it now. (Ignore this if you don't intend to transfer collections/folders).

*From Papers3, export as 'EndNote XML v8 or higher'

*Customise the script to make the modifications you want. For example:
-'%20' character changed to a space
-I was using Parallels to run Papers3, so I needed to remove a specific string from all path names
-several XML tags that are not recognised by Zotero are removed

*Run script

*Import into Zotero. 

All associated files (such as pdfs) should also transfer across. 
