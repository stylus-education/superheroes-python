from superheroes_python.main import battle


def test_battle_returns_the_hero_if_they_have_a_higher_score(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=
        {
            "items": [
                {"name": 'Winner', "score": 9.0, type: 'hero'},
                {"name": 'Loser', "score": 8.0, type: 'villain'}
            ]
        }
    )

    assert battle("Winner", "Loser") == {"name": 'Winner', "score": 9.0, type: 'hero'}


