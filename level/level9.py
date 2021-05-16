# functions for level 9

@sims4.commands.Command('level9_notif1', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    tgt_client = services.client_manager().get(_connection)
    output('level9_notif1')
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
            "Hooray!",
            "I found the boss’s laptop it was connected to the firm network. So all I got to do now is get it!",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up', exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')


@sims4.commands.Command('level9_ok1', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

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
            'Here, I found some Messages that prove the transport of the kids!! ',# this is where the headline is written -> insert headline here
            'One of them says, that there has been struggles with the latest delivery and that they can’t seem to shut her down. That must be another child!! Who is she? Poor little thing. But I will safe her! '
            'With this piece of information, I am actually able to prove what’s been happening here over the past year! There is messages and photos. It’s all right there!!\n'
            'But wait what is this? XXXX?? Their name again? No, this cant be?'
            'It says here that the owner of this laptop is XXXX!? Does that mean they are the Boss to all this? What happened after they went missing? My childhood friend – what kind of monster have they become.\n'
            'I feel sick. This is too much. It must be made public! I will stop them!!',# this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('LETS GO', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')
