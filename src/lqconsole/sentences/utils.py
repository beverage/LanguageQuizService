import json

from .models import DirectObject, IndirectPronoun, Negation
from lqconsole.utils.console import Answers, Color, Style

def problem_formatter(sentences) -> str:

    output: str = ""

    for sentence in sentences:

        output = output + " ".join(
            [Answers.CORRECT if sentence.is_correct is True else Answers.INCORRECT,
             f"{Color.LIGHT_GRAY}{"COD" if sentence.direct_object != DirectObject.none.name else "---"}{Style.RESET}",
             f"{Color.LIGHT_GRAY}{"COI" if sentence.indirect_pronoun != IndirectPronoun.none.name else "---"}{Style.RESET}",
             f"{Color.LIGHT_GRAY}{"NEG" if sentence.negation != Negation.none.name else "---"}{Style.RESET}",
             sentence.content,
             f"{Color.BRIGHT_BLUE}({sentence.translation}){Style.RESET}" if sentence.is_correct else f"{Color.LIGHT_RED}({sentence.translation}){Style.RESET}",
            '\n'])

    return output

def clean_json_output(raw_output: str) -> dict:
    try:
        raw_json = raw_output.strip("```json").strip("```").strip()
        return json.loads(raw_json)
    except json.JSONDecodeError:
        raise ValueError("Malformed JSON received: " + raw_output)
