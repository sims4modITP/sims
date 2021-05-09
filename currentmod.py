from typing import Any
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_input_float_dialog import CommonInputFloatDialog
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog
from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.utils.sims.common_sim_inventory_utils import CommonSimInventoryUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from distributor.shared_messages import IconInfoData
from ui.ui_dialog import UiDialogOk
from ui.ui_dialog_notification import UiDialogNotification
from sims4.resources import Types
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_resource_utils import CommonResourceUtils
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from statistics.skill import Skill
from sims4communitylib.enums.skills_enum import CommonSkillId
from sims4communitylib.utils.sims.common_sim_skill_utils import CommonSimSkillUtils


def run_once(function):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return function(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


class skill1:
    @run_once
    def ok1(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'This is you!',  # this is where the headline is written -> insert headline here
                'You wanted to be a computer scientist your whole life and now, finally, that dream is coming true! '
                'You just received the Letter – you are an employee at Wayfair starting Monday morning. '
                'But let’s be honest you sent too many letters of application to even remember what kind of company Wayfair'
                ' is, right? Let’s check it out!',  # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
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
                "RUG SALE!!!",
                "XXXX Area Rug\nHave a look at this beautiful handwoven rug! It is made of the finest Materials only, wisely chosen by Wayfair. The natural green colour is a perfect fit for all living rooms!\nMake your house feel like a HOME!\nDetails:\nName: XXXX Green Area Rug\nSize: Rectangle 5’ x 8’\nOverall Product Weight: 56 lb.\nFree Shipping on orders over $35.00\n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 16900524886024814375)))
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)

    @run_once
    def ok2(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'XXXXXX...',  # this is where the headline is written -> insert headline here
                'That really does sound familiar. '
                'Where do I know that name from? '
                'Wasn’t it like a childhood friend or something?',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def common_testing_show_basic_notification2(self):
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
                "Hmmmmm...",
                "This really is kind of suss, I cannot seem to get that name out of my head. \nWhere do I know it from? I must find out!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)

    @run_once
    def common_testing_show_basic_notification3(self):
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
                "Mhmm... ",
                "XXXX is still stuck in my head.\nWhere do I know you from?\n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)

    @run_once
    def ok3(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'GREEN! Of course!',  # this is where the headline is written -> insert headline here
                'It was their favourite colour! And their Name!? Now I know who XXXX was. They were a good friend from back in school, '
                'but they went missing when we were around 8 years old. How could I have forgotten!! I must have repressed the memories. '
                'I have been really close with them; it was a big shock for me when they suddenly disappeared. Police never found out where they went or what happened with them. '
                'I wish I could have at least said goodbye. But how does this rug end up having the same name as they had? I got to find out more about this.',
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)


class skill2:
    def ok(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Whats this??',  # this is where the headline is written -> insert headline here
                'I went through all the files at Wayfair and I think I found something. There is a catalogue that is signed to be for VIP’s only. '
                'But why would a furniture firm like Wayfair have a VIP membership? And why would it be sealed? Isn’t that suspicious? '
                'What is VIP furniture supposed to be and why is it so secret that it has to be sealed away from normal customers? '
                'Wouldn’t a VIP membership be a good seller? So why hide it? Also isn’t a rug just a rug? I need to get access to the data that’s in there. '
                'Let’s see what I can do about it.',
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    def item(self):
        CommonSimInventoryUtils.add_to_inventory(CommonSimUtils.get_active_sim_info(), 34330, 3)#spawn item in inventory 34330 instance id for programming book lmao


class skill3:
    @run_once
    def foo(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (
                CommonLocalizationUtils.create_localized_string(
                    2977195159,
                    text_color=CommonLocalizedStringColor.GREEN
                ),
            )
            description_tokens = (
                CommonLocalizationUtils.create_localized_string(
                    2977195159,
                    text_color=CommonLocalizedStringColor.RED
                ),
            )
            dialog = CommonBasicNotification(
                # CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
                # CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
                "",
                "Those names … and the weight. Something is strange here, why are those kept a secret? It doesn’t make any sense. But I do feel like I know these names they sound strangely familiar. Wasn’t there a case of missing children last month that had the name Charlotte Brandt in it? I have to get those police files. I just need to know for sure!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                urgency=UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)
        return 0

    @run_once
    def ok(self):
        try:
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (
                CommonLocalizationUtils.create_localized_string('Actual Story',
                                                                tokens=(CommonSimUtils.get_active_sim_info(),),
                                                                text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Connie Peyton Brown Indoor/Outdoor Area Rug',
                # this is where the headline is written -> insert headline here
                '15.08.2020 \n\n Can a rug sturdy enough for both indoor and outdoor use also be chic and attractive? This durable and fade-resistant area rug is ideal for the casual lifestyle and works just as well in covered outdoor locations such as patio or porch as they do in your living room, family room or another favorite spot. Distinguished by their high-low loop pile, this area rug takes a visual cue from hand-carved rugs but is easily affordable and designed to withstand wear. This contemporary collection ranges from linear and geometric to sprightly floral – all enhanced by dimensional pile in today’s most coveted neutral tones. \n Details: \n\n Name: Connie Peyton Brown Indoor/Outdoor Area Rug \n\n Size: Rectangle 6’ x 7’ \n\n Overall Product Weight: 49.5 lb. \n\n Free Shipping on orders over $35.00',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Show Next Object',
                                                                                   text_color=CommonLocalizedStringColor.GREEN)
            )
            # dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 7169552662410693051)))
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                                 exception=ex)  # falls error -> log

    @run_once
    def three_third_dialogue(self):
        try:
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (
                CommonLocalizationUtils.create_localized_string('Actual Story',
                                                                tokens=(CommonSimUtils.get_active_sim_info(),),
                                                                text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Charlotte Brandt White/Navy Hallway Runner',
                # this is where the headline is written -> insert headline here
                '11.03.2021 \n\n'
                'Complement your coastal - inspired decor with this breezy indoor / outdoor area rug, featuring a simple quatrefoil design. '
                'It\'s flatwoven in Turkey from water- and fade-resistant polypropylene, so it can easily stand up to tough stains and spills. '
                'The backing is safe to roll out in rooms with floor heating. '
                'And the soft navy blue and white hues work well with any color palette you can dream up. '
                'Plus, it has a low 0.09" pile height that\'s ideal for spaces with high foot traffic like the entryway or '
                'patio, and for homes with little ones and furry friends running around.\n\n'
                'Details:\n\n'
                'Name: Charlotte Brandt White/Navy Hallway Runner\n\n'
                'Size: Rectangle 5’3’’ x 7’3’’\n\n'
                'Overall Product Weight: 34.0 lb.\n\n'
                'Free Shipping on orders over $35.00',

                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Close',
                                                                                   text_color=CommonLocalizedStringColor.GREEN)
            )
            # dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 7169552662410693051)))
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                                 exception=ex)  # falls error -> log

    @run_once
    def common_testing_show_input_float_dialog(self) -> Any:
        def _on_chosen(choice: float, outcome: CommonChoiceOutcome):
            if choice == 2 or choice == 3:
                pass
            else:
                pass

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string
                            ("You nearly did it!", text_color=CommonLocalizedStringColor.BLUE),)
            description_tokens = (CommonLocalizationUtils.create_localized_string
                                      (
                                      "Your have nearly made it to the final destination of your work to reach the next hint.\nThere is one more thing you have to solve before you can take a look at it: \n\nWhat might be the Evil behind all that \n(1) Pop-Culture \n(2) Capitalism \n(3) Men ",
                                      tokens=(CommonSimUtils.get_active_sim_info(),),
                                      text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonInputFloatDialog(
                CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
                CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
                0.0,
                title_tokens=title_tokens,
                description_tokens=description_tokens
            )
            dialog.show(on_submit=_on_chosen)
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def ok1(self):
        try:
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (
                CommonLocalizationUtils.create_localized_string('Actual Story',
                                                                tokens=(CommonSimUtils.get_active_sim_info(),),
                                                                text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Valenti Remer Gray/Blue Area Rug',
                # this is where the headline is written -> insert headline here
                'Special things stand the test of time. Used look meets modern. This rug cannot be described any better. This style shows the classic counter-reaction to swish designer pieces and is so special that you need to look at least twice. Upcycling is the new trend. Exceptional colours make this small work of art into a real eye catcher with character. Anyone can do boring. The Oeko-Tex 100 certified quality is not only a low price but also durable and dirt-repellent. Of course the fabric used is suitable for use on underfloor heating. Bring a trend setter home, which sets new standards in combination with your furniture.Details:\n\n\nName: Valenti Remer Gray/Blue Area Rug\n\nSize: Rectangle 5’ x 6’\n\nOverall Product Weight: 39.5 lb.\n\nFree Shipping on orders over $35.00\n\n',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Show Next Object',
                                                                                   text_color=CommonLocalizedStringColor.GREEN)
            )
            # dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 7169552662410693051)))
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                                 exception=ex)  # falls error -> log

@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Skill, "_show_level_notification")
def _load_skill1(original, self, *args, **kwargs) -> Any:
    simsskill = CommonSimSkillUtils.get_current_skill_level(CommonSimUtils.get_active_sim_info(),
                                                            CommonSkillId.ADULT_MAJOR_PROGRAMMING)
    if simsskill == 1:
        skill1().ok1()
        skill1().common_testing_show_basic_notification()
        skill1().ok2()
        skill1().common_testing_show_basic_notification2()
        skill1().common_testing_show_basic_notification3()
        skill1().ok3()
    return original(self, *args, **kwargs)

@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Skill, "on_skill_level_up")
def _load_foo(original, self, *args, **kwargs) -> Any:
    simsskill = CommonSimSkillUtils.get_current_skill_level(CommonSimUtils.get_active_sim_info(), CommonSkillId.ADULT_MAJOR_PROGRAMMING)
    if simsskill == 2:
        skill2().ok()
        #skill2().item()
    elif simsskill == 3:
        skill3().ok1()
        skill3().ok()
        skill3().three_third_dialogue()
        skill3().common_testing_show_input_float_dialog()
        skill3().foo()
    return original(self, *args, **kwargs)
