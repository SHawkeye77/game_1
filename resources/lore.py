"""
This module holds all the wordy lore/text that we wouldn't want to take up a ton of space in the code.
"""

INTRODUCTION_TEXT = \
    "\n\n==========================================================\n" \
    "Date: May 10, 2045\n"\
    "Location: 1,000 km from Mars, 54,599,000 km from Earth\n"\
    "==========================================================\n"\
    "You are almost to Mars.\n"\
    "Until now, the intent of your solo flight from Earth was nothing more than an initial commute to work; you were" \
    " just hired as Mars’ “facilities manager” (glorified janitor). Minutes ago, however," \
    " you received the following message…\n"\
    "***\nDear Mr. Adams,\nOur Martian station has failed to provide their daily report for three days now." \
    " We understand this is not your main employment objective, but due to the pressing nature" \
    " of this issue and as an employee of the United Nations’ Extraterrestrial Expansion Association," \
    " we request your assistance in contacting our Martian-based communications director before" \
    " your allotted rest and integration period. We suspect the problem stems from a malfunction" \
    " with our transmitter’s photopropulsion apparatus, a problem, as you know, that is best handled by a team." \
    " It should not take longer than one work day. Thank you for your willingness to help.\n***" \
    "\nA little less than an hour later, your ship touches down at the UNEEA's Martian base...\n\n"

CONCLUSION_TEXT = "SUCCESS\nSpecial thanks to:\nOwen Murphy\nPeter Schmidt\n"

DEATH_TEXT = "GAME OVER"

#  =====================================================================================================================
#  Text for computer scenarios
#  =====================================================================================================================
GUI_LOGIN = \
    " ________________________________________________ \n" \
    "|    UNEAA SECURE SERVER AUTHENTICATION PORTAL   |\n" \
    "|                                                |\n" \
    "|             __________________                 |\n" \
    "|   USERNAME:|                  |                |\n" \
    "|             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻                 |\n" \
    "|             __________________                 |\n" \
    "|   PASSWORD:|                  |                |\n" \
    "|             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻                 |\n" \
    "|                                                |\n" \
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"

GUI_LOGIN_AFTER_FAIL = \
    " ________________________________________________ \n" \
    "|  INVALID USERNAME/PASSWORD COMBINATION         |\n" \
    "|  TRY AGAIN                                     |\n" \
    "|             __________________                 |\n" \
    "|   USERNAME:|                  |                |\n" \
    "|             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻                 |\n" \
    "|             __________________                 |\n" \
    "|   PASSWORD:|                  |                |\n" \
    "|             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻                 |\n" \
    "|                                                |\n" \
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"

COMM_DIR_POST_LOGIN_GUI = \
    " ________________________________________________ \n"\
    "| USER: DAVID LU                                 |\n"\
    "|                                                |\n" \
    "|                                                |\n" \
    "|   __________________     __________________    |\n"\
    "|  |VIEW SENT MESSAGES|   |   VIEW DRAFTS    |   |\n"\
    "|   ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻     ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻    |\n"\
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n"\
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"


COMM_DIR_SENT_MESSAGES = \
    " ________________________________________________ \n"\
    "| MAY 7, 2045                                    |\n"\
    "| 05:46 UTC                                      |\n"\
    "| SUBJECT: EXCITING NEWS                         |\n"\
    "| RECIPIENT: MARTIAN_BASE_INHABITANTS_ALL        |\n"\
    "|       ----------------------------------       |\n"\
    "| GOOD MORNING BASE EMPLOYEES,                   |\n"\
    "| I AM THRILLED TO ANNOUNCE THE BIGGEST          |\n"\
    "| ACHIEVEMENT OF OUR BASE THUS FAR. AS OF        |\n"\
    "| YESTERDAY, AROUND 21:15 UTC, THANKS TO THE     |\n"\
    "| HARD WORK OF OUR BASE'S RESEARCH TEAM, HUMANS  |\n"\
    "| NOW KNOW WE ARE NOT ALONE IN OUR EXISTENCE. A  |\n"\
    "| SMALL COLONY OF WHAT HAS BEEN DEEMED           |\n"\
    "| \"science name\" OR \"nickname\" WAS               |\n"\
    "| DISCOVERED IN OUR MINES. RESEARCH HAS BEEN,    |\n"\
    "| AND WILL CONTINUE TO BE, CONDUCTED NONSTOP ON  |\n"\
    "| THIS MICROORGANISM ON OUR LOCAL BASE UNTIL WE  |\n"\
    "| CREATE A VIABLE, SAFE WAY TO TRANSPORT A       |\n"\
    "| TO OUR TERRAN FACILITIES.                      |\n"\
    "|                                                |\n"\
    "| CONGRATULATIONS AND THANK YOU FOR BEING A PART |\n"\
    "| OF THE GREATEST ACCOMPLISHMENT ACHIEVED IN     |\n"\
    "| EXTRATERRESTRIAL HISTORY.                      |\n"\
    "|       ----------------------------------       |\n"\
    "| MAY 7, 2045                                    |\n"\
    "| 05:53 UTC                                      |\n"\
    "| SUBJECT: EXCITING NEWS - FOLLOW UP             |\n"\
    "| RECIPIENT: MARTIAN_BASE_SCIENCE_DIVISION       |\n"\
    "|       ----------------------------------       |\n"\
    "| AS BRIEFED BY...                               |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                                |\n"\
    "|                                        ______  |\n"\
    "|                                       | BACK | |\n"\
    "|                                        ⎻⎻⎻⎻⎻⎻  |\n"\
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"\

