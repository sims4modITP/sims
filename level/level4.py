# functions for level 4

@sims4.commands.Command('level4_notif1', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    tgt_client = services.client_manager().get(_connection)
    output('level4_notif1')
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",#string id form string table
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        dialog = CommonBasicNotification(
            "The truth...",
            "There is only one way to find out the truth. I have to hack the police system!\n",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up', exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')


@sims4.commands.Command('level4_ok1', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog. level4_ok1')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'PIC',# this is where the headline is written -> insert headline here
            'Name: Valenti Remer\n'
            'Gender: Male\n'
            'Age: 5\n'
            'Weight: 39.5 lb\n'
            'Height: 42.5"\n'
            'Missing since: 27.03.2020\n'
            'Last seen in Northville, New York\n'
            'Description:\n'
            'Went missing while playing in a field near his house. Wore a blue jacket, black trousers and sneakers. Last seen by his mother in the kitchen, where he got himself a glass of water.',# this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')


@sims4.commands.Command('level4_ok2', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog. level4_ok2')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'PIC',# this is where the headline is written -> insert headline here
            'Name: Connie Peyton\n'
            'Gender: Female\n'
            'Age: 7\n'
            'Weight: 49.5 lb\n'
            'Height: 47.7"\n'
            'Missing since: 15.08.2020\n'
            'Last seen in Boston, Massachusetts\n'
            'Description:\n'
            'Went missing on her way home from school. Wore a blue dress, brown sandals and a bow tie in her hair. Last seen by friends at school at 12:35 o’clock.',# this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')


@sims4.commands.Command('level4_ok3', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog. level4_ok3')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'PIC',# this is where the headline is written -> insert headline here
            'Name: Name: Charlotte Brandt\n'
            'Gender: Female\n'
            'Age: 4\n'
            'Weight: 34.0 lb\n'
            'Height: 39.5"\n'
            'Missing since: 11.03.2021\n'
            'Last seen in New York City, New York\n'
            'Description:\n'
            'Went missing in the metro while with her mother. Wore a white jacket. Last seen by said mother while buying a ticket. Reported immediately.',# this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')


@sims4.commands.Command('level4_notif2', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    tgt_client = services.client_manager().get(_connection)
    output('level4_notif2')
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",#string id form string table
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        dialog = CommonBasicNotification(
            "A MATCH",
            "All ages, dates and even NAMES seem to match?!?! How is that even possible? I wanted to just prove myself wrong and get my overly curious mind some rest, but what am I to do with this now? It’s not enough to actually prove it. Police will never believe me. Its my word against theirs. Besides that, I didn’t exactly get the files the legal way… I am on my own now. But I have to find out what this really is!! \n",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up', exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')
