import unittest
from easyregex import EasyRegex

class TestEasyRegexTranslation(unittest.TestCase):
    def setUp(self):
        self.er = EasyRegex()

    def test_start_end_anchors(self):
        self.assertEqual(
            self.er.english_to_regex("start of string digit one or more end of string"),
            r"^\d+$",
        )

    def test_zero_or_more(self):
        self.assertEqual(self.er.english_to_regex("letter zero or more"), r"[A-Za-z]*")

    def test_optional(self):
        self.assertEqual(self.er.english_to_regex("digit optional"), r"\d?")

    def test_exactly(self):
        self.assertEqual(self.er.english_to_regex("number exactly 3"), r"\d{3}")

    def test_at_least(self):
        self.assertEqual(self.er.english_to_regex("digit at least 2"), r"\d{2,}")

    def test_between(self):
        self.assertEqual(
            self.er.english_to_regex("digit between 2 and 4"),
            r"\d{2,4}",
        )

    def test_literal_quotes(self):
        self.assertEqual(self.er.english_to_regex('"abc"'), r"abc")

    def test_unknown_word(self):
        self.assertEqual(self.er.english_to_regex("foo"), r"foo")

class TestEasyRegexIntegration(unittest.TestCase):
    def setUp(self):
        self.er = EasyRegex()

    def test_search(self):
        match = self.er.search("digit one or more", "abc123def")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(), "123")

    def test_match(self):
        self.assertIsNotNone(self.er.match("letter one or more", "abc"))

    def test_fullmatch(self):
        self.assertIsNotNone(
            self.er.fullmatch("start of string digit one or more end of string", "123")
        )

if __name__ == "__main__":
    unittest.main()
