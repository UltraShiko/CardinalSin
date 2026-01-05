
### Styles

style notification_system_text:

    font "fonts/gara.ttf"
    color "#511717"

style notification_system_frame is frame:

    xpadding 10
    ypadding 35
    right_padding 82
    background Frame("Compendium/NotificationManager/notification.png", 0, 35, 82, 35)


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen custom_notify(message, ypos_value, notification__system, notification_slot):

    zorder 100

    style_prefix "notify"

    frame at notify_appear:

        style "notification_system_frame"

        ypos ypos_value

        text message:

            style "notification_system_text"

    timer 3.25 action [ Hide('custom_notify'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_1(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_1'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_2(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_2'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_3(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_3'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_4(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_4'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_5(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_5'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_6(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_6'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_7(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_7'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_8(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_8'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_9(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_9'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]

screen custom_notify_10(message, ypos_value, notification__system, notification_slot):

    zorder 100

    use custom_notify(message, ypos_value, notification__system, notification_slot)

    timer 3.25 action [ Hide('custom_notify_10'), Function( notification__system.releaseNotificationSpot, notification_slot ) ]
