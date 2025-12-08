
init python:

    class NotificationManager():

        def __init__(self):

            self.notify_slots_available = [True] * 7


        def show_notification(self, message):

            # Search for first availabe slot.
            for i in range( 0, len(self.notify_slots_available) ):

                if self.isNotificationSlotAvailable( i ):

                    self.claimNotificationSpot( i )

                    renpy.show_screen( "custom_notify_" + str(i + 1), message, gui.notify_ypos + i * 125, self, i)

                    break

            return

        def isNotificationSlotAvailable(self, notification_slot):

            return self.notify_slots_available[ notification_slot ]

        def claimNotificationSpot( self, notification_slot ):

            self.notify_slots_available[ notification_slot ] = False

        def releaseNotificationSpot( self, notification_slot ):

            self.notify_slots_available[ notification_slot ] = True
