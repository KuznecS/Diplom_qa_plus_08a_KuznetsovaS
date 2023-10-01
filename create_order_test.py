# Кузнецова Светлана, qa_plus_08-а — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_get_order_by_track():
    response = sender_stand_request.post_new_order()
    track = response.json()["track"]

    response = sender_stand_request.get_new_order_track(track)
    assert response.status_code == 200


