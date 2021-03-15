# sims

Quick Guide zum Workspace

IMPORTANT:  

Bevor ihr versucht ein Skript im Workspace zu erstellen müsst ihr eure Pfade im settings.py ,
dementsprechend wo euer Sims Pfad ist, ändern.

Also muss das hier: 

       game_folder = os.path.join('D:', os.sep, 'Games', 'The Sims 4')

z.B. zu das hier:

       game_folder = os.path.join('C:', os.sep, 'Prgramme (x86)', 'Steam', 'steamapps', 'common' 'The Sims 4') <- (das hier ist der default Steampfad)
                    
                    

                                              !!!!!!!ALSO UMBEDINGT CHECKEN WO EUER SIMS GESPEICHERT IST!!!!!!!!
                                                
                                                
Der Game Folder sollte das hier standard sein: 

        mods_folder = os.path.expanduser(os.path.join('~', 'OneDrive', 'Dokumente', 'Electronic Arts', 'The Sims 4', 'Mods')) 

(Achtet drauf ob bei euch The Sims 4 oder Die Sims 4 steht und ob es im OneDrive auch wirklich gespeichert ist)

Den creator_name könnt ihr beliebig ändern ist halt nur ein Name.

Unter Example Mod/Scripts findet ihr ein Beispiel Skript mit dem Namen example_mod.py
Dieser ist ein einfacher command den ihr im Eingabebereich eingeben könnt um den jeweiligen output rauszubekommen. Bevor ihr das machen könnt müsst ihr den compile.py ausfürhen
damit eine .ts4script Datei erstellt werden kann. Diese .ts4script Datei müsst ihr dann zum Mods Ordner verschieben sodass Sims4 diesen Mod auch benutzten kann.

NICHT VERGESSEN SCRIPT USE IN DEN SETTINGS VON SIMS ZU ENABLEN
