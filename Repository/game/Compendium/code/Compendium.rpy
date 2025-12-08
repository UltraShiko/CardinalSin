
python early:

    class Compendium():

        def __init__( self, list_of_entries ):

            self.entry_list = []
            self.entry_dictionary = {}

            # Check if all entries are valid.
            for i in range( 0, len( list_of_entries ) ):

                # Check if entry is of correct type.
                if not type( list_of_entries[i] ) is CompendiumEntry:

                    raise Exception( "Trying to add an Entry to the Compendium that is not of the correct type.)" )

                # Check if ID already exists. No two entries should have the same ID.
                if list_of_entries[i].getID() in self.entry_dictionary:

                    raise Exception( "Trying to add an Entry with a repeated ID. Problematic ID is " + list_of_entries[i].getID() )

                # Add current entry to list and dictionary.
                self.entry_list.append( list_of_entries[i] )
                self.entry_dictionary[ list_of_entries[i].getID() ] = list_of_entries[i]

        def numberOfEntries(self):

            return len( self.entry_list )

        def clear(self):

            # Lock all entries again.
            for entry_ID in self.entry_dictionary.keys():

                self.clearEntry( entry_ID )

        ### Title related.

        def getEntryTitle( self, entry_index ):

            return self.entry_list[ entry_index ].getTitle()

        def getEntryTitle_ID( self, entry_ID ):

            return self.entry_dictionary[ entry_ID ].getTitle()

        ### Content related.

        def getEntryContent( self, entry_index ):

            return self.entry_list[ entry_index ].getContent()

        ### Lock related.

        def lockEntry( self, entry_ID ):

            self.entry_dictionary[ entry_ID ].lock()

        def unlockEntry( self, entry_ID ):

            self.entry_dictionary[ entry_ID ].unlock()

        def isEntryLocked( self, entry_index ):

            return self.entry_list[ entry_index ].isLocked()

        def isEntryLocked_ID( self, entry_ID ):

            return self.entry_dictionary[ entry_ID ].isLocked()

        def clearEntry( self, entry_ID ):

            return self.entry_dictionary[ entry_ID ].clear()

        ### Other

        def areAllEntriesUnlocked( self ):

            # Check if any entries are locked.
            for index in range( 0, self.numberOfEntries() ):

                if self.isEntryLocked( index ) is True:

                    return False

            # If all checks pass, then the compendium is fully unlocked.
            return True

        ### Operators

        def __eq__(self, other):

            if not isinstance(other, Compendium):

                return False

            return ( self.entry_list == other.entry_list and self.entry_dictionary == other.entry_dictionary )

        ### Debug

        def unlockAllEntries(self):

            for entry in self.entry_list:

                entry.unlock()

            return
