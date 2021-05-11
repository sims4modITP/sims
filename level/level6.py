# functions for level 6


# First notification 
@sims4.commands.Command('notif1_level_6', command_type=sims4.commands.CommandType.Live)
def common_testing_show_basic_notification(self):
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",  # string id form string table
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
            "FOUND SOMETHING",
            "I think I have found something important ... ",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 16900524886024814375)))
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                             'Failed to show a basic notification you fucked up',
                                             exception=ex)

# Targeted Question Dialog aus Level 6

