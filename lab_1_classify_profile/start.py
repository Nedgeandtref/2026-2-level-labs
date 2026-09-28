"""
Language detection starter.
"""
# pylint: disable=unused-variable, duplicate-code
import lab_1_classify_profile.main


def main() -> None:
    """
    Launches an implementation.
    """
    with open("lab_1_classify_profile/assets/texts/de.txt", "r", encoding="utf-8") as file:
        de_text = file.read()
    with open("lab_1_classify_profile/assets/texts/unknown.txt", "r", encoding="utf-8") as file:
        unknown_text = file.read()
    with open("lab_1_classify_profile/assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    with open("lab_1_classify_profile/assets/texts/en.txt", "r", encoding="utf-8") as file:
        en_text = file.read()
    de_tokens = lab_1_classify_profile.main.tokenize(de_text)
    de_tokens = lab_1_classify_profile.main.remove_stop_words(de_tokens, stopwords)
    de_frequency = lab_1_classify_profile.main.calculate_frequencies(de_tokens)
    result = lab_1_classify_profile.main.get_top_n_words(de_frequency, 7)
    assert result, "Detection result is None"
    print(result)

if __name__ == "__main__":
    main()
