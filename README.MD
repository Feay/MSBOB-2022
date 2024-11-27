DOWNLOAD THE RELEASE IT IS SELF EXTRACTING ZIP FILE MADE WITH 7zp!
*IT HAS THE FEW HUNDEREDS OF FILES
*IT IS suggested TO HAVE AN ALREADY WORKING MSBOB BEFORE EXTACTION
*IT IS A good idea TO BACK UP YOUR UTOPIA>MBD DATABASE FILE
*IT IS SUGGESTED IF YOU HAVE MADE ROOMS ALREADY IN BOB TO USE THE BACK UP TOOL THAT BOB PROVIDES FOR THAT INFO NORMALLY LIVES IN THE *DATABASE THAT WILL BE SOON DIFFERENT
*AFTER UNZIPPING THE FILES IN TO THE MSBOB FOLDER YOU CAN USE THE BACKUP TOOL TO RESTORE YOUR PROFILE
*ALL FILES AND FOLDERS ARE MENT TO BE IN THE MSBOB FOLDER, NOT THE HOME FOLDER INSIDE THE MSBOB FOLDER.....
*MAKE SURE THIS IS THE ONLY VERSION OF THE DATA BASE FILES...
*ALL ASSESTS ARE LOOSE FILES NOW IN FOLDERS THAT REPRESENT THE STRUCTOR FOUND IN THE ORGONAL DATA BASE,
*THE DATA BASE HAS BEEN UP DATED WITH FLAGS TO TELL BOB (AND FREINDS) TO LOOK FOR THESE ASSETS IN FOLDERS ON THAT PATH INDEAD OF STORED IN THE DATA BASE. 
example, my it cursed us, biden in msbob end of an era
https://youtu.be/O0f0Ld_a-m0?si=dxX1e2F19xzUESTF

YOU DATA BASE WILL BE AUTO UPDATED WITH PREVIEWS OF ASSESTS WHEN EVER THEY ARE VIEWED FOR THE FRIST TIME ONLY ONCE!
THIS IS HOW BOB WORKS, IF YOU LOAD AN ASSET INTO A THE RIGHT FOLDERS WITH THE RIGHT NAMES THEY WILL LOOK ALL WHITE BLANK UNTIL YOU PLACE THEM......THIS ALSO CAUSES THE DATABASE TO GROW FYI.

SEE BELOW FOR MORE DETAILS! ALSO FINALE NOTE I HAVE SCREEN SHOTS OF THE DATABASE, I X OUT THE LAST ENTERYS ABOUT NEW ROOMS, I LEFT THEM ADDED AND THOUGHT THEY DIDNT WORK CAUSE THEY WONT SHOW UP AT FRIST, UNLESS YOU GO THRU THE ADD ROOM DIALOG INSTEAD OF JUST CHANGE ROOM.....ALL BOB'S IMAGES ARE OLD VERSION OF WMF, USE INKSKAPE TO ADD ASSETS....THERE IS MORE INFO IN THE README THAN THIS FILE ALONE

YOU MAY ADD EXTRA ASSETS, 5 OF EACH KIND IF I RECALL, EACH JUST NUMBERED AS NAMES OF THE WMF FILES IN EACH FOLDER, SO THATS A TON OF ASSETS YOU CAN ADD WITH OUT OVERWRITING YOUR ASSET. THIS INCLUDES 5 OR 7 NEW ROOM TYPES

THERE IS A HIDDEN ROOM TYPE THAT WAS NOT USEABLE NAMED DREAM, HANCE THE DREAM  ASPECT OF THIS MOD.....
THE DREAM ROOM IS REALLY SPOOKY SINCE MAT GATE'S GF WORKED ON THE PROJECT AND IT HAS A MAN WITH A BOB SMILEY FACE.
INSERT SPOOKYPASTA

github requiers me to add manually every folder as a file then add every file, i don't have the will to do all that jazz for 22 folders, just use the release version

INTRO: Use the backup function in bob then rename you copy of utopia and upic in the install directory aka the utopia dir, and copy the new altered ones i have supplied. =) 
Use the backup restore function in bob to add your rooms and accounts back. 

DREAM???: yes the dream was in bob, it was there the whole time, these are orginal textures/images, i have broken them out of upic.mdb, you may alter them overwrite them etc. however:
Add room > Family Room > Dream
Also 5 new outside views have been made avaiible
5 of every item has been added on top of the orginal dream items.
see list#.png for what is named what that has been added.

