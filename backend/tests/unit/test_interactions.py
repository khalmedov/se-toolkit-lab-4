"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_excludes_interaction_with_different_learner_id():
    """
    Test that filtering by item_id returns interactions with that item_id
    even if they have different learner_ids
    """
    from app.models.interaction import InteractionLog
    
    # Создаем тестовые данные как объекты InteractionLog
    interactions = [
        InteractionLog(id=1, item_id=1, learner_id=1, kind="like"),
        InteractionLog(id=2, item_id=1, learner_id=2, kind="like"),  # Должна быть найдена
        InteractionLog(id=3, item_id=2, learner_id=1, kind="like"),
    ]
    
    # Фильтруем по item_id=1
    from app.routers.interactions import _filter_by_item_id
    filtered = _filter_by_item_id(interactions, 1)
    
    # Проверяем, что нашлась interaction с item_id=1 и learner_id=2
    assert len(filtered) == 2, f"Expected 2 interactions, got {len(filtered)}"
    assert any(i.id == 2 for i in filtered), "Interaction with id=2 should be in results"
