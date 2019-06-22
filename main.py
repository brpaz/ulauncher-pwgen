"""
Ulauncher PWGen extension.
Generates strong passwords using pwgen tool.
"""
import logging
import pwgen

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

LOGGER = logging.getLogger(__name__)


class PwgenExtension(Extension):
    """ Main Extension Constructor """

    def __init__(self):
        LOGGER.info('init Pwgen Extension')
        super(PwgenExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    """ Class that listens to the Keyboard event """

    def on_event(self, event, extension):
        """ Handles event """
        items = []

        if event.get_argument():
            pw_length = int(event.get_argument())
        else:
            pw_length = int(extension.preferences['pw_length'])

        pw_count = int(extension.preferences['pw_count'])
        passwords = pwgen.pwgen(pw_length, pw_count, False, False, True, True,
                                False, True, '!$.#*+-_~()][?%&@,;', True)
        for password in passwords:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=password,
                    description='Press Enter to copy this password to clipboard',
                    highlightable=False,
                    on_enter=CopyToClipboardAction(password)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    PwgenExtension().run()