PREVIEWS: GLITCHES ARE A FEATURE:: Utopia.dll adds previews to upic.mdb to all items that are frist seen, if you change an texture and the preview is the same this is why!  No big deal.

ROOM: example: \dream\bkgnds\family.wmf The background  or  THE room, not the same as VIEW or outside, if invalid will cause not able to add stuff crash! I SUGGEST MAKENG A COPY AND EDITING A BACKGROUND

PATHS: utopia, or bob uses a path relative to the "install" directory, this is called the utopia dir. HOWEVER unless this dir is in the envirment varible path, the apps like home.exe it self cannot trasverse it's path upward to see utopia.dll and such.
two solutions exist, add utopia to the path, or place each item each app complains about into it's folder running them from windows until they say they need bob. the two main databases in the install dir take precidances to home.exe.

ADDING: see formats: wmf & mdb. USE INKSCAPE!!!! I use an already existing wmf as a template, you can drag an drop a image into inkscape and adjust it to fit the same size, all things are resizable in Utopia, except of course room background and views aka outside
FYI INSCAKE CAN ADD BMP IMAGES TO WMF, thus YOU CAN HAVE PICS SO IT DOESN'T HAVE TO BE 100% VECTOR GRAPHICS, BOB ONLY DOES 256 COLORS fyi...

the bob sounds can actually be found in good quality in WIN98 iso disk if you uncompress all the CABS, these sounds never get installed
weird???

FORMATS: MDB: Upic.mdb and Utopia.mdb are the main databases that store everything.
version msaccess 1.1 jet format, you will need msaccess 1.1 iit runs on win3x, can only install in win3x. After installed you can use it from winxp as i do (xp's ntvdm handles win16 apps)
edit a seperate copy of the databases, ms access seems to auto update and here seems no way to delete a row only editing rows and adding more at the bottom by typing them into the last row.
upic has two tables that need to be edited if adding, attributes and storage, there is a query table that will list the type flag for attributes such as item type/room type/ such that each entry in strogage needs a style type and item type input into the attribute table, 146 is dream style in the bob menus, the rest is self explaintory
As for photostorage, flag 2 makes it look for images in the real path and not the database. 
Flag 4 makes it use an animation file
Flag 5 only used on login door, no idea what it does
Look at a clock entry other flag numbers make it draw a clock on top of the texture.

utopia populates previews as you use bob, bob is slow frist run for this reason, and it inflates upic.mdb

FORMATS: WMF, WMF adolius version, there are more than one version of wmf, and also some EMF are named WMF in the web. to edit, save, convert, use INKSCAPE , sorry it's the only thing. there is a path for automation via image magik  to make ps files then psoedit to make wmf but the have a invisible bounding box the size of printer paper...some Postscript option must exist but i gave up. 
It eems to only render WMF for bob's assets, even though the dll can render bitmaps, editing upic to use a bmp or dib, and then loading bob with a bmp in the path you rewrote and flag 2 or more will load successfully without glitches such as unable to add items crash, but renders as non existant, this you will see a view and not a room doing this with backgrounds.

FORMATS: WAV, it seems to use wavs, one can use a hex editor to extract a wav from SHELLSND.ANI but cutting the header and renameing...

FORMATS: ANI: i have no idea how to edit these or any program that can.

FORMATS: ACT: actor files, add the elefant from safari to \actors\ and he works! he was made with all the calls. You can't replace rover by a name change rover has special calls, interactons for login. i have no idea how to edit these or any program that can. adding very old ms assitant files doesn't work, such as bonzi buddy or SAM the orginal..

APPS: PROGRAM BOXES: Utopia grabs the 32X32 pixel icon from programs it seems, also does not seem to render alpha of an icon, looks like a white square. 
The program box it self Needs at least one opaque area/path/section/layer, a single object layer of type shown in invalid.wmf with the transparacy color makes it unselectible. 

APPS: CUT CONTENT: ZIPPER: I made zipper selectible in programs, this shows credits from the coding team of MS, utopia.mdb apps table, change the flag like other built in bob apps sush as ballon

APPS: CUT CONTENT: Bob photoviewer, it doesn't exist as far as i can tell

APPS: CUT CONTENT: Gazoo-rama I have no idea what this is but upic has tons of textures for it but it seems to have been an external app like letterwritter.exe and others.

APPS: CUT CONTENT: Safari builder  it doesn't exist as far as i can tell, external app like gosafari it self
