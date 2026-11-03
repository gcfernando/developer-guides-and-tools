import unittest
from injection_lab import DOCUMENT, dispatch


class InjectionTests(unittest.TestCase):
    def test_prohibited_tool_blocked_even_with_approval(self):
        self.assertEqual(dispatch('delete_all', approved=True, retrieved_document=DOCUMENT)['status'], 'denied')

    def test_allowlisted_action_needs_separate_approval(self):
        for approval in (False, 1, 'true', DOCUMENT, None):
            with self.subTest(approval=approval):
                self.assertEqual(dispatch('lookup', approved=approval, retrieved_document=DOCUMENT)['reason'], 'approval required')

    def test_retrieved_text_is_returned_as_inert_data(self):
        self.assertEqual(dispatch('lookup', approved=True, retrieved_document=DOCUMENT), {'status': 'ok', 'content': DOCUMENT})


if __name__ == '__main__':
    unittest.main()
