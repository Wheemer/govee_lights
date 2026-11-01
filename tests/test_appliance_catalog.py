"""Keep the APK-confirmed local appliance catalog from silently shrinking."""

import ast
from pathlib import Path


CONST_PATH = Path(__file__).parents[1] / "custom_components" / "govee_unified" / "const.py"


def _literal_set(name: str) -> set[str]:
    tree = ast.parse(CONST_PATH.read_text(encoding="utf-8"))
    for statement in tree.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in statement.targets
        ):
            value = statement.value
            assert isinstance(value, ast.Call)
            return set(ast.literal_eval(value.args[0]))
    raise AssertionError(f"{name} was not found")


def test_shared_switch_appliance_aliases_are_retained() -> None:
    """Aliases registered by the APK's shared SwitchController modules stay local."""
    expected = {
        "H7102",
        "H7103",
        "H7107",
        "H7124",
        "H7127",
        "H7128",
        "H712C",
        "H7131",
        "H7134",
        "H7136",
        "H7137",
        "H7138",
        "H713A",
        "H713B",
        "H713C",
        "H713D",
        "H713E",
        "H7146",
        "H7147",
        "H7148",
        "H714E",
        "H7153",
        "H7162",
        "H717A",
    }
    assert expected <= _literal_set("SIMPLE_POWER_APPLIANCE_MODELS")


def test_ice_maker_variants_keep_their_distinct_power_frame() -> None:
    assert _literal_set("ICE_MAKER_MODELS") == {"H7172", "H7178", "H717D"}
