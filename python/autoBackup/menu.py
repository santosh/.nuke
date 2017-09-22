import nuke
import autoBackup

SantoshMenu.addCommand("autoBackup/open backup dir", "autoBackup.open_backup_dir()")
nuke.addOnScriptSave(autoBackup.make_backup)