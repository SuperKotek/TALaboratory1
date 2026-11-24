"""Тесты для задания 07_secret.py — расшифровка сообщения срезами."""
from __future__ import annotations


SECRET_MESSAGE = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

EXPECTED_PHRASE = "в бане веник дороже денег"


def test_module_runs_without_errors(run):
    res = run("07_secret")
    assert res.returncode == 0
    assert res.stderr == ""


def test_decoded_phrase(run):
    """Расшифрованное сообщение совпадает с ожидаемой фразой."""
    res = run("07_secret")
    assert res.stdout.strip() == EXPECTED_PHRASE


def test_each_word_extracted_by_documented_rules():
    """
    Независимо проверяем каждое слово по ключу расшифровки из комментария
    задания: 4-я буква; 10..13; 6..15 через одну; 8..13 в обратном порядке;
    17..21 в обратном порядке. Номера букв — 1-индексированные.
    """
    word1 = SECRET_MESSAGE[0][3]                       # 4-я буква -> индекс 3
    word2 = SECRET_MESSAGE[1][9:13]                    # буквы 10..13 -> [9:13]
    word3 = SECRET_MESSAGE[2][5:14:2]                  # буквы 6..15 через одну
    word4 = SECRET_MESSAGE[3][12:6:-1]                 # буквы 8..13 наоборот
    word5 = SECRET_MESSAGE[4][20:15:-1]                # буквы 17..21 наоборот
    phrase = f"{word1} {word2} {word3} {word4} {word5}"
    assert phrase == EXPECTED_PHRASE


def test_phrase_has_five_words():
    """Во фразе ровно пять слов, как и зашифровано в пяти элементах списка."""
    assert len(EXPECTED_PHRASE.split()) == 5
    assert len(SECRET_MESSAGE) == 5
