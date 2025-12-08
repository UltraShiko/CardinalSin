
python early:

    class CompendiumEntry():

        def __init__(self, inner_ID, entry_title, entry_content, locked_by_default=True):

            self.ID = inner_ID
            self.title = entry_title
            self.content = entry_content
            self.locked_default_state = locked_by_default

            self.locked = locked_by_default

        ### ID related

        def getID(self):

            return self.ID

        def setID(self, new_ID):

            self.ID = new_ID

        def checkIfSameID( self, other_ID ):

            return self.ID == other_ID

        ### Title related.

        def getTitle(self):

            return self.title

        def setTitle( self, new_title ):

            self.title = new_title

        ### Content related.

        def getContent(self):

            return self.content

        def setContent( self, new_content ):

            self.content = new_content

        ### Lock related.

        def lock(self):

            self.locked = True

        def unlock(self):

            self.locked = False

        def isLocked(self):

            return ( self.locked == True )

        def getLockDefaultState(self):

            return self.locked_default_state

        def clear(self):

            self.locked = self.locked_default_state



        ### Operators

        def __eq__(self, other):

            if not isinstance(other, CompendiumEntry):

                return False

            return ( self.ID == other.ID and self.title == other.title and self.content == other.content and self.locked == self.locked )
