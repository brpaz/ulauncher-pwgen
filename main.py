import json
import logging
import pwgen
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

class PwgenExtension(Extension):

    def __init__(self):
        logger.info('init Pwgen Extension')
        super(PwgenExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        
        if event.get_argument():
            pwLength = int(event.get_argument())
        else:
            pwLength = int(extension.preferences['pw_length'])
        
        pwCount = int(extension.preferences['pw_count'])
        passwords = pwgen.pwgen(pwLength, pwCount, False, False, True, True, False, True, '!$.#*+-_~()][?%&@,;', True)
        for password in passwords:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=password,
                                             description='Press Enter to copy this password to clipboard',
                                             highlightable=False,
                                             on_enter=CopyToClipboardAction(password)
                                             ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    PwgenExtension().run()
