import importlib
import sys

import streamlit as st

from app import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go HIGHER!")


def test_check_guess_swapped_hint_messages():
    # Regression test for the hint message bug fix.
    assert check_guess(60, 50) == ("Too High", "📈 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📉 Go HIGHER!")


def test_guess_prompt_matches_difficulty_range(monkeypatch):
    """The displayed prompt should use the selected difficulty range."""

    class DummyContext:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

    class DummyState(dict):
        def __getattr__(self, name):
            return self.get(name)

        def __setattr__(self, name, value):
            self[name] = value

    dummy_state = DummyState(secret=1, attempts=1,
                             score=0, status="playing", history=[])
    monkeypatch.setattr(st, "session_state", dummy_state)
    monkeypatch.setattr(st, "set_page_config", lambda *args, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "selectbox",
                        lambda *args, **kwargs: "Easy")
    monkeypatch.setattr(st.sidebar, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "title", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "subheader", lambda *args, **kwargs: None)

    captured = {}

    def fake_info(message, *args, **kwargs):
        captured["message"] = message

    monkeypatch.setattr(st, "info", fake_info)
    monkeypatch.setattr(st, "expander", lambda *args, **kwargs: DummyContext())
    monkeypatch.setattr(st, "columns", lambda *args, **
                        kwargs: [DummyContext(), DummyContext(), DummyContext()])
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "button", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "success", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "error", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "warning", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "divider", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "balloons", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "rerun", lambda *args, **kwargs: None)

    if "app" in sys.modules:
        del sys.modules["app"]

    importlib.import_module("app")

    assert "Guess a number between 1 and 20." in captured["message"]


def test_new_game_resets_status(monkeypatch):
    """When a new game is started after a win/loss, the status should become playing."""

    class DummyContext:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

    class DummyState(dict):
        def __getattr__(self, name):
            return self.get(name)

        def __setattr__(self, name, value):
            self[name] = value

    dummy_state = DummyState(status="won")
    monkeypatch.setattr(st, "session_state", dummy_state)
    monkeypatch.setattr(st, "set_page_config", lambda *args, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "selectbox", lambda *args,
                        **kwargs: args[1][kwargs.get("index", 1)])
    monkeypatch.setattr(st.sidebar, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "title", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "caption", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "info", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "expander", lambda *args, **kwargs: DummyContext())
    monkeypatch.setattr(st, "columns", lambda *args, **
                        kwargs: [DummyContext(), DummyContext(), DummyContext()])
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")

    def fake_button(label, *args, **kwargs):
        return label == "New Game 🔁"

    monkeypatch.setattr(st, "button", fake_button)
    monkeypatch.setattr(st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(st, "success", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "error", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "warning", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "divider", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "balloons", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "rerun", lambda *args, **kwargs: None)

    if "app" in sys.modules:
        del sys.modules["app"]

    app = importlib.import_module("app")

    assert app.st.session_state.status == "playing"
    assert app.st.session_state.attempts == 0
