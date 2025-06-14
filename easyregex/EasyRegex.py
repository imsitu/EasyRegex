"""Translate simple English phrases to regular expressions."""

from __future__ import annotations

import regex


class EasyRegex:
    """Utility for generating regular expressions from English phrases."""

    TOKEN_MAP = {
        "digit": r"\d",
        "digits": r"\d",
        "number": r"\d",
        "numbers": r"\d",
        "letter": r"[A-Za-z]",
        "letters": r"[A-Za-z]",
        "alphabet": r"[A-Za-z]",
        "alphabets": r"[A-Za-z]",
        "word": r"\w",
        "whitespace": r"\s",
        "space": " ",
        "tab": r"\t",
        "any": ".",
        "dot": r"\.",
    }

    def english_to_regex(self, phrase: str) -> str:
        """Return a regex pattern string for a given English phrase.

        The translation is intentionally simple and only supports a
        subset of common regex constructs. Unknown words are treated
        as literal text.
        """

        tokens = regex.findall(r'"[^"]+"|\S+', phrase.lower())
        pattern_parts: list[str] = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            # Anchors: start/end of string
            if tokens[i:i + 3] == ["start", "of", "string"]:
                pattern_parts.append("^")
                i += 3
                continue
            if tokens[i:i + 3] == ["end", "of", "string"]:
                pattern_parts.append("$")
                i += 3
                continue

            # Determine base pattern
            if token in self.TOKEN_MAP:
                base = self.TOKEN_MAP[token]
                i += 1
            elif token.startswith('"') and token.endswith('"'):
                base = regex.escape(token[1:-1])
                i += 1
            else:
                base = regex.escape(token)
                i += 1

            # Check for quantifier phrases following the base token
            if tokens[i:i + 3] == ["one", "or", "more"]:
                base += "+"
                i += 3
            elif tokens[i:i + 3] == ["zero", "or", "more"]:
                base += "*"
                i += 3
            elif i < len(tokens) and tokens[i] == "optional":
                base += "?"
                i += 1
            elif i + 1 < len(tokens) and tokens[i] == "exactly" and tokens[i + 1].isdigit():
                base += f"{{{tokens[i + 1]}}}"
                i += 2
            elif i + 2 < len(tokens) and tokens[i] == "at" and tokens[i + 1] == "least" and tokens[i + 2].isdigit():
                base += f"{{{tokens[i + 2]},}}"
                i += 3
            elif (
                i + 3 < len(tokens)
                and tokens[i] == "between"
                and tokens[i + 1].isdigit()
                and tokens[i + 2] == "and"
                and tokens[i + 3].isdigit()
            ):
                base += f"{{{tokens[i + 1]},{tokens[i + 3]}}}"
                i += 4

            pattern_parts.append(base)

        return "".join(pattern_parts)

    def compile(self, phrase: str, flags: int = 0) -> regex.Pattern:
        """Compile an English phrase into a :class:`regex.Pattern`."""

        return regex.compile(self.english_to_regex(phrase), flags)

    # Convenience wrappers around ``regex`` searching functions
    def search(self, phrase: str, text: str, flags: int = 0):
        return self.compile(phrase, flags).search(text)

    def match(self, phrase: str, text: str, flags: int = 0):
        return self.compile(phrase, flags).match(text)

    def fullmatch(self, phrase: str, text: str, flags: int = 0):
        return self.compile(phrase, flags).fullmatch(text)