COMM_DIR_DRAFTS = \
    " ________________________________________________ \n" \
    "| DRAFT 1 *CONNECTION LOST*                      |\n" \
    "| MAY 10,2045                                    |\n" \
    "| 04:48 UTC                                      |\n" \
    "| SUBJECT: IMMEDIATE ASSISTANCE NEEDED           |\n" \
    "| RECIPIENT: UNEEA_TERRA_COMMUNICATIONS          |\n" \
    "|       ----------------------------------       |\n" \
    "|  ...                                           |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                        ______  |\n" \
    "|                                       | BACK | |\n" \
    "|                                        ⎻⎻⎻⎻⎻⎻  |\n" \
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"


FAC_MAN_POST_LOGIN_GUI = \
    " ________________________________________________ \n"\
    "| USER: EZRA ADAMS                               |\n"\
    "|                                                |\n" \
    "|                                                |\n" \
    "|   ________________       _______________       |\n"\
    "|  |INCOMPLETE TASKS|     |COMPLETED TASKS|      |\n"\
    "|   ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻       ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻       |\n"\
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n"\
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"

FAC_MAN_INCOMPLETE_TASKS = \
    " ________________________________________________ \n"\
    "| USER: EZRA ADAMS                               |\n"\
    "|                                                |\n" \
    "| INCOMPLETE TASKS/EVENTS:                       |\n" \
    "|                                                |\n" \
    "| 1. MEET WITH COMMUNICATIONS DIRECTOR FOR       |\n"\
    "|    PHOTOPROPULSION APPARATUS FIX.              |\n"\
    "|    -> LOCATION: TERRA COMMUNICATIONS ROOM      |\n" \
    "|    -> ASSIGNED BY: TERRA BASE                  |\n" \
    "|    -> DUE/STARTS: ASAP                         |\n" \
    "|    -> DESCRIPTION: ASSISTANCE REQUESTED ON     |\n" \
    "|       MALFUNCTIONING COMMUNICATIONS EQUIPMENT. |\n" \
    "|                                                |\n" \
    "| 2. MARTIAN BASE ORIENTATION                    |\n" \
    "|    -> LOCATION: MAINTENANCE ROOM               |\n" \
    "|    -> ASSIGNED BY: MARTIAN BASE                |\n" \
    "|    -> DUE/STARTS: 5/11/2045, 08:00 UTC         |\n"\
    "|    -> DESCRIPTION: INTRODUCTION TO BASE        |\n" \
    "|       DUTIES, TEAM INITIATION, EQUIPMENT       |\n" \
    "|       OVERVIEW, ETC.                           |\n" \
    "|                                                |\n" \
    "|                                        ______  |\n" \
    "|                                       | BACK | |\n" \
    "|                                        ⎻⎻⎻⎻⎻⎻  |\n" \
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"

FAC_MAN_COMPLETED_TASKS = \
    " ________________________________________________ \n" \
    "| USER: EZRA ADAMS                               |\n" \
    "|                                                |\n" \
    "| YOU HAVE NO COMPLETED TASKS.                   |\n" \
    "| PLEASE WORK HARDER.                            |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                                |\n" \
    "|                                        ______  |\n" \
    "|                                       | BACK | |\n" \
    "|                                        ⎻⎻⎻⎻⎻⎻  |\n" \
    " ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
