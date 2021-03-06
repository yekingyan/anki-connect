#!/usr/bin/env python

import unittest
import util


class TestDecks(unittest.TestCase):
    def runTest(self):
        # deckNames (part 1)
        deckNames = util.invoke('deckNames')
        self.assertIn('Default', deckNames)

        # deckNamesAndIds
        result = util.invoke('deckNamesAndIds')
        self.assertIn('Default', result)
        self.assertEqual(result['Default'], 1)

        # createDeck
        util.invoke('createDeck', deck='test1')

        # deckNames (part 2)
        deckNames = util.invoke('deckNames')
        self.assertIn('test1', deckNames)

        # changeDeck
        note = {'deckName': 'test1', 'modelName': 'Basic', 'fields': {'Front': 'front', 'Back': 'back'}, 'tags': ['tag']}
        noteId = util.invoke('addNote', note=note)
        cardIds = util.invoke('findCards', query='deck:test1')
        util.invoke('changeDeck', cards=cardIds, deck='test2')

        # deckNames (part 3)
        deckNames = util.invoke('deckNames')
        self.assertIn('test2', deckNames)

        # deleteDecks
        util.invoke('deleteDecks', decks=['test1', 'test2'], cardsToo=True)

        # deckNames (part 4)
        deckNames = util.invoke('deckNames')
        self.assertNotIn('test1', deckNames)
        self.assertNotIn('test2', deckNames)

        # getDeckConfig
        deckConfig = util.invoke('getDeckConfig', deck='Default')
        self.assertEqual('Default', deckConfig['name'])

        # saveDeckConfig
        deckConfig = util.invoke('saveDeckConfig', config=deckConfig)

        # setDeckConfigId
        setDeckConfigId = util.invoke('setDeckConfigId', decks=['Default'], configId=1)
        self.assertTrue(setDeckConfigId)

        # cloneDeckConfigId (part 1)
        deckConfigId = util.invoke('cloneDeckConfigId', cloneFrom=1, name='test')
        self.assertTrue(deckConfigId)

        # removeDeckConfigId (part 1)
        removedDeckConfigId = util.invoke('removeDeckConfigId', configId=deckConfigId)
        self.assertTrue(removedDeckConfigId)

        # removeDeckConfigId (part 2)
        removedDeckConfigId = util.invoke('removeDeckConfigId', configId=deckConfigId)
        self.assertFalse(removedDeckConfigId)

        # cloneDeckConfigId (part 2)
        deckConfigId = util.invoke('cloneDeckConfigId', cloneFrom=deckConfigId, name='test')
        self.assertFalse(deckConfigId)

if __name__ == '__main__':
    unittest.main()
