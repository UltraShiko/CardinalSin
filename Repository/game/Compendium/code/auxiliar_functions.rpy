
define compendium_unlock_sound_effect = "audio/SFX/Scribble.ogg"

init 2 python:

    def unlockCompendionEntry( compendium_entry_ID ):

        global persistent
        global compendium_unlock_sound_effect

        # Check if compendium entry_ID is not yet unlocked.
        if persistent.compendium.isEntryLocked_ID( compendium_entry_ID ):

            persistent.compendium.unlockEntry( compendium_entry_ID )

            if not renpy.music.get_playing(channel='notification') == compendium_unlock_sound_effect:

                renpy.music.play( compendium_unlock_sound_effect, channel='notification' )

            notification_system.show_notification("{size=-10}Unlocked lore entry:\n{/size}" + persistent.compendium.getEntryTitle_ID( compendium_entry_ID ) )

        renpy.save_persistent()

        # # Check if all entries are unlocked.
        # if persistent.compendium.areAllEntriesUnlocked():
        #
        #     grantAchievement("Loremaster")

        return

    def clearCompedium():

        global persistent

        persistent.compendium.clear()

        renpy.save_persistent()

        return
